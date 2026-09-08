# PS — Protect the Software

Fonte: NIST SP 800-218 (SSDF v1.1), tabela oficial de práticas (domínio público — publicação do governo dos EUA).

## PS.1 — Protect All Forms of Code from Unauthorized Access and Tampering

Help prevent unauthorized changes to code, both inadvertent and intentional, which could circumvent or negate the intended security characteristics of the software. For code that is not intended to be publicly accessible, this helps prevent theft of the software and may make it more difficult or time-consuming for attackers to find vulnerabilities in the software.

| Task | Descrição |
|---|---|
| PS.1.1 | Store all forms of code – including source code, executable code, and configuration-as-code – based on the principle of least privilege so that only authorized personnel, tools, services, etc. have access. |

## PS.2 — Provide a Mechanism for Verifying Software Release Integrity

Help software acquirers ensure that the software they acquire is legitimate and has not been tampered with.

| Task | Descrição |
|---|---|
| PS.2.1 | Make software integrity verification information available to software acquirers. |

## PS.3 — Archive and Protect Each Software Release

Preserve software releases in order to help identify, analyze, and eliminate vulnerabilities discovered in the software after release.

| Task | Descrição |
|---|---|
| PS.3.1 | Securely archive the necessary files and supporting data (e.g., integrity verification information, provenance data) to be retained for each software release. |
| PS.3.2 | Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials [SBOM]). |
