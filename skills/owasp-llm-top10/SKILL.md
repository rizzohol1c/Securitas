---
name: owasp-llm-top10
description: Use when designing, building, reviewing, or threat-modeling an LLM/GenAI application, agent, RAG pipeline, or prompt — covers prompt injection, sensitive information disclosure, supply chain risk, data/model poisoning, improper output handling, excessive agency, system prompt leakage, vector/embedding weaknesses, misinformation, and unbounded consumption/DoS, with mitigations and attack scenarios per risk (OWASP Top 10 for LLM Applications, 2025 v2.0).
license: CC-BY-SA-4.0
metadata:
  type: framework-mirror
  domain: seguranca-llm-ia
  owasp_llm_top10: LLM01-LLM10
  source: https://github.com/OWASP/www-project-top-10-for-large-language-model-applications
  upstream_version: "2025-v2.0"
---

# OWASP Top 10 for LLM Applications (2025)

## Overview

Security checklist for LLM-based applications, agents, and RAG systems. Each risk has its own reference file with: description, subtypes, prevention/mitigation strategies, example attack scenarios, and citations.

## When to use

- Reviewing code/architecture for an LLM app, agent, chatbot, or RAG pipeline
- Writing or reviewing a system prompt, tool/function definition, or agent permission scheme
- Threat-modeling a GenAI feature before or during implementation
- Investigating an incident involving unexpected LLM output or behavior

## Quick reference

| ID | Risk | Reference |
|----|------|-----------|
| LLM01 | **Prompt Injection** — crafted input (direct or indirect, via tool/RAG content) overrides intended model behavior | [references/LLM01_PromptInjection.md](references/LLM01_PromptInjection.md) |
| LLM02 | **Sensitive Information Disclosure** — PII, credentials, or proprietary data leak via prompts, training data, or output | [references/LLM02_SensitiveInformationDisclosure.md](references/LLM02_SensitiveInformationDisclosure.md) |
| LLM03 | **Supply Chain** — compromised training data, pre-trained models, LoRA adapters, or deployment platforms | [references/LLM03_SupplyChain.md](references/LLM03_SupplyChain.md) |
| LLM04 | **Data and Model Poisoning** — manipulated training/fine-tuning/embedding data introduces backdoors or bias | [references/LLM04_DataModelPoisoning.md](references/LLM04_DataModelPoisoning.md) |
| LLM05 | **Improper Output Handling** — unsanitized LLM output passed to shells, DBs, browsers (XSS/SSRF/RCE-style downstream risk) | [references/LLM05_ImproperOutputHandling.md](references/LLM05_ImproperOutputHandling.md) |
| LLM06 | **Excessive Agency** — over-broad tool permissions, functionality, or autonomy let the model take unintended actions | [references/LLM06_ExcessiveAgency.md](references/LLM06_ExcessiveAgency.md) |
| LLM07 | **System Prompt Leakage** — system prompt discloses secrets it shouldn't rely on staying hidden | [references/LLM07_SystemPromptLeakage.md](references/LLM07_SystemPromptLeakage.md) |
| LLM08 | **Vector and Embedding Weaknesses** — RAG-specific: injection via retrieved content, embedding inversion, access-control gaps | [references/LLM08_VectorAndEmbeddingWeaknesses.md](references/LLM08_VectorAndEmbeddingWeaknesses.md) |
| LLM09 | **Misinformation** — confident but false/misleading output (hallucination) relied on downstream | [references/LLM09_Misinformation.md](references/LLM09_Misinformation.md) |
| LLM10 | **Unbounded Consumption** — uncontrolled inference volume/cost/resource use (denial of wallet/service) | [references/LLM10_UnboundedConsumption.md](references/LLM10_UnboundedConsumption.md) |

## How to use

1. Scan the table for risks relevant to the feature at hand (a RAG feature → LLM01, LLM08; an agent with tools → LLM01, LLM06; anything handling user data → LLM02).
2. Open the matching reference file for concrete mitigations and attack scenarios to check against.
3. Apply the "Prevention and Mitigation Strategies" section as a checklist during design/review.

## Source

Mirrored from [OWASP/www-project-top-10-for-large-language-model-applications](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications), 2_0_vulns/. Licensed CC BY-SA 4.0 — see [references/LICENSE.md](references/LICENSE.md). Not maintained in sync; re-pull from upstream for updates.
