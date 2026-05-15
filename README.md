# Home SIEM Lab (Splunk) – Threat Detection & Incident Response

## Overview
This project demonstrates the setup and operation of a home SIEM environment using Splunk, Windows Event Logs, and Sysmon. The goal was to simulate real SOC Tier 1 workflows including log analysis, alert triage, and incident investigation.

## Detection & Monitoring Evidence

### SIEM Dashboard (Threat Overview)
![SIEM Dashboard](https://github.com/user-attachments/assets/2efffe46-9d1e-4713-889f-ef16ad7ad9d8)
*This dashboard provides a consolidated view of security events, combining multiple detection categories such as failed login attempts, PowerShell activity, and process creation logs. It enables real-time monitoring and efficient alert triage in a SOC environment.*

### Brute Force Detection (Event ID 4625)
![Brute Force](https://github.com/user-attachments/assets/716106c3-ba96-4f72-b307-ea3313c50833)
*This screenshot shows multiple failed login attempts (Event ID 4625), which were analyzed to detect potential brute-force attacks. Repeated authentication failures from the same host were identified as suspicious activity during the triage process.*

### Suspicious PowerShell Activity (Event ID 4104)
![PowerShell](https://github.com/user-attachments/assets/2260755f-3f93-4ed2-b868-045e8a514eba)
*This view highlights PowerShell script block logging (Event ID 4104), including suspicious commands such as Invoke-WebRequest. These events were analyzed to identify potentially malicious script execution and abnormal system behavior.*

## Tools & Technologies
- Splunk Enterprise
- Windows Event Logs
- Sysmon
- Splunk Universal Forwarder

## Key Activities
- Built a SIEM lab with log forwarding from Windows to Splunk
- Investigated suspicious activity such as brute force attempts and PowerShell execution
- Performed alert triage by validating and analyzing log data
- Simulated attack scenarios to generate and analyze security events

## Detection Use Cases
- Brute-force login attempts (Event ID 4625)
- Suspicious PowerShell activity (Event ID 4104)
- Process creation monitoring (Sysmon Event ID 1)
- Registry persistence detection (Sysmon Event ID 13)

## Full Report
[Home SIEM Lab Report](./home-siem-lab-report.pdf)
