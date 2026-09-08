# Securitas — guia para agentes de IA

Repositório de skills de segurança no formato aberto
[Agent Skills](https://agentskills.io/specification), mais documentação
de estudo sobre segurança para SaaS construído com apoio de IA. Duas
camadas: `00-frameworks-base/` e `01`–`10` são documentação de estudo;
`skills/` é o produto instalável.

Antes de editar, leia [`ARCHITECTURE.md`](ARCHITECTURE.md) (estrutura,
taxonomia, formato do `SKILL.md`, metodologia de validação) e
[`skills/README.md`](skills/README.md) (catálogo e como instalar). Este
arquivo é o resumo operacional, não substitui os dois.

## Regras ao trabalhar neste repo

### Skills (`skills/`)

- Cada skill é `skills/<nome>/SKILL.md`. O `name` no frontmatter tem que
  ser idêntico ao nome da pasta (regra da spec, não convenção).
- Todo `SKILL.md` declara `metadata.type`: `framework-mirror` ou
  `vulnerability-pattern`. Não crie um terceiro tipo sem atualizar
  `ARCHITECTURE.md` primeiro.
- **`framework-mirror`** (`owasp-top10-web`, `owasp-llm-top10`,
  `owasp-asvs`, `nist-ssdf`): nunca edite `references/` à mão. Rode o
  script de sync correspondente (`scripts/sync-*.sh`/`.py`) e commite o
  diff que ele gerar. O conteúdo é em inglês, espelhando a fonte
  oficial.
- **`vulnerability-pattern`**: siga o template nesta ordem — Padrão de
  falha, Como corrigir, Verificação (Estático / Dinâmico / Manual-agente),
  Erros comuns, Relacionado. Conteúdo em português, autocontido (sem
  `references/`).
- Depois de criar ou editar uma skill, rode
  `python3 scripts/validate_skill.py skills/*/` contra a pasta inteira
  (não a skill isolada — isolada não ativa a checagem de link cruzado
  quebrado em "Relacionado"). Tem que sair só `PASS`, sem `FAIL`.
- Skill nova: crie a pasta, escreva o `SKILL.md`, valide, adicione uma
  linha no catálogo de `skills/README.md` e, se fizer sentido, um link
  no README do tema correspondente em `01`–`10`.

### Documentação (`00-frameworks-base/`, `01`–`10`)

Essas pastas são resumo e "por que importa para vibe coding", nunca uma
cópia do conteúdo integral de um framework. Se o conteúdo já existe numa
skill `framework-mirror`, linke para ela em vez de reescrever.

### Licença

MIT para o repositório e para skills `vulnerability-pattern`. Skills
`framework-mirror` mantêm a licença da fonte que espelham (CC BY-SA 4.0
para as da OWASP, domínio público para as do NIST) — declarada no
próprio `metadata`/`license` do `SKILL.md`.

## Outros agentes de código

Este arquivo também é lido por outros agentes via os aliases
`AGENTS.md` e `GEMINI.md` (symlinks para este arquivo) — mantenha o
conteúdo aqui, não duplique nos symlinks.
