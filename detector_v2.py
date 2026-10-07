import re
from datetime import datetime
from collections import defaultdict

LOG_FILE = "clean_ssh_failed.log"

THRESHOLD = 5
TIME_WINDOW = 60

events = []

with open(LOG_FILE, "r") as file:
    for line in file:

        timestamp_match = re.search(
            r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})",
            line
        )

        user_match = re.search(
            r"Failed password for (\S+)",
            line
        )

        ip_match = re.search(
            r"from (\d+\.\d+\.\d+\.\d+)",
            line
        )

        if timestamp_match and user_match and ip_match:

            timestamp = datetime.strptime(
                timestamp_match.group(1),
                "%Y-%m-%dT%H:%M:%S"
            )

            username = user_match.group(1)
            ip = ip_match.group(1)

            events.append({
                "time": timestamp,
                "username": username,
                "ip": ip
            })


ip_events = defaultdict(list)

for event in events:
    ip_events[event["ip"]].append(event)


print("======================================")
print("   SSH BRUTE-FORCE DETECTOR V2")
print("======================================")


for ip, attempts in ip_events.items():

    attempts.sort(key=lambda x: x["time"])

    for i in range(len(attempts)):

        start_time = attempts[i]["time"]
        window_events = []

        for event in attempts[i:]:

            difference = (
                event["time"] - start_time
            ).total_seconds()

            if difference <= TIME_WINDOW:
                window_events.append(event)
            else:
                break

        if len(window_events) >= THRESHOLD:

            print(f"Source IP       : {ip}")
            print(
                f"Username        : "
                f"{window_events[0]['username']}"
            )
            print(
                f"Failed Attempts : "
                f"{len(window_events)}"
            )
            print(
                f"Time Window     : "
                f"{start_time} to "
                f"{window_events[-1]['time']}"
            )
            print("Severity        : HIGH")
            print(
                "ALERT           : "
                "Possible SSH Brute-Force Attack"
            )
            print("--------------------------------------")

            break
