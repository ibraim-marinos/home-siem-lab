# Brute Force Login Investigation (Event ID 4625)

## Overview

This investigation focused on identifying repeated failed authentication attempts using Windows Security Event ID 4625 collected through Splunk.

The objective was to determine whether authentication failures could be detected, analyzed, and investigated using centralized log collection.

## Situation

While monitoring security events in Splunk, I wanted to determine whether repeated failed authentication attempts could be detected and investigated using Windows Security logs.

Because brute-force attacks commonly generate multiple failed login events, I simulated this activity within the lab environment and validated the visibility provided by the SIEM platform.

## Initial Hypothesis

The failed logins could represent a user repeatedly entering an incorrect password.

However, when authentication failures occur multiple times within a short period, they may also indicate password guessing or brute-force activity.

## Investigation

I analyzed Windows Security Event ID 4625 logs in Splunk and created a correlation search designed to identify accounts generating multiple failed authentication attempts.

The query grouped failed login events by account name and host, helping identify suspicious authentication patterns that would normally require further investigation by a SOC analyst.

## Findings

The results showed multiple failed authentication attempts associated with the monitored Windows endpoint.

The correlation search successfully identified accounts exceeding the defined threshold, demonstrating that brute-force activity could be detected through centralized log analysis.

## Response

To improve visibility, I created a Splunk detection rule that generates an alert whenever multiple failed logon events exceed a predefined threshold.

This approach allows suspicious authentication activity to be identified quickly and supports faster triage by a SOC analyst.

## MITRE ATT&CK Mapping

* T1110 – Brute Force

## Skills Demonstrated

* Authentication log analysis
* Threat detection
* Event correlation
* SOC investigation workflow
* Splunk search development
