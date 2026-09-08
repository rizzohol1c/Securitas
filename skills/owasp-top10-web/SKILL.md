---
name: owasp-top10-web
description: Use when designing, building, reviewing, or threat-modeling any web application or API — covers broken access control, security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software/data integrity failures, logging/alerting failures, and mishandling of exceptional conditions, with background, CWE mappings, and prevention guidance per category (OWASP Top 10:2025).
license: CC-BY-SA-4.0
metadata:
  type: framework-mirror
  domain: fundamentos
  owasp_top10: A01-A10
  source: https://github.com/OWASP/Top10
  upstream_version: "2025"
---

# OWASP Top 10 (Web Applications, 2025)

## Overview

The most widely used web application security awareness list, based on
analysis of 175,000+ CVEs and practitioner surveys. Each category has its
own reference file mirrored from the official OWASP document: background,
score/incidence data, description, how to prevent, example attack
scenarios, and references.

## When to use

- Reviewing code/architecture for a web app, API, or backend service
- Threat-modeling a feature before or during implementation
- Doing a general security pass on an application (not LLM-specific — see
  `owasp-llm-top10` for that)
- Investigating an incident or vulnerability report to classify its root
  cause

## Quick reference

| ID | Risk | Reference |
|----|------|-----------|
| A01 | **Broken Access Control** — users act outside intended permissions (includes SSRF, absorbed here in 2025) | [references/A01.md](references/A01.md) |
| A02 | **Security Misconfiguration** — insecure defaults, open CORS, debug mode in prod, wrong storage/bucket permissions | [references/A02.md](references/A02.md) |
| A03 | **Software Supply Chain Failures** — compromise in the build/distribution/update pipeline (new in 2025) | [references/A03.md](references/A03.md) |
| A04 | **Cryptographic Failures** — sensitive data exposed due to weak/missing crypto in transit or at rest | [references/A04.md](references/A04.md) |
| A05 | **Injection** — SQL/NoSQL/OS command/XSS: untrusted input interpreted as code | [references/A05.md](references/A05.md) |
| A06 | **Insecure Design** — structural/architectural flaw, not an implementation bug | [references/A06.md](references/A06.md) |
| A07 | **Authentication Failures** — weak login, session, or credential-recovery implementation | [references/A07.md](references/A07.md) |
| A08 | **Software or Data Integrity Failures** — trusting updates/plugins/data without verifying integrity | [references/A08.md](references/A08.md) |
| A09 | **Security Logging and Alerting Failures** — insufficient logging/alerting to detect and respond in time | [references/A09.md](references/A09.md) |
| A10 | **Mishandling of Exceptional Conditions** — errors/exceptions handled in a way that leaks data or breaks security logic (new in 2025) | [references/A10.md](references/A10.md) |

## How to use

1. Scan the table for risks relevant to the code/feature at hand.
2. Open the matching reference file for background, CWE mapping, and
   concrete prevention guidance.
3. Apply the "How to Prevent" section as a checklist during design/review.
4. For requirement-level, testable criteria (not just awareness), cross
   the relevant category with `owasp-asvs`.

## Source

Mirrored from [OWASP/Top10](https://github.com/OWASP/Top10), `2025/docs/en/`.
Licensed CC BY-SA 4.0 — see [references/LICENSE.md](references/LICENSE.md).
Not maintained in sync; re-pull from upstream for updates.
