import csv

LOG_FILE = "powershell_events.csv"

SUSPICIOUS_KEYWORDS = [
    "Invoke-WebRequest",
    "DownloadString",
    "EncodedCommand",
    "IEX",
    "Start-Process"
]

print("SOC Detection Results")
print("=" * 50)

with open(LOG_FILE, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:

        user = row["Account_Name"]
        host = row["host"]
        command = row["command"]
        event_code = row["EventCode"]

        for keyword in SUSPICIOUS_KEYWORDS:

            if keyword.lower() in command.lower():

                severity = "HIGH"

                if "EncodedCommand" in command or "IEX" in command:
                    severity = "CRITICAL"

                print(f"""
[{severity}] Suspicious PowerShell Activity Detected

User: {user}
Host: {host}
Command: {command}

MITRE ATT&CK: T1059.001 - PowerShell
Detection: Windows Event ID {event_code}

Recommended Action:
Review endpoint activity and escalate if confirmed malicious.
""")

                break