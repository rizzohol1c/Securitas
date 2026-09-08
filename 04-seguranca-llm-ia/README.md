# 04-seguranca-llm-ia

Prompt injection, OWASP LLM Top 10, excessive agency de agentes de IA,
vazamento de system prompt.

Desdobramento direto do
[OWASP Top 10 for LLM Applications](../00-frameworks-base/02-owasp-llm-top10.md)
(2025 v2.0). Cada risco (LLM01–LLM10) vai virar um arquivo aqui com
mitigação e exemplo de ataque aplicado a SaaS vibe-coded.

## Skills instaláveis relacionadas

- [`excessive-agent-permissions`](../skills/excessive-agent-permissions/SKILL.md) — agente com tool destrutiva sem confirmação ou checagem de permissão (LLM06)

## Índice planejado

- [ ] LLM01 — Prompt Injection
- [ ] LLM02 — Sensitive Information Disclosure
- [ ] LLM03 — Supply Chain
- [ ] LLM04 — Data and Model Poisoning
- [ ] LLM05 — Improper Output Handling
- [x] LLM06 — Excessive Agency (`excessive-agent-permissions`)
- [ ] LLM07 — System Prompt Leakage
- [ ] LLM08 — Vector and Embedding Weaknesses
- [ ] LLM09 — Misinformation
- [ ] LLM10 — Unbounded Consumption
