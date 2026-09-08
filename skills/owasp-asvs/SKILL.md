---
name: owasp-asvs
description: Use when turning "be secure" into checkable, testable security requirements for a web application or API — writing acceptance criteria, a pre-deploy checklist, a pentest/verification scope, or reviewing AI-generated code against a concrete standard instead of a vague risk list (OWASP Application Security Verification Standard 5.0.0).
license: CC-BY-SA-4.0
metadata:
  type: framework-mirror
  domain: checklists-templates
  owasp_asvs: V1-V17
  source: https://github.com/OWASP/ASVS
  upstream_version: "5.0.0"
---

# OWASP ASVS (Application Security Verification Standard) 5.0.0

## Overview

Unlike the Top 10 (a risk-awareness list), ASVS is a list of ~346
**verifiable requirements** — each one a testable "the system verifies
that X" / "the system rejects Y" statement, organized into 17 chapters
and 3 verification levels. It's the tool for turning a security concern
into something you can mark ✅ or ❌.

## When to use

- Defining acceptance criteria or a pre-deploy security checklist for a
  web app/API
- Reviewing AI-generated code against concrete, testable requirements
  instead of a vague "looks secure" impression
- Scoping a pentest or internal security review
- Deciding how much rigor a given app needs (L1 vs L2 vs L3)

## Verification levels

| Level | Purpose | Application profile |
|---|---|---|
| **L1** | Minimum viable security, verifiable even by automated testing | Any internet-facing application — non-negotiable floor |
| **L2** | Recommended standard for most applications | Apps handling user data, payment, sensitive business data |
| **L3** | High rigor, requires in-depth manual review | Critical apps: financial, healthcare, highly regulated data |

For a typical SaaS: **L1 before any production deploy**, **L2 as the
target** as the product matures.

## Quick reference — the 17 chapters

| ID | Chapter | Reference |
|---|---|---|
| V1 | Encoding and Sanitization | [references/V1.md](references/V1.md) |
| V2 | Validation and Business Logic | [references/V2.md](references/V2.md) |
| V3 | Web Frontend Security | [references/V3.md](references/V3.md) |
| V4 | API and Web Service | [references/V4.md](references/V4.md) |
| V5 | File Handling | [references/V5.md](references/V5.md) |
| V6 | Authentication | [references/V6.md](references/V6.md) |
| V7 | Session Management | [references/V7.md](references/V7.md) |
| V8 | Authorization | [references/V8.md](references/V8.md) |
| V9 | Self-contained Tokens | [references/V9.md](references/V9.md) |
| V10 | OAuth and OIDC | [references/V10.md](references/V10.md) |
| V11 | Cryptography | [references/V11.md](references/V11.md) |
| V12 | Secure Communication | [references/V12.md](references/V12.md) |
| V13 | Configuration | [references/V13.md](references/V13.md) |
| V14 | Data Protection | [references/V14.md](references/V14.md) |
| V15 | Secure Coding and Architecture | [references/V15.md](references/V15.md) |
| V16 | Security Logging and Error Handling | [references/V16.md](references/V16.md) |
| V17 | WebRTC | [references/V17.md](references/V17.md) |

Each reference file lists that chapter's requirements as a table:
`req_id | L (level) | requirement text`, grouped by section.

## How to use

1. Pick the target level (L1 floor, L2 for most SaaS, L3 for
   critical/regulated apps).
2. Open the chapter(s) relevant to the feature under review (e.g. a login
   flow → V6 Authentication + V7 Session Management).
3. Filter rows by `L` ≤ target level and use them as a literal checklist.
4. Cross-reference with `owasp-top10-web` for *why* a category matters and
   `nist-ssdf` for *when* in the lifecycle to check it.

## Source

Mirrored from the official CSV in
[OWASP/ASVS](https://github.com/OWASP/ASVS), `5.0/docs_en/`.
Licensed CC BY-SA 4.0 — see [references/LICENSE.md](references/LICENSE.md).
Not maintained in sync; re-pull from upstream for updates (a new ASVS
version or errata may renumber/adjust requirements).
