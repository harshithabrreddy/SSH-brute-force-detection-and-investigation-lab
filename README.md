# SSH Brute-Force Detection and Investigation

## Project Overview

This project demonstrates a SOC workflow for detecting, investigating, and documenting SSH brute-force activity using Linux authentication logs and Python.

## Objectives

- Collect SSH authentication logs
- Detect failed SSH login attempts
- Identify source IP and targeted username
- Detect repeated failures within a time window
- Generate a security alert
- Investigate the alert
- Map the activity to MITRE ATT&CK
- Create an incident report

## Lab Environment

- Operating System: Ubuntu Linux (WSL)
- SSH: OpenSSH Server
- Log Source: /var/log/auth.log
- Programming Language: Python 3
- Detection Method: Python log analysis

## Detection Rule

5 or more failed SSH authentication attempts from the same source IP within 60 seconds generate a HIGH severity alert.

## Detection Workflow

SSH Authentication
|
v
/var/log/auth.log
|
v
Failed SSH Events
|
v
Python Detection
|
v
Source IP + Username
|
v
5 Attempts / 60 Seconds
|
v
HIGH Severity Alert
|
v
SOC Investigation
|
v
MITRE ATT&CK Mapping
|
v
Incident Report

## Sample Detection

Source IP: 127.0.0.1

Target Username: harshithabr

Failed Attempts: 6

Time Window: 53 seconds

Severity: HIGH

Alert: Possible SSH Brute-Force Attack

## Investigation Result

The alert was investigated by reviewing SSH authentication logs and checking for successful authentication events.

No successful SSH login was identified during the investigation.

The activity was intentionally generated as part of a controlled cybersecurity lab.

Final Classification: BENIGN / AUTHORIZED LAB ACTIVITY

## MITRE ATT&CK Mapping

- Tactic: Credential Access
- Technique: T1110 - Brute Force
- Sub-technique: T1110.001 - Password Guessing

## Project Files

- detector.py - Basic SSH failed-login detector
- detector_v2.py - Time-window brute-force detector
- clean_ssh_failed.log - Clean SSH failure evidence
- ssh_failed.log - Raw project log sample
- alert.txt - Generated SOC alert
- mitre_mapping.md - MITRE ATT&CK mapping
- incident_report.md - Incident investigation report

## Key SOC Concepts Demonstrated

- Log analysis
- Alert detection
- Threshold-based detection
- Time-window detection
- Source IP analysis
- Authentication investigation
- Alert classification
- MITRE ATT&CK mapping
- Incident reporting

## Future Improvements

- Detect external attacker IP addresses
- Add GeoIP enrichment
- Generate JSON alerts
- Integrate with Splunk
- Integrate with Wazuh
- Add automated alerting

## Disclaimer

This project was performed in a controlled personal lab environment for cybersecurity learning and defensive security testing.
