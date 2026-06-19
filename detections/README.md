# Detection Rules

This section documents the detection logic developed and validated throughout the Home SIEM project.

## Detection 1 – Failed Login Activity (Event ID 4625)

Purpose:
Identify accounts generating multiple failed authentication attempts.

Detection Logic:

```spl
index=main source="WinEventLog:Security" EventCode=4625
| stats count as failed_attempts by Account_Name, host
| where failed_attempts >= 5
```

MITRE ATT&CK:

* T1110 – Brute Force

---

## Detection 2 – Suspicious PowerShell Activity (Event ID 4104)

Purpose:
Monitor PowerShell script execution activity.

Detection Logic:

```spl
index=main sourcetype="XmlWinEventLog:Microsoft-Windows-PowerShell/Operational" EventID=4104
| table _time host ScriptBlockText
| sort -_time
```

MITRE ATT&CK:

* T1059.001 – PowerShell

---

## Detection 3 – Process Creation Activity (Sysmon Event ID 1)

Purpose:
Monitor process execution activity.

Detection Logic:

```spl
index=main sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventID=1
| table _time host Image CommandLine User
| sort -_time
```

MITRE ATT&CK:

* T1057 – Process Discovery

---

## Detection 4 – Registry Persistence Activity (Sysmon Event ID 13)

Purpose:
Monitor registry modifications associated with persistence.

Detection Logic:

```spl
index=main sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventID=13
| table _time host TargetObject Details User
| sort -_time
```

MITRE ATT&CK:

* T1547 – Boot or Logon Autostart Execution

