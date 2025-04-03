import argparse
import csv
from collections import OrderedDict
import json
import requests
from time import sleep, time
import topicinfo

import flatmate


class Client:
    def __init__(self, email, password, site, city_id, wait=10):
        if wait is None:
            wait = 10
        self.base = "https://api.govoutreach.com"
        self.site = site
        self.city_id = city_id
        self.wait = wait
        self.prevtime = None
        self.login(email, password)

    def throttle(self):
        current = time()
        if isinstance(self.prevtime, float):
            wait_time = self.prevtime + self.wait - current
            if wait_time > 0:
                print("[gogov] sleeping " + str(wait_time) + " seconds")
                sleep(wait_time)
        self.prevtime = current

    def login(self, email, password):
        url = self.base + "/users/sessions"
        headers = {"Content-Type": "application/json", "X-Gogovapps-Site": self.site}
        self.throttle()
        r = requests.post(
            url, headers=headers, json={"email": email, "password": password}
        )
        data = r.json()
        self.token = data["token"]
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self.expiry = data["expiry"]
        self.session_id = data["id"]
        return data

    def logout(self):
        print("[gogov] logging out")
        url = self.base + "/users/sessions"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "X-Gogovapps-Site": self.site,
        }
        self.throttle()
        r = requests.delete(url, headers=headers)
        data = r.json()
        print("[gogov] logged out")

    def get_all_topic_info(self):
        url = self.base + "/crm/requests/all_topic_info"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "X-Gogovapps-Site": self.site,
        }
        self.throttle()
        r = requests.get(url, headers=headers)
        data = r.json()
        return data

    def get_topics(self):
        url = self.base + "/core/crm/topics"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "X-Gogovapps-Site": self.site,
        }
        self.throttle()
        r = requests.get(url, headers=headers)
        data = r.json()
        return data

    def search(self):
        url = self.base + "/core/crm/search"
        headers = {"Authorization": self.token, "X-Gogovapps-Site": self.site}

        searchAfter = []

        results = []

        for i in range(1_000_000):
            payload = {
                "cityId": self.city_id,
                "searchAfter": searchAfter,
                "size": 100,
                "sort": [
                    {"dateEntered": {"missing": "_last", "order": "desc"}},
                    {"_id": "desc"},
                ],
            }
            print("[gogov] url:", url)
            # print("[gogov] headers:", headers)
            print("[gogov] payload:", payload)
            self.throttle()
            r = requests.post(url, headers=headers, json=payload)
            self.prevtime = (
                time()
            )  # throttle based on time the request completed (not started)
            print(
                "[gogov] response:", r.text[:500], ("..." if len(r.text) > 1000 else "")
            )
            data = r.json()

            hits = data["hits"]["hits"]

            if len(hits) == 0:
                break

            searchAfter = hits[-1]["sort"]

            sources = [hit["_source"] for hit in hits]

            results += sources

        return results

    def export_requests(self, filepath=None, fh=None, custom_fields=None):
        # all_topic_info = self.get_all_topic_info()

        # get list of all topic ids
        # all_topic_ids = [t['id'] for t in all_topic_info]

        # Make a "flat" dictionary of the topic IDs and their names to get classificationName
        topics = self.get_topics()
        topics_ids = {
            topic["id"]: topic["attributes"]["name"] for topic in topics["data"]
        }

        base_columns = OrderedDict(
            [
                ("caseId", "caseId"),
                ("caseType", "caseType"),
                ("classificationId", "classificationId"),
                ("classificationName", "N/A"),
                ("departmentId", "departmentId"),
                ("contactId", "contactId"),
                ("contact2Id", "contact2Id"),
                ("description", "description"),
                ("location", "location"),
                ("latitude", "locationPoint.lat"),
                ("longitude", "locationPoint.lon"),
                ("dateEntered", "dateEntered"),
                ("howEntered", "howEntered"),
                ("enteredById", "enteredById"),
                ("status", "status"),
                ("assignedToId", "assignedToId"),
                ("dateClosed", "dateClosed"),
                ("closedById", "closedById"),
                ("reasonClosed", "reasonClosed"),
                ("dateExpectClose", "dateExpectClose"),
                ("priority", "priority"),
                ("cecaseId", "cecaseId"),
                ("dateLastUpdated", "dateLastUpdated"),
                ("contact.firstName", "contact.firstName"),
                ("contact.lastName", "contact.lastName"),
                ("contact.phone", "contact.phone"),
            ]
        )

        custom_columns = OrderedDict([])

        all_results = []
        for page in range(1):
            results = self.search()

            for source in results:
                # overwrite custom fields, converting from list of dictionaries to a simple dictionary
                source["customFields"] = dict(
                    [
                        (fld["name"], fld["value"])
                        for fld in source["customFields"]
                        if fld.get("name")
                    ]
                )

                # add to custom fields
                if custom_fields is None:
                    for name in source["customFields"].keys():
                        if "." not in name:
                            if name not in custom_columns:
                                custom_columns[name] = ".".join(["customFields", name])

                # just want the source part
                all_results.append(source)

        if custom_fields is not None:
            custom_columns = OrderedDict(
                [(fld, ".".join(["customFields", fld])) for fld in custom_fields]
            )

        columns = OrderedDict(list(base_columns.items()) + list(custom_columns.items()))

        print("[gogov] columns:", columns)
        flattened_results = flatmate.flatten(
            all_results, columns=columns, clean=True, skip_empty_columns=False
        )

        # Add the classification name using the classification ID
        for result in flattened_results:
            result["classificationName"] = topics_ids[result["classificationId"]]

        f = fh or open(filepath, "w", newline="", encoding="utf-8")

        writer = csv.DictWriter(f, fieldnames=list(columns.keys()))
        writer.writeheader()
        writer.writerows(flattened_results)

        if fh is None:
            f.close()

    # topic_fields: Lists fields associated with each topic (minus loc., desc., etc.)
    # field_values: Lists acceptable inputs for each drop-down field (often "Yes", "No", or "Unknown")
    topic_fields, field_values = topicinfo.get_topic_field_info()

    # Function that submits a CRM request to the client's site using the GOGov API
    #   location format is as follows: {"shortAddress": _, "coordinates: {"latitude": _, "longitude": _}}
    #   description is required; be sure to include any specific information the service team may need
    #   contact_id defaults to 0; this indicates an anonymous requester
    #   assigned_to_id defaults to 0; this indicates automatic routing to the assignee
    #   "fields" param contains all other fields: [{"id": "field1", "value": "value1"}, {"id": _, "value": _}, ...]
    # See the GOGov API: https://documenter.getpostman.com/view/11428138/TVzLpgCK#69dfabaf-84b2-416f-92e0-2857e0702982
    def submit_request(
        self,
        topic_id,
        location=None,
        description=None,
        contact_id=0,
        assigned_to_id=0,
        fields=None,
    ):
        # Make a dict of all topic_id: topic_name and use it to validate the user's input for topic_id
        topics = self.get_topics()
        topic_ids = {
            topic["id"]: topic["attributes"]["name"] for topic in topics["data"]
        }
        if topic_id not in topic_ids:
            raise ValueError(f"Invalid input for topic_id: {topic_id}")

        # Raise an error if the user did not put in a location
        if location is None:
            raise ValueError("No value provided for location.")

        # Same for description
        if description is None:
            raise ValueError("No value provided for description.")

        # Make a single dict with {id}: {value} for each field dict in "fields" for input validation
        input_fields = {field["id"]: field["value"] for field in fields}

        # Get the name assoc. with topic_id and check if the input for "fields" is missing any required ones
        topic_name = topic_ids[topic_id].upper()
        # topic_name.upper()
        required_fields = self.topic_fields[topic_name]
        missing_fields = []
        for required_field in required_fields:
            if required_field not in input_fields:
                missing_fields.append(required_field)
        if len(missing_fields) > 0:
            raise ValueError(
                f"Missing ({len(missing_fields)}) required fields: {missing_fields}"
            )

        # Validate the user's input for any fields that are answered with drop-down boxes
        for field in input_fields:
            if (
                field in self.field_values
                and input_fields[field] not in self.field_values[field]
            ):
                invalid_message = f"""
                    Invalid input value for {field}: {input_fields[field]} ; 
                    list of valid input values for {field}: {self.field_values[field]}
                """
                raise ValueError(invalid_message)

        # The URL for submitting the request
        url = "https://api.govoutreach.com/crm/requests"

        # Necessary headers
        headers = {
            "Authorization": self.access_token,
            "X-Gogovapps-Site": self.site,
            "Content-Type": "application/json",
        }

        # JSON-formatted dict
        data = {
            "data": {
                "attributes": {
                    "topic-id": topic_id,
                    "description": description,
                    "contact-id": contact_id,
                    "assigned-to-id": assigned_to_id,
                    "custom-fields": fields,
                    "location": location,
                }
            }
        }

        self.throttle()
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
        print(f"[gogov] response: {response.text}")


def main():
    parser = argparse.ArgumentParser(
        prog="gogov",
        description="High-Level API Client for GoGov",
    )
    parser.add_argument(
        "method",
        help='method to run, can be "export-requests"',
    )
    parser.add_argument(
        "outpath", help="output filepath of where to save downloaded CSV"
    )
    parser.add_argument(
        "--base",
        type=str,
        help='base url for the API, like "https://api.govoutreach.com"',
    )
    parser.add_argument("--city-id", type=str, help="city id")
    parser.add_argument(
        "--custom-fields",
        type=str,
        help="comma-separated list of custom fields to include",
    )
    parser.add_argument("--email", type=str, help="email")
    parser.add_argument("--password", type=str, help="password")
    parser.add_argument("--site", type=str, help="site")
    parser.add_argument("--wait", type=float, help="wait")
    args = parser.parse_args()

    if args.method not in ["export-requests", "export_requests"]:
        raise Except("[gogov] invalid or missing method")

    client = Client(
        email=args.email,
        password=args.password,
        site=args.site,
        city_id=args.city_id,
        wait=args.wait,
    )

    if args.method in ["export-requests", "export_requests"]:
        custom_fields = args.custom_fields.split(",") if args.custom_fields else None
        client.export_requests(args.outpath, custom_fields=custom_fields)

    client.logout()


if __name__ == "__main__":
    main()
