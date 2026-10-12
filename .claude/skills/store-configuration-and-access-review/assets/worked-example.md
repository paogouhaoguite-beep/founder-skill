# Synthetic worked example

Synthetic production gateway G1 is enabled, mode attested sandbox, credentials masked. Result: **sandbox on production requires owner review; operational payment capability unverified**. G2 is disabled intentionally for unsupported currency: no automatic enable. Former contractor U1 still has catalog write access with offboarding ticket; propose revoke after checking ownership handoff. U2 has no last-login field: activity unknown, not stale.

| Item | Proposed action | Verification |
|---|---|---|
|G1|prepare owner-approved live-mode change|scoped checkout/payment acceptance|
|U1|offboarding access removal preview|permission readback and recovery owner|

## Boundary case 1

A field called public_key is intentionally public but arbitrary unknown fields may contain secrets. Use field-level allowlist; never dump full settings just because names lack “secret”.

## Boundary case 2

Only active owner account would be removed. Stop and establish approved replacement/recovery access before revocation.
