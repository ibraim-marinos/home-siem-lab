# SOC Detection Scripts

This folder contains beginner SOC Analyst Python detection scripts developed as part of the Home SIEM Lab project.

---

## Scripts Included

### Failed Login Detector – Event ID 4625

Detects repeated failed login attempts from Windows authentication logs.

Features:
- Parses CSV log data
- Detects brute-force style activity
- Counts failed login attempts by user and host
- Generates SOC-style alerts

Example output:

```text
ALERT: User 'ibraim' on host 'DESKTOP-BR4IAB0' had 6 failed login attempts.
```

Related Detection:
- Windows Event ID 4625
- Brute-force detection
- Authentication monitoring
