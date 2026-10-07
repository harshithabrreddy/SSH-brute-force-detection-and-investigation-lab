# MITRE ATT&CK Mapping

## Detection
SSH Brute-Force / Password Guessing

## MITRE ATT&CK

- Tactic: Credential Access
- Technique: T1110 - Brute Force
- Sub-technique: T1110.001 - Password Guessing

## Observed Behavior

Multiple failed SSH authentication attempts were observed
against the same user account from the same source IP.

## Evidence

Source IP: 127.0.0.1
Target User: harshithabr
Failed Attempts: 6
Time Window: 53 seconds

## Detection Rule

5 or more failed SSH authentication attempts
from the same source IP within 60 seconds.

## Investigation Result

No successful SSH login was identified during the
investigation.

The activity was intentionally generated as part of
a controlled cybersecurity lab.

## Conclusion

The detection rule successfully identified behavior
consistent with password guessing / brute-force activity.
The event was benign because it was generated during
authorized testing.
