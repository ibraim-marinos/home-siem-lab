# Process Creation Investigation (Sysmon Event ID 1)

## Overview

This investigation focused on monitoring process creation activity using Sysmon Event ID 1 collected through Splunk.

The objective was to validate endpoint visibility and analyze process execution activity from a centralized SIEM platform.

## Situation

While monitoring endpoint telemetry, I wanted to determine whether process execution activity could be captured and investigated using Sysmon Event ID 1.

Process creation events provide valuable visibility into user activity, application execution, and potentially suspicious behavior occurring on a Windows endpoint.

## Initial Hypothesis

Most process creation events would represent normal user or system activity.

However, unusual processes, unexpected command-line arguments, or suspicious parent-child process relationships may indicate malicious activity that requires investigation.

## Investigation

I analyzed Sysmon Event ID 1 logs in Splunk and reviewed process names, command-line arguments, parent processes, and associated user accounts.

Several applications were intentionally executed on the endpoint, including Notepad, Calculator, Task Manager, and PowerShell, to generate process creation telemetry.

## Findings

The investigation confirmed that Sysmon successfully captured process execution activity and forwarded the events to Splunk.

The collected telemetry provided visibility into executed processes, command-line arguments, parent processes, and user context.

## Response

To improve endpoint monitoring capabilities, process creation telemetry was incorporated into the Home SIEM dashboard.

This allowed process activity to be reviewed centrally and provided additional visibility during investigations.

## MITRE ATT&CK Mapping

* T1059 – Command and Scripting Interpreter

## Skills Demonstrated

* Endpoint visibility
* Process analysis
* Command-line investigation
* Sysmon monitoring
* Splunk log analysis
