# Extended: E-Webhook - HMAC delivery

**Status:** implemented (static + unit smoke)
**Sub-module:** E-Webhook
**Requirements:** ODTIS-0531, ODTIS-0358 (draft)
**Profile:** extended

## Procedure

1. Register webhook URL and HMAC secret for `verification.completed`.
2. Trigger event; verify outbound POST includes valid HMAC signature header.
3. Reject tampered payload at receiver.

## Pass criteria

Unsigned or invalid HMAC payloads fail verification; delivery logged on failure.
