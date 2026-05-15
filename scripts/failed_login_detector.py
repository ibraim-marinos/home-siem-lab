import csv
from collections import defaultdict

LOG_FILE = "failed_logins.csv"
THRESHOLD = 5

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        user = row.get("Account_Name", "Unknown")
        host = row.get("host", "Unknown")

        key = (user, host)
        failed_attempts[key] += 1

print("Failed Login Detection Results")
print("-" * 35)

for (user, host), count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"ALERT: User '{user}' on host '{host}' had {count} failed login attempts.")