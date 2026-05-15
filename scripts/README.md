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
