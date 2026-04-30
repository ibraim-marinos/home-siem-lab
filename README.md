# Home SIEM Lab (Splunk) – Threat Detection & Incident Response

## Overview
This project demonstrates the setup and operation of a home SIEM environment using Splunk, Windows Event Logs, and Sysmon. The goal was to simulate real SOC Tier 1 workflows including log analysis, alert triage, and incident investigation.

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
