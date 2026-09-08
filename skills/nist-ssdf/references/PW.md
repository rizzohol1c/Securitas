# PW — Produce Well-Secured Software

Fonte: NIST SP 800-218 (SSDF v1.1), tabela oficial de práticas (domínio público — publicação do governo dos EUA).

## PW.1 — Design Software to Meet Security Requirements and Mitigate Security Risks

Identify and evaluate the security requirements for the software; determine what security risks the software is likely to face during operation and how the software’s design and architecture should mitigate those risks; and justify any cases where risk-based analysis indicates that security requirements should be relaxed or waived. Addressing security requirements and risks during software design (secure by design) is key for improving software security and also helps improve development efficiency.

| Task | Descrição |
|---|---|
| PW.1.1 | Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software. |
| PW.1.2 | Track and maintain the software’s security requirements, risks, and design decisions. |
| PW.1.3 | Where appropriate, build in support for using standardized security features and services (e.g., enabling software to integrate with existing log management, identity management, access control, and vulnerability management systems) instead of creating proprietary implementations of security features and services. [Formerly PW.4.3] |

## PW.2 — Review the Software Design to Verify Compliance with Security Requirements and Risk Information

Help ensure that the software will meet the security requirements and satisfactorily address the identified risk information.

| Task | Descrição |
|---|---|
| PW.2.1 | Have 1) a qualified person (or people) who were not involved with the design and/or 2) automated processes instantiated in the toolchain review the software design to confirm and enforce that it meets all of the security requirements and satisfactorily addresses the identified risk information. |

## PW.4 — Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality

Lower the costs of software development, expedite software development, and decrease the likelihood of introducing additional security vulnerabilities into the software by reusing software modules and services that have already had their security posture checked. This is particularly important for software that implements security functionality, such as cryptographic modules and protocols.

| Task | Descrição |
|---|---|
| PW.4.1 | Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open-source, and other third-party developers for use by the organization’s software. |
| PW.4.2 | Create and maintain well-secured software components in-house following SDLC processes to meet common internal software development needs that cannot be better met by third-party software components. |
| PW.4.4 | Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements, as defined by the organization, throughout their life cycles. |

## PW.5 — Create Source Code by Adhering to Secure Coding Practices

Decrease the number of security vulnerabilities in the software, and reduce costs by minimizing vulnerabilities introduced during source code creation that meet or exceed organization-defined vulnerability severity criteria.

| Task | Descrição |
|---|---|
| PW.5.1 | Follow all secure coding practices that are appropriate to the development languages and environment to meet the organization’s requirements. |

## PW.6 — Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security

Decrease the number of security vulnerabilities in the software and reduce costs by eliminating vulnerabilities before testing occurs.

| Task | Descrição |
|---|---|
| PW.6.1 | Use compiler, interpreter, and build tools that offer features to improve executable security. |
| PW.6.2 | Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved configurations. |

## PW.7 — Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements

Help identify vulnerabilities so that they can be corrected before the software is released to prevent exploitation. Using automated methods lowers the effort and resources needed to detect vulnerabilities. Human-readable code includes source code, scripts, and any other form of code that an organization deems human-readable.

| Task | Descrição |
|---|---|
| PW.7.1 | Determine whether code review (a person looks directly at the code to find issues) and/or code analysis (tools are used to find issues in code, either in a fully automated way or in conjunction with a person) should be used, as defined by the organization. |
| PW.7.2 | Perform the code review and/or code analysis based on the organization’s secure coding standards, and record and triage all discovered issues and recommended remediations in the development team’s workflow or issue tracking system. |

## PW.8 — Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements

Help identify vulnerabilities so that they can be corrected before the software is released in order to prevent exploitation. Using automated methods lowers the effort and resources needed to detect vulnerabilities and improves traceability and repeatability. Executable code includes binaries, directly executed bytecode and source code, and any other form of code that an organization deems executable.

| Task | Descrição |
|---|---|
| PW.8.1 | Determine whether executable code testing should be performed to find vulnerabilities not identified by previous reviews, analysis, or testing and, if so, which types of testing should be used. |
| PW.8.2 | Scope the testing, design the tests, perform the testing, and document the results, including recording and triaging all discovered issues and recommended remediations in the development team’s workflow or issue tracking system. |

## PW.9 — Configure Software to Have Secure Settings by Default

Help improve the security of the software at the time of installation to reduce the likelihood of the software being deployed with weak security settings, putting it at greater risk of compromise.

| Task | Descrição |
|---|---|
| PW.9.1 | Define a secure baseline by determining how to configure each setting that has an effect on security or a security-related setting so that the default settings are secure and do not weaken the security functions provided by the platform, network infrastructure, or services. |
| PW.9.2 | Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators. |
