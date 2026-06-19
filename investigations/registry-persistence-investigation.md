# Registry Persistence Investigation (Sysmon Event ID 13)

## Overview

This investigation focused on detecting registry modifications associated with persistence techniques using Sysmon Event ID 13.

The objective was to determine whether persistence-related registry activity could be captured, monitored, and investigated through Splunk.

## Situation

While exploring common attacker persistence techniques, I wanted to validate whether registry modifications could be detected using Sysmon telemetry.

Windows Run keys are frequently abused by attackers to maintain persistence after system reboot.

## Initial Hypothesis

Registry modifications may represent legitimate software installations or system configuration changes.

However, modifications to persistence-related registry locations may also indicate malicious activity that requires investigation.

## Investigation

A registry Run key entry was intentionally created on the Windows endpoint to simulate a persistence technique.

I analyzed Sysmon Event ID 13 logs in Splunk and reviewed the affected registry path, modified values, and associated user activity.

## Findings

The investigation confirmed that Sysmon successfully detected and recorded the registry modification event.

The collected telemetry provided visibility into registry paths, modified values, and persistence-related activity.

## Response

Registry modification telemetry was incorporated into the monitoring strategy and dashboard to improve visibility into persistence techniques.

This provided an additional detection capability for identifying suspicious changes within the Windows endpoint.

## MITRE ATT&CK Mapping

* T1547 – Boot or Logon Autostart Execution

## Skills Demonstrated

* Persistence detection
* Registry monitoring
* Endpoint investigation
* Sysmon analysis
* MITRE ATT&CK mapping

## Lessons Learned

Registry modifications are not always malicious and may result from legitimate software installations or system changes. Monitoring persistence-related registry locations provides valuable visibility into techniques that attackers may use to maintain access after system reboot.
