import re
from collections import Counter

LOG_FILE = "clean_ssh_failed.log"

with open(LOG_FILE, "r") as file:
    logs = file.readlines()

ip_addresses = []

for line in logs:
    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

    if match:
        ip = match.group(1)
        ip_addresses.append(ip)

ip_counts = Counter(ip_addresses)

print("================================")
print("   SSH BRUTE-FORCE DETECTOR")
print("================================")

for ip, count in ip_counts.items():

    print(f"Source IP      : {ip}")
    print(f"Failed Attempts: {count}")

    if count >= 5:
        print("Severity       : HIGH")
        print("ALERT          : Possible SSH Brute-Force Attack")
    else:
        print("Severity       : LOW")
        print("Status         : No brute-force threshold reached")

    print("--------------------------------")
