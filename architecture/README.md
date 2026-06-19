# Home SIEM Lab Architecture

## Overview

This lab was designed to simulate a small Security Operations Center (SOC) environment for monitoring and investigating security events.

The environment collects Windows endpoint telemetry and forwards security logs to Splunk Enterprise for centralized analysis and threat detection.

## Components

### Ubuntu Server

- Splunk Enterprise
- Centralized log collection
- Search and reporting
- Dashboard visualization

### Windows 10 Endpoint

- Sysmon
- Windows Security Logs
- PowerShell Operational Logs
- Splunk Universal Forwarder

### Splunk Universal Forwarder

The Universal Forwarder collects Windows telemetry and securely forwards events to Splunk Enterprise for indexing and analysis.

## Data Flow

Windows Endpoint
↓
Sysmon / Windows Event Logs / PowerShell Logs
↓
Splunk Universal Forwarder
↓
Splunk Enterprise (Ubuntu)
↓
Dashboards, Searches, Investigations, and Detections

## Security Telemetry Collected

- Windows Security Event ID 4625
- PowerShell Event ID 4104
- Sysmon Event ID 1
- Sysmon Event ID 13

## Architecture Diagram

```text
+-----------------------+
| Windows 10 Endpoint   |
| Sysmon + Event Logs   |
+-----------+-----------+
            |
            |
            v
+-----------------------+
| Splunk Universal      |
| Forwarder             |
+-----------+-----------+
            |
            |
            v
+-----------------------+
| Ubuntu Server         |
| Splunk Enterprise     |
+-----------+-----------+
            |
            |
            v
+-----------------------+
| Dashboards &          |
| Investigations        |
+-----------------------+
```
