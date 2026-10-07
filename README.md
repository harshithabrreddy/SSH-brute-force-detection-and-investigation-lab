# SSH Brute-Force Detection and Investigation

## Project Overview

This project demonstrates a SOC workflow for detecting, investigating, and documenting SSH brute-force activity using Linux authentication logs and Python.

##Project Roadmap 
<img width="984" height="1060" alt="Project Roadmap" src="https://github.com/user-attachments/assets/6d489c29-e574-40e1-966a-c333aaeb1d20" />


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

<img width="989" height="1287" alt="03-soc-alert" src="https://github.com/user-attachments/assets/fa07b186-19f4-4a79-807c-c0b0fd3f6880" />


The alert was investigated by reviewing SSH authentication logs and checking for successful authentication events.

No successful SSH login was identified during the investigation.

The activity was intentionally generated as part of a controlled cybersecurity lab.

Final Classification: BENIGN / AUTHORIZED LAB ACTIVITY

## MITRE ATT&CK Mapping

<img width="1349" height="1600" alt="04-mitre-mapping" src="https://github.com/user-attachments/assets/32d0ea8c-2b3a-4901-94d4-3dc85f359473" />


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

## Project Screenshots

### 1. SSH Failed Login Evidence

![SSH Failed Login Evidence]
<img width="1600" height="841" alt="01-ssh-failed-login" src="https://github.com/user-attachments/assets/38b5458f-218e-4fc7-92ee-76f90b8cd653" />


Multiple failed SSH authentication attempts were recorded in `/var/log/auth.log`.

### 2. Brute-Force Detection

![Brute-Force Detection]
<img width="1496" height="1600" alt="02-brute-force-detection" src="https://github.com/user-attachments/assets/a7808ceb-bfaf-4892-aa9b-b7eca7508623" />


The Python detector identified 6 failed login attempts from the same source IP within 53 seconds and generated a HIGH severity alert.

### 3. SOC Alert

![SOC Alert]
<img width="989" height="1287" alt="03-soc-alert" src="https://github.com/user-attachments/assets/6439073e-bbfe-4bee-a8bd-cb0fc6014b39" />


The generated alert contains the source IP, target username, failed attempts, severity, and detection rule.

### 4. MITRE ATT&CK Mapping

![MITRE ATT&CK Mapping]
<img width="1349" height="1600" alt="04-mitre-mapping" src="https://github.com/user-attachments/assets/676f8b43-589e-44f8-ada7-e1bcf934df76" />


The detected behavior was mapped to MITRE ATT&CK T1110.001 Password Guessing.

### 5. Incident Report

![Incident Report]
<img width="1294" height="1600" alt="05-incident-report" src="https://github.com/user-attachments/assets/3c7b187e-d55a-4e78-97d1-a081a9a14e35" />


The incident report documents the investigation, evidence, classification, and response.

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
