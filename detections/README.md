# Detection Rules

This section contains the detection logic developed and validated during the Home SIEM project.

The detections were designed to identify suspicious activity using Windows Event Logs and Sysmon telemetry collected through Splunk Enterprise.

## Detection 1 – Brute Force Login Activity

### Data Source

* Windows Security Logs
* Event ID 4625

### Objective

Detect multiple failed authentication attempts occurring within a short period of time.

### MITRE ATT&CK

* T1110 – Brute Force

---

## Detection 2 – Suspicious PowerShell Activity

### Data Source

* PowerShell Operational Logs
* Event ID 4104

### Objective

Identify PowerShell commands that may indicate suspicious or unauthorized activity.

### MITRE ATT&CK

* T1059.001 – PowerShell

---

## Detection 3 – Process Creation Activity

### Data Source

* Sysmon Event ID 1

### Objective

Monitor process execution activity and identify unusual process behavior.

### MITRE ATT&CK

* T1057 – Process Discovery

---

## Detection 4 – Registry Persistence Activity

### Data Source

* Sysmon Event ID 13

### Objective

Detect registry modifications associated with persistence techniques.

### MITRE ATT&CK

* T1547.001 – Registry Run Keys / Startup Folder
