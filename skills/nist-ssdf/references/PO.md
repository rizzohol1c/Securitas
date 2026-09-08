# PO — Prepare the Organization

Fonte: NIST SP 800-218 (SSDF v1.1), tabela oficial de práticas (domínio público — publicação do governo dos EUA).

## PO.1 — Define Security Requirements for Software Development

Ensure that security requirements for software development are known at all times so that they can be taken into account throughout the SDLC and duplication of effort can be minimized because the requirements information can be collected once and shared. This includes requirements from internal sources (e.g., the organization’s policies, business objectives, and risk management strategy) and external sources (e.g., applicable laws and regulations).

| Task | Descrição |
|---|---|
| PO.1.1 | Identify and document all security requirements for the organization’s software development infrastructures and processes, and maintain the requirements over time. |
| PO.1.2 | Identify and document all security requirements for organization-developed software to meet, and maintain the requirements over time. |
| PO.1.3 | Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization’s own software. [Formerly PW.3.1] |

## PO.2 — Implement Roles and Responsibilities

Ensure that everyone inside and outside of the organization involved in the SDLC is prepared to perform their SDLC-related roles and responsibilities throughout the SDLC.

| Task | Descrição |
|---|---|
| PO.2.1 | Create new roles and alter responsibilities for existing roles as needed to encompass all parts of the SDLC. Periodically review and maintain the defined roles and responsibilities, updating them as needed. |
| PO.2.2 | Provide role-based training for all personnel with responsibilities that contribute to secure development. Periodically review personnel proficiency and role-based training, and update the training as needed. |
| PO.2.3 | Obtain upper management or authorizing official commitment to secure development, and convey that commitment to all with development-related roles and responsibilities. |

## PO.3 — Implement Supporting Toolchains

Use automation to reduce human effort and improve the accuracy, reproducibility, usability, and comprehensiveness of security practices throughout the SDLC, as well as provide a way to document and demonstrate the use of these practices. Toolchains and tools may be used at different levels of the organization, such as organization-wide or project-specific, and may address a particular part of the SDLC, like a build pipeline.

| Task | Descrição |
|---|---|
| PO.3.1 | Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, as well as how the toolchain components are to be integrated with each other. |
| PO.3.2 | Follow recommended security practices to deploy, operate, and maintain tools and toolchains. |
| PO.3.3 | Configure tools to generate artifacts of their support of secure software development practices as defined by the organization. |

## PO.4 — Define and Use Criteria for Software Security Checks

Help ensure that the software resulting from the SDLC meets the organization’s expectations by defining and using criteria for checking the software’s security during development.

| Task | Descrição |
|---|---|
| PO.4.1 | Define criteria for software security checks and track throughout the SDLC. |
| PO.4.2 | Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria. |

## PO.5 — Implement and Maintain Secure Environments for Software Development

Ensure that all components of the environments for software development are strongly protected from internal and external threats to prevent compromises of the environments or the software being developed or maintained within them. Examples of environments for software development include development, build, test, and distribution environments.

| Task | Descrição |
|---|---|
| PO.5.1 | Separate and protect each environment involved in software development. |
| PO.5.2 | Secure and harden development endpoints (i.e., endpoints for software designers, developers, testers, builders, etc.) to perform development-related tasks using a risk-based approach. |
