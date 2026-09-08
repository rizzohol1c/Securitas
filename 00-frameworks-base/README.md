# 00 · Frameworks de base

Esta pasta é o alicerce do repositório: quatro frameworks/padrões da
indústria que dão estrutura a tudo que vou documentar nas pastas `01` a
`10`. Cada um responde a uma pergunta diferente — juntos cobrem o ciclo
completo de "o que pode dar errado" até "como provar que não deu".

| Framework | Pergunta que responde | Quando entra em jogo |
|---|---|---|
| [OWASP Top 10](01-owasp-top10-web.md) | Quais falhas clássicas de app web mais aparecem em produção? | Revisão de código e arquitetura da aplicação |
| [OWASP Top 10 for LLM Applications](02-owasp-llm-top10.md) | O que quebra especificamente por ter um LLM/agente no meio? | Qualquer feature com IA, agente, RAG ou geração de output |
| [OWASP ASVS](03-owasp-asvs.md) | Como transformar "seja seguro" em requisitos verificáveis? | Definir critério de aceite / checklist de verificação |
| [NIST SSDF (+ perfil GenAI)](04-nist-ssdf.md) | Em que ponto do processo de desenvolvimento cada prática entra? | Desenho do fluxo de trabalho, não só o código final |

## Onde vive o quê

Para não republicar conteúdo que a OWASP e o NIST já mantêm (e ficar
desatualizado), o texto oficial de cada framework vive como uma **skill
instalável** em [`skills/`](../skills/README.md), não repetido nesta
pasta:

| Framework | Skill | Conteúdo espelhado |
|---|---|---|
| OWASP Top 10 (web) | [`owasp-top10-web`](../skills/owasp-top10-web/SKILL.md) | A01–A10 completos (background, CWEs, prevenção, ataques) |
| OWASP LLM Top 10 | [`owasp-llm-top10`](../skills/owasp-llm-top10/SKILL.md) | LLM01–LLM10 completos (mitigação, cenário de ataque) |
| OWASP ASVS | [`owasp-asvs`](../skills/owasp-asvs/SKILL.md) | 346 requisitos oficiais, por capítulo V1–V17, com nível L1/L2/L3 |
| NIST SSDF (+ GenAI) | [`nist-ssdf`](../skills/nist-ssdf/SKILL.md) | 42 práticas oficiais (PO/PS/PW/RV) + resumo do perfil GenAI |

Os arquivos desta pasta (`01`–`04`) são o resumo, o "porquê para vibe
coding" e o link para a skill correspondente — não uma cópia do conteúdo
integral. Para o texto oficial: peça para um agente invocar a skill (ex.:
"use a skill owasp-asvs para checar V8"), ou leia direto em
`skills/<nome>/references/` no repo. Ver [`ARCHITECTURE.md`](../ARCHITECTURE.md)
para como essas skills são categorizadas, validadas e mantidas em dia com
a fonte oficial.

## Como os quatro se encaixam

```
NIST SSDF          → define QUANDO no ciclo de vida (planejar, construir, revisar, responder)
  └─ OWASP Top 10     → aponta O QUE pode estar errado na aplicação
  └─ OWASP LLM Top 10 → aponta O QUE pode estar errado por causa da IA
       └─ OWASP ASVS    → transforma os dois de cima em requisitos
                            verificáveis, com nível de rigor (L1/L2/L3)
```

Na prática, para vibe coding: o SSDF me diz *quando* parar para revisar
segurança (não só no final); o Top 10 web e o LLM Top 10 me dizem *o que*
procurar nessa revisão; o ASVS me dá a *régua* para saber se o requisito
foi realmente atendido, não só "parece bom".

## Como isso alimenta o resto do repositório

- `01-fundamentos/` parte do OWASP Top 10 e do modelo de processo do SSDF.
- `02` a `09` (temas específicos: auth, segredos, IA, infra, dados, CI/CD,
  monitoramento) detalham controles que o ASVS pede e que o SSDF posiciona
  no ciclo de vida.
- `04-seguranca-llm-ia/` é o desdobramento direto do OWASP LLM Top 10.
- `10-checklists-templates/` traduz itens do ASVS (nível L1/L2) e das
  práticas do SSDF em checklists prontos para usar antes de um deploy.

## Fontes oficiais

- OWASP Top 10:2025 — <https://owasp.org/Top10/2025/>
- OWASP Top 10 for LLM Applications 2025 (v2.0) — <https://genai.owasp.org/>
- OWASP ASVS 5.0 — <https://owasp.org/www-project-application-security-verification-standard/>
- NIST SP 800-218 (SSDF v1.1) — <https://csrc.nist.gov/projects/ssdf>
- NIST SP 800-218A (perfil GenAI/foundation models do SSDF) — <https://csrc.nist.gov/pubs/sp/800/218/a/final>
