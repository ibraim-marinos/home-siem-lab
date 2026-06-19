# Suspicious PowerShell Activity Investigation (Event ID 4104)

## Overview

This investigation focused on monitoring and analyzing PowerShell activity using Windows PowerShell Operational Event ID 4104 collected through Splunk.

The objective was to determine whether PowerShell commands could be effectively monitored and whether potentially suspicious activity could be identified through centralized logging.

## Situation

While reviewing endpoint telemetry in Splunk, I wanted to determine whether PowerShell activity could be monitored effectively and whether potentially suspicious commands could be identified through centralized logging.

Because PowerShell is commonly used by attackers for reconnaissance, payload execution, persistence, and administrative tasks, visibility into script execution was an important capability to validate within the lab environment.

## Initial Hypothesis

Not all PowerShell activity is malicious.

Many commands are executed as part of normal administrative operations. However, unusual or unexpected PowerShell commands may indicate malicious behavior and should be investigated further.

## Investigation

I analyzed Windows PowerShell Operational logs (Event ID 4104) collected in Splunk.

The investigation focused on script block logging, allowing me to review executed PowerShell commands and identify activity that would warrant additional investigation in a SOC environment.

Several PowerShell commands were intentionally executed on the endpoint to generate telemetry and validate detection visibility.

## Findings

The PowerShell logs provided detailed visibility into commands executed on the Windows endpoint and confirmed that script block logging was functioning correctly.

The investigation successfully captured administrative and test commands, demonstrating that PowerShell activity could be monitored and reviewed through centralized logging.

## Response

To improve endpoint visibility, I incorporated PowerShell logging into the monitoring strategy and validated that Event ID 4104 telemetry was consistently reaching Splunk.

This provided detailed command execution visibility and improved the ability to investigate potentially suspicious PowerShell activity.

## MITRE ATT&CK Mapping

* T1059.001 – PowerShell

## Skills Demonstrated

* PowerShell analysis
* Script block logging investigation
* Threat detection
* Log analysis
* SOC investigation workflow
* Splunk search development
