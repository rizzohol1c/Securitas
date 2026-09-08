# Skills

Esta pasta contém skills prontas para instalar em qualquer agente de IA
que suporte o formato aberto [Agent Skills](https://agentskills.io/specification)
(`SKILL.md` com frontmatter `name`/`description`) — não é específico do
Claude Code. Cada subpasta é uma skill independente, instalável sozinha.

Para a arquitetura completa (taxonomia, formato do `SKILL.md`,
metodologia de validação, como as skills se relacionam com o resto do
repo), ver [`ARCHITECTURE.md`](../ARCHITECTURE.md). Este README é só o
catálogo + instruções de instalação.

## Catálogo

### `type: framework-mirror` — espelho de padrão oficial (OWASP/NIST)

| Skill | Cobre | Fonte |
|---|---|---|
| [`owasp-top10-web`](owasp-top10-web/SKILL.md) | 10 categorias de risco em app web (A01–A10) | OWASP Top 10:2025 |
| [`owasp-llm-top10`](owasp-llm-top10/SKILL.md) | 10 riscos específicos de LLM/agente (LLM01–LLM10) | OWASP GenAI Security Project, 2025 v2.0 |
| [`owasp-asvs`](owasp-asvs/SKILL.md) | 346 requisitos verificáveis, 17 capítulos, níveis L1–L3 | OWASP ASVS 5.0.0 |
| [`nist-ssdf`](nist-ssdf/SKILL.md) | 42 práticas de processo seguro (PO/PS/PW/RV) + perfil GenAI | NIST SP 800-218 + SP 800-218A |

### `type: vulnerability-pattern` — padrão de falha original, com correção

| Skill | Cobre |
|---|---|
| [`login-rate-limiting`](login-rate-limiting/SKILL.md) | Força bruta em login/recuperação de senha/MFA sem limite de tentativas |
| [`jwt-session-lifecycle`](jwt-session-lifecycle/SKILL.md) | Armazenamento, expiração e revogação de token JWT |
| [`api-response-minimization`](api-response-minimization/SKILL.md) | API devolvendo campos/dados a mais do que o necessário |
| [`prevent-user-enumeration`](prevent-user-enumeration/SKILL.md) | Respostas que revelam se uma conta existe |
| [`cors-configuration-review`](cors-configuration-review/SKILL.md) | CORS permissivo demais e confusão entre CORS e autorização |
| [`secrets-management`](secrets-management/SKILL.md) | Chave/token/senha hardcoded no código ou commitada em `.env` |
| [`error-handling-leaks`](error-handling-leaks/SKILL.md) | Stack trace ou erro de banco vazando na resposta HTTP |
| [`ssrf-prevention`](ssrf-prevention/SKILL.md) | Requisição HTTP a partir de URL do usuário atingindo rede interna/metadata de nuvem |
| [`webhook-signature-verification`](webhook-signature-verification/SKILL.md) | Webhook processado sem verificar assinatura, timestamp ou idempotência |
| [`excessive-agent-permissions`](excessive-agent-permissions/SKILL.md) | Agente de IA com tool destrutiva sem confirmação ou checagem de permissão |

## Como instalar

Copie a pasta da skill inteira (com o `SKILL.md`) para o diretório de
skills do seu agente:

```bash
# Claude Code (pessoal, disponível em todos os projetos)
cp -r skills/login-rate-limiting ~/.claude/skills/

# Codex CLI, Copilot CLI, Gemini CLI (alias multi-runtime)
cp -r skills/login-rate-limiting ~/.agents/skills/

# Skill só para um projeto específico (qualquer agente compatível)
cp -r skills/login-rate-limiting /caminho/do/seu/projeto/.claude/skills/
```

Ou copie a pasta `skills/` inteira de uma vez para instalar todas.

Para outros agentes, consulte a documentação deles sobre onde procuram
skills locais — o formato (`SKILL.md` com `name` e `description` no
frontmatter) é o mesmo definido pela spec, então qualquer agente
compatível deve reconhecer a pasta sem alteração.

## Como validar uma skill

```bash
python3 scripts/validate_skill.py skills/*/
```

Checa a spec (nome/descrição válidos, pasta bate com `name`) e a
convenção deste repo (`license`, `metadata.type`, `metadata.domain`).
Roda automaticamente em CI a cada push/PR que toque `skills/**`
(`.github/workflows/validate-skills.yml`).

## Como atualizar uma skill `framework-mirror`

Não edite `references/` à mão — rode o script de sync correspondente e
revise o diff:

```bash
./scripts/sync-owasp-top10-web.sh
./scripts/sync-owasp-llm-top10.sh
python3 scripts/sync-owasp-asvs.py
python3 scripts/sync-nist-ssdf.py
```

Um workflow semanal (`check-upstream-freshness.yml`) roda os quatro e
falha se o conteúdo oficial mudou e o repo ainda não foi atualizado.

## Contribuindo com uma skill nova

Ver [`ARCHITECTURE.md`](../ARCHITECTURE.md#metodologia-de-validação)
para o processo completo. Resumo:

1. Um padrão de vulnerabilidade real e específico, não uma reescrita de
   um framework que já existe (esses são `framework-mirror`, gerados por
   script a partir da fonte oficial).
2. `mkdir skills/nome-da-skill` — `name` no frontmatter idêntico ao nome
   da pasta.
3. `description` começa descrevendo quando usar (gatilhos concretos),
   não o que a skill faz passo a passo.
4. Preencha `license` e `metadata.type`/`metadata.domain`.
5. Rode `python3 scripts/validate_skill.py skills/nome-da-skill` antes
   do PR.
