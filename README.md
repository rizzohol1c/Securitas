# Segurança para SaaS com IA e Vibe Coding

Repositório de boas práticas de segurança para quem constrói produtos SaaS
usando ferramentas de IA (Claude Code, Cursor, Copilot, v0, etc.) e o
fluxo de "vibe coding" — onde grande parte do código é gerado por IA em
ciclos rápidos de iteração.

## Por que este repositório existe

Vibe coding acelera a criação de produtos, mas também acelera a criação de
vulnerabilidades: segredos commitados sem querer, permissões abertas demais
no banco, dependências aceitas sem revisão, prompts vulneráveis a injeção.
A IA que gera o código raramente pensa em segurança por padrão — quem
precisa pensar é quem revisa.

Este repositório é meu registro de estudos como iniciante em
cibersegurança: cada pasta numerada (`01`–`10`) é um **tema** que estou
documentando à medida que aprendo, com foco prático em SaaS construídos
com apoio de IA. Dentro desses temas, tanto os frameworks de base quanto
os padrões de vulnerabilidade mais recorrentes viram **skills
instaláveis de verdade** em [`skills/`](skills/README.md) — arquivos
`SKILL.md` no formato aberto [Agent Skills](https://agentskills.io/specification),
que qualquer agente de IA compatível (Claude Code, Codex, Copilot CLI,
Gemini CLI, etc.) consegue instalar e usar nativamente, não só ler como
documentação.

Como tudo isso se encaixa — estrutura, taxonomia das skills, formato do
`SKILL.md`, metodologia de validação — está documentado em
[`ARCHITECTURE.md`](ARCHITECTURE.md).

## Objetivos

- Documentar boas práticas de segurança organizadas por tema (skill),
  priorizando os riscos mais comuns em produtos vibe-coded.
- Criar checklists aplicáveis antes de colocar um SaaS em produção.
- Registrar exemplos reais (sanitizados) de vulnerabilidades encontradas e
  como foram corrigidas.
- Servir de referência rápida para revisar código gerado por IA antes de
  aceitar (fluxo "generate → review → harden").

## Frameworks de base

Todo o conteúdo parte de quatro frameworks reconhecidos da indústria,
documentados em [`00-frameworks-base/`](00-frameworks-base/README.md) e
espelhados como skill em `skills/` (conteúdo oficial completo, atualizado
por script — ver `ARCHITECTURE.md`):

- **OWASP Top 10** — vulnerabilidades clássicas de aplicação web.
- **OWASP Top 10 for LLM Applications** (2025) — riscos específicos de IA:
  prompt injection, improper output handling, excessive agency etc.
- **OWASP ASVS** — transforma os dois acima em requisitos verificáveis,
  com nível de rigor (L1/L2/L3).
- **NIST SSDF** (+ perfil para IA generativa, SP 800-218A) — posiciona
  cada prática no ciclo de vida do desenvolvimento, não só como auditoria
  no final.

## Estrutura de pastas

```
.
├── 00-frameworks-base/          # doc: os 4 frameworks acima, resumo + link pra skill
├── 01-fundamentos/              # doc: conceitos base: CIA triad, threat modeling, OWASP Top 10
├── 02-autenticacao-autorizacao/ # doc: login, sessão, RBAC, RLS (Supabase/Postgres), JWT
├── 03-gestao-de-segredos/       # doc: API keys, .env, secret managers, rotação
├── 04-seguranca-llm-ia/         # doc: prompt injection, OWASP LLM Top 10, excessive agency de agentes
├── 05-dependencias-supply-chain/# doc: pacotes de terceiros, código gerado por IA, SBOM
├── 06-infraestrutura-cloud/     # doc: deploy, redes, buckets, permissões de nuvem
├── 07-dados-e-privacidade/      # doc: LGPD/GDPR, criptografia, minimização de dados
├── 08-ci-cd-deploy/             # doc: pipelines, secrets em CI, revisão antes de merge
├── 09-monitoramento-resposta/   # doc: logging, alertas, plano de resposta a incidentes
├── 10-checklists-templates/     # doc: checklists prontos para usar, derivados do ASVS
├── skills/                      # PRODUTO: skills instaláveis (Agent Skills spec) — 4 framework-mirror + 10 vulnerability-pattern
├── scripts/                     # regenera skills framework-mirror da fonte oficial + valida schema
├── .github/workflows/           # CI: validação de schema + checagem semanal de frescor
├── ARCHITECTURE.md              # como tudo isso se encaixa
├── LICENSE                      # MIT
└── README.md
```

Cada pasta temática terá seu próprio `README.md` com o índice do conteúdo,
e vai crescendo conforme eu estudo o tema. As skills em `skills/` são o
formato "pronto para usar" desse conteúdo — ver [`skills/README.md`](skills/README.md)
para a lista completa e como instalar, ou [`ARCHITECTURE.md`](ARCHITECTURE.md)
para o desenho completo.

## Como uso este repositório

1. Antes de colocar um SaaS novo em produção, passo pelos checklists em
   `10-checklists-templates/`.
2. Ao revisar código gerado por IA, confiro os temas relevantes nas pastas
   `02` a `06` antes de aceitar o PR/commit.
3. Vulnerabilidades reais encontradas (sem dados sensíveis do cliente) viram
   estudo de caso na skill correspondente.

## Status

🟡 Em construção — começando os estudos. Estrutura criada, conteúdo sendo
preenchido pasta por pasta.
