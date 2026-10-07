# Incident Report - SSH Brute-Force Detection

## 1. Incident Summary

A high-severity SSH authentication alert was generated
after multiple failed login attempts were detected from
the same source IP within a short time period.

## 2. Alert Details

Alert ID: SSH-001
Alert Type: SSH Brute-Force
Severity: HIGH
Status: CLOSED - Benign Lab Activity

## 3. Source Information

Source IP: 127.0.0.1
Target Username: harshithabr
Failed Attempts: 6

## 4. Timeline

Start Time: 2026-10-07 06:42:31
End Time: 2026-10-07 06:43:24
Duration: 53 seconds

## 5. Detection Rule

Trigger an alert when 5 or more failed SSH
authentication attempts occur from the same
source IP within 60 seconds.

## 6. Investigation

SSH authentication logs were reviewed to identify
the source IP, targeted username, number of failed
attempts, and authentication result.

No successful SSH login was identified by the
successful-login search.

## 7. MITRE ATT&CK Mapping

Tactic: Credential Access
Technique: T1110 - Brute Force
Sub-technique: T1110.001 - Password Guessing

## 8. Impact

No compromise was identified.

The source IP was 127.0.0.1 because the activity
was generated locally in the controlled lab.

## 9. Root Cause

The failed authentication attempts were intentionally
generated to test the SSH brute-force detection rule.

## 10. Response

The alert was investigated and classified as
benign authorized testing activity.

No containment action was required.

## 11. Recommendations

- Monitor repeated SSH authentication failures.
- Use strong passwords.
- Prefer SSH key-based authentication.
- Restrict SSH access where possible.
- Monitor authentication logs continuously.
- Investigate repeated failures from external IP addresses.

## 12. Final Classification

Classification: BENIGN / AUTHORIZED LAB ACTIVITY

Detection Result: SUCCESSFUL
Investigation Result: NO COMPROMISE IDENTIFIED
