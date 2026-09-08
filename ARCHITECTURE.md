# Arquitetura do repositório

Este documento descreve como o repositório é organizado, como as skills
são categorizadas, o formato que cada `SKILL.md` segue, e como o
conteúdo é validado — tanto estruturalmente (schema) quanto quanto à
veracidade (conteúdo espelhado de fonte oficial vs. conteúdo original).

## Modelo mental: duas camadas

O repositório tem duas camadas com propósitos diferentes, e é importante
não confundi-las:

| Camada | Pastas | Propósito | Consumidor |
|---|---|---|---|
| **Documentação de estudo** | `00-frameworks-base/`, `01`–`10` | Prosa: o que é cada framework, por que importa em vibe coding, como os temas se relacionam | Humano lendo o repo |
| **Skills instaláveis** | `skills/` | Artefato funcional: `SKILL.md` que um agente de IA carrega e usa em tempo real | Agente de IA (Claude Code, Codex, Copilot CLI, Gemini CLI, etc.) |

A camada de documentação **nunca duplica** o conteúdo integral de um
framework — ela resume e linka para a skill correspondente em `skills/`.
A camada de skills é a fonte única de verdade para conteúdo técnico
detalhado (checklists, requisitos, mitigações).

## Estrutura de pastas

```
.
├── 00-frameworks-base/              # doc: os 4 frameworks de base e como se encaixam
│   ├── README.md
│   ├── 01-owasp-top10-web.md        # resumo + link -> skills/owasp-top10-web
│   ├── 02-owasp-llm-top10.md        # resumo + link -> skills/owasp-llm-top10
│   ├── 03-owasp-asvs.md             # resumo + link -> skills/owasp-asvs
│   └── 04-nist-ssdf.md              # resumo + link -> skills/nist-ssdf
│
├── 01-fundamentos/ … 10-checklists-templates/   # doc: um README por tema, linkando as skills relevantes
│
├── skills/                          # PRODUTO: skills instaláveis (Agent Skills spec)
│   ├── README.md                    # catálogo + instalação
│   ├── owasp-top10-web/             # type: framework-mirror
│   │   ├── SKILL.md
│   │   └── references/A01.md … A10.md, LICENSE.md
│   ├── owasp-llm-top10/             # type: framework-mirror
│   │   └── references/LLM01_*.md … LLM10_*.md, LICENSE.md
│   ├── owasp-asvs/                  # type: framework-mirror
│   │   └── references/V1.md … V17.md, LICENSE.md
│   ├── nist-ssdf/                   # type: framework-mirror
│   │   └── references/PO.md, PS.md, PW.md, RV.md, GenAI-profile.md
│   ├── login-rate-limiting/         # type: vulnerability-pattern (self-contained)
│   ├── jwt-session-lifecycle/       # type: vulnerability-pattern (self-contained)
│   ├── api-response-minimization/   # type: vulnerability-pattern (self-contained)
│   ├── prevent-user-enumeration/    # type: vulnerability-pattern (self-contained)
│   ├── cors-configuration-review/   # type: vulnerability-pattern (self-contained)
│   ├── secrets-management/          # type: vulnerability-pattern (self-contained)
│   ├── error-handling-leaks/        # type: vulnerability-pattern (self-contained)
│   ├── ssrf-prevention/             # type: vulnerability-pattern (self-contained)
│   ├── webhook-signature-verification/ # type: vulnerability-pattern (self-contained)
│   └── excessive-agent-permissions/ # type: vulnerability-pattern (self-contained)
│
├── scripts/                         # regenera conteúdo espelhado + valida schema
│   ├── sync-owasp-top10-web.sh
│   ├── sync-owasp-llm-top10.sh
│   ├── sync-owasp-asvs.py
│   ├── sync-nist-ssdf.py
│   └── validate_skill.py
│
├── .github/workflows/
│   ├── validate-skills.yml          # CI: schema em todo push/PR que toque skills/**
│   └── check-upstream-freshness.yml # CI agendado: detecta drift da fonte oficial
│
├── LICENSE                          # MIT (o repo; cada skill declara a própria license)
├── ARCHITECTURE.md                  # este arquivo
└── README.md
```

**Por que `skills/` é plana (sem subpastas por categoria):** o `name` no
frontmatter precisa bater com o nome da pasta (regra da spec), e um
agente descobre skills varrendo um diretório raso. Categorização vive
nos metadados (`metadata.type`, `metadata.domain`), não na posição no
filesystem — assim uma skill pode pertencer a mais de um domínio sem
precisar escolher uma pasta.

## Taxonomia das skills

Toda skill se encaixa em exatamente um `metadata.type`:

| `type` | O que é | Conteúdo | Como se atualiza |
|---|---|---|---|
| `framework-mirror` | Espelho de um padrão oficial mantido por terceiros (OWASP, NIST) | Grande, gerado por script, baixo julgamento autoral — é a fonte oficial reformatada | `scripts/sync-*` — nunca editar `references/` à mão |
| `vulnerability-pattern` | Um padrão de falha real, específico e original, com correção | Pequeno, autocontido, alto julgamento autoral | Edição direta do `SKILL.md`, revisão humana |

E um `metadata.domain`, que espelha o slug da pasta temática (`01`–`10`)
mais próxima — a ponte entre a doc de estudo e a skill instalável:

`fundamentos` · `autenticacao-autorizacao` · `gestao-de-segredos` ·
`seguranca-llm-ia` · `dependencias-supply-chain` · `infraestrutura-cloud`
· `dados-e-privacidade` · `ci-cd-deploy` · `monitoramento-resposta` ·
`checklists-templates`

Opcionalmente, cross-refs para os frameworks de base, como texto livre
(não têm que ser exaustivos — servem para navegação, não para uma
ontologia formal):

- `owasp_top10: A07` — categoria(s) do OWASP Top 10 web
- `owasp_llm_top10: LLM06` — risco(s) do OWASP LLM Top 10
- `owasp_asvs: V6,V7` — capítulo(s) do ASVS
- `nist_ssdf: PW.1` — prática(s) do SSDF

Essas mesmas chaves (`owasp_top10`, `owasp_asvs` etc.) também aparecem
nas skills `framework-mirror`, ali descrevendo o intervalo completo que
a skill cobre (ex.: `owasp_asvs: V1-V17`) em vez de um item específico.

**Por que só duas categorias de `type`, e não uma taxonomia mais rica
(severidade, OWASP category, linguagem, etc.):** com 14 skills, uma
taxonomia elaborada é overhead sem benefício de busca. `type` existe
porque muda *como a skill se mantém* (script vs. edição manual) — uma
distinção operacional real, não decorativa. As demais dimensões (OWASP
category, ASVS chapter) já são strings livres em `metadata`, prontas
para virar filtro de verdade (um catálogo gerado, uma busca) se o número
de skills crescer o suficiente para justificar.

## Formato do `SKILL.md`

Frontmatter — superset da [spec agentskills.io](https://agentskills.io/specification)
mais as convenções deste repo:

```yaml
---
name: nome-da-skill              # obrigatório (spec) — idêntico ao nome da pasta
description: Use quando ...      # obrigatório (spec) — gatilho, não workflow
license: MIT                     # convenção do repo — MIT p/ vulnerability-pattern,
                                  # CC-BY-SA-4.0 ou "Public Domain" p/ framework-mirror
metadata:                        # convenção do repo — taxonomia (ver acima)
  type: vulnerability-pattern
  domain: autenticacao-autorizacao
  owasp_top10: A07
  owasp_asvs: V6
---
```

Corpo — dois templates, por `type`:

**`vulnerability-pattern`** (autocontido, sem `references/`):

```markdown
# Título curto do padrão de falha

## Padrão de falha
[sintoma concreto: o que um atacante consegue fazer e por quê]

## Como corrigir
[a correção, em prosa curta — o princípio, não só a checklist]

## Verificação

### Estático (revisão de código)
- [ ] item que dá pra checar olhando o código, sem executar nada

### Dinâmico (teste executado)
- [ ] uma ação concreta + o resultado esperado (ex.: "enviar X → esperado 403")

### Manual / agente
- [ ] pergunta ou passo que exige julgamento — não vira ✅/❌ mecânico

## Erros comuns
- confusão ou meia-solução frequente, e por que não basta

## Relacionado
- outra skill deste repo que cobre a mesma superfície de ataque
- capítulo/categoria do framework de base correspondente
```

**`framework-mirror`** (índice + `references/` por seção):

```markdown
# Nome do framework

## Overview
[o que é, quem mantém, por que é diferente dos outros frameworks do repo]

## When to use
[cenários concretos]

## Quick reference
[tabela: ID | categoria | link pra references/<ID>.md]

## How to use
[passo a passo curto de como navegar a tabela + os arquivos]

## Source
[repo/URL oficial espelhado, licença, e nota de que não é sincronizado
automaticamente — rodar o script de sync]
```

Regras de estilo, para as duas:

- `description` começa com o gatilho ("Use quando...", "Use when..."),
  nunca com um resumo do processo interno da skill (isso faz o agente
  seguir a descrição em vez de ler o corpo — ver
  `superpowers:writing-skills` para o porquê).
- Corpo em português para `vulnerability-pattern` (conteúdo original
  deste repo); `framework-mirror` mantém a língua da fonte oficial
  espelhada (inglês, no caso das quatro atuais) — espelho fiel, não
  tradução.
- Links cruzados citam o **nome da skill**, não o caminho de arquivo —
  sobrevive a uma skill sendo instalada isolada, fora da estrutura deste
  repo.

## Metodologia de validação

Três camadas, cada uma pega um tipo de erro diferente:

### 1. Validação estrutural (automática, todo push/PR)

`scripts/validate_skill.py` — sem dependências externas — checa:

- **Regras da spec** (falha bloqueia o PR): `name` casa com a pasta,
  regex `^[a-z0-9]+(-[a-z0-9]+)*$`, ≤ 64 caracteres; `description`
  presente e ≤ 1024 caracteres.
- **Convenção do repo** (gera aviso, não bloqueia sozinho): `license`
  presente; `metadata.type` em `{framework-mirror, vulnerability-pattern}`;
  `metadata.domain` presente; todo nome citado em "Relacionado" existe de
  verdade entre as skills passadas ao validador (checagem só roda quando
  `skills/*/` é validado inteiro, não uma skill isolada).

Roda local (`python3 scripts/validate_skill.py skills/*/`) e em CI
(`.github/workflows/validate-skills.yml`). Também validado contra o
validador oficial (`agentskills/agentskills` `skills-ref`) antes de cada
skill nova entrar no repo — as 14 skills atuais passam nos dois.

### 2. Frescor do conteúdo espelhado (automática, semanal)

Skills `framework-mirror` são só tão corretas quanto a última vez que
foram sincronizadas com a fonte oficial. `check-upstream-freshness.yml`
roda os 4 scripts de sync toda segunda-feira contra a fonte real e falha
(com `git diff --stat` no log) se algo mudou upstream e o repo ainda não
foi atualizado — sinal de que a OWASP/NIST revisou o documento e é hora
de rodar o sync, revisar o diff e commitar.

Isso substitui o processo manual ("re-pull from upstream for updates",
como a nota original da skill `owasp-llm-top10` dizia) por um script
testado e um alerta agendado — a skill não fica desatualizada em
silêncio.

### 3. Revisão de conteúdo (manual, no PR)

O que nenhum script consegue checar sozinho — critério pra quem revisa
um PR de skill nova:

**Para `framework-mirror`:**
- O conteúdo em `references/` veio do script de sync, não foi digitado à
  mão (`git diff` depois de rodar o sync deve dar vazio).
- `metadata.source` e `metadata.upstream_version` apontam pra fonte real
  e versão real, verificável no link.

**Para `vulnerability-pattern`:**
- O "Padrão de falha" descreve um cenário concreto e verificável (um
  request específico, uma resposta específica) — não uma afirmação
  vaga tipo "isso pode ser inseguro".
- Cada item de "Verificação" é uma coisa que dá pra marcar ✅/❌ olhando
  código, rodando um teste, ou seguindo um passo de revisão — não um
  conselho genérico ("configure isso com cuidado").
- "Relacionado" linka pra skills que existem de verdade neste repo —
  checado automaticamente pelo `validate_skill.py` (aviso, não falha,
  se o link estiver quebrado) quando o script roda contra `skills/*/`
  inteiro, não uma skill isolada.

Esta camada é deliberadamente manual: o valor de uma
`vulnerability-pattern` está no julgamento de que o padrão é real e a
correção é a certa — isso não é uma propriedade sintática que um linter
consiga verificar.

## Fluxo de contribuição (skill nova)

1. Decidir o `type`: é um padrão de vulnerabilidade original
   (`vulnerability-pattern`) ou o espelho de um framework que ainda não
   está no repo (`framework-mirror`)?
2. `mkdir skills/nome-da-skill`, escrever `SKILL.md` seguindo o template
   do `type` escolhido (acima).
3. `python3 scripts/validate_skill.py skills/nome-da-skill` — corrigir
   até sair `PASS`.
4. Se `framework-mirror`: escrever `scripts/sync-nome-da-skill.*`
   seguindo o padrão dos 4 existentes (baixa da fonte oficial, nunca
   conteúdo digitado à mão).
5. Abrir PR — `validate-skills.yml` roda sozinho; revisão de conteúdo
   (camada 3 acima) fica com quem revisar o PR.
