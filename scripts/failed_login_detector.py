import csv
from collections import defaultdict

LOG_FILE = "failed_logins.csv"
THRESHOLD = 5

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        user = row["Account_Name"]
        host = row["host"]
        source_ip = row["source_ip"]
        timestamp = row["timestamp"]

        key = (user, host, source_ip)

        failed_attempts[key] += 1

print("SOC Detection Results")
print("=" * 50)

for (user, host, source_ip), count in failed_attempts.items():

    if count >= THRESHOLD:

        print(f"""
[HIGH] Possible Brute Force Detected

User: {user}
Host: {host}
Source IP: {source_ip}
Failed Attempts: {count}

MITRE ATT&CK: T1110
Detection: Windows Event ID 4625
""")