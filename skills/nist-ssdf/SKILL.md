---
name: nist-ssdf
description: Use when designing or reviewing a development *process* rather than a single piece of code — deciding when in the lifecycle security practices belong (before coding, during build, before release, after deploy), setting up a secure SDLC, or building/using AI models where extra practices for training data, model artifacts, and drift monitoring apply (NIST SP 800-218 Secure Software Development Framework + SP 800-218A generative AI profile).
license: Public Domain (US Government Work)
metadata:
  type: framework-mirror
  domain: ci-cd-deploy
  nist_ssdf: PO-PS-PW-RV
  source: https://csrc.nist.gov/projects/ssdf
  upstream_version: "SP800-218v1.1+SP800-218A"
---

# NIST SSDF (Secure Software Development Framework)

## Overview

Unlike OWASP's risk lists (what can go wrong in the app), the SSDF is a
**process framework**: 42 practices across 4 groups that say *when* in
the software development lifecycle a security practice belongs, not what
technical control to apply. SP 800-218A extends it with practices
specific to building with or on generative AI / foundation models.

## When to use

- Designing or auditing a team's secure development process (not a single
  code review)
- Deciding at what point in a project's lifecycle a security practice
  should be introduced
- Building a product that trains, fine-tunes, or wraps a generative AI
  model — need practices for training data integrity, model artifact
  protection, or behavior-drift monitoring
- Setting up compliance/attestation for secure software development
  (e.g. US federal software attestation)

## Quick reference — the 4 practice groups

| Group | Name | Question it answers | Reference |
|---|---|---|---|
| **PO** | Prepare the Organization | Are people, process, and tooling ready to develop securely? | [references/PO.md](references/PO.md) |
| **PS** | Protect the Software | Is source code and build output protected from tampering? | [references/PS.md](references/PS.md) |
| **PW** | Produce Well-Secured Software | Was the software designed, coded, and tested to minimize vulnerability? | [references/PW.md](references/PW.md) |
| **RV** | Respond to Vulnerabilities | Are post-release vulnerabilities identified and fixed? | [references/RV.md](references/RV.md) |

Each reference file lists that group's practices (e.g. `PO.1`) and their
tasks (e.g. `PO.1.1`, `PO.1.2`) with the official task description.

Generative-AI-specific additions (SP 800-218A) are summarized per group in
[references/GenAI-profile.md](references/GenAI-profile.md) — a high-level
summary, not a verbatim mirror; see that file for the full-text source.

## How to use

1. Walk the 4 groups in order (PO → PS → PW → RV) against the project's
   actual workflow — most teams over-invest in PW (writing code) and
   under-invest in PO (readiness) and RV (post-release response).
2. Pull the specific tasks relevant to the gap found.
3. If the product involves a generative AI model (own or third-party API),
   check `GenAI-profile.md` for the practices that apply beyond standard
   software.
4. Cross-reference with `owasp-top10-web` / `owasp-llm-top10` for *what*
   to check, and `owasp-asvs` for testable acceptance criteria.

## Source

Practice/task text sourced from the official NIST SP 800-218 (SSDF v1.1)
table — a US government work in the public domain. GenAI profile summary
sourced from NIST SP 800-218A metadata; full text at
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf>.
Not maintained in sync; re-check upstream for updates.
