# SOC Detection Scripts

This folder contains Python detection scripts developed as part of the Home SIEM Lab project.

---

# Failed Login Detector – Event ID 4625

## Purpose

This Python script analyzes failed Windows login events and identifies repeated authentication failures that may indicate brute-force activity.

## Features

- Parses CSV log data
- Detects repeated failed login attempts
- Identifies username, host, and source IP
- Uses configurable alert threshold
- Simulates SOC alert triage workflow
- Maps detection to MITRE ATT&CK T1110

## Detection Logic

- Windows Event ID: 4625
- MITRE ATT&CK: T1110 – Brute Force
- Threshold: 5 failed login attempts

## Example Output

See:
- `failed-login-bruteforce-detection.png`

## Skills Demonstrated

- Python scripting
- Log analysis
- SOC alert triage
- Threat detection
- CSV parsing
- Basic detection engineering


---

# Suspicious PowerShell Detector – Event ID 4104

## Purpose

This Python script analyzes PowerShell execution logs and detects suspicious commands commonly associated with malicious activity.

## Features

- Detects suspicious PowerShell commands
- Identifies HIGH and CRITICAL severity activity
- Detects encoded commands and download attempts
- Maps detections to MITRE ATT&CK
- Simulates SOC alert triage workflow

## Detection Logic

- Windows Event ID: 4104
- MITRE ATT&CK: T1059.001 – PowerShell

## Example Output

See:
- `powershell-suspicious-detection.png`

## Skills Demonstrated

- Python scripting
- Log analysis
- Threat detection
- Detection engineering
- SOC alert triage
- MITRE ATT&CK mapping
