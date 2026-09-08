---
name: secrets-management
description: Use ao revisar como uma aplicação armazena, distribui ou versiona credenciais — cobre chaves de API, tokens e senhas hardcoded no código ou commitados em .env, com boas práticas de variável de ambiente, secret manager e rotação depois de um vazamento.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: gestao-de-segredos
  owasp_top10: A02
  owasp_asvs: V13
---

# Segredo hardcoded ou commitado

## Padrão de falha

Chave de API, credencial de banco ou token fica escrito direto no
código-fonte, ou num `.env` que acaba commitado no git. É um padrão
comum em vibe coding: a IA sugere colar a chave direto no arquivo "pra
testar rápido", e aquilo nunca é removido — ou é removido do arquivo
atual, mas continua para sempre no histórico do git.

## Como corrigir

Segredo nunca entra no código-fonte — só em variável de ambiente,
carregada em tempo de execução. Em produção, prefira um secret manager
(Vault, AWS/GCP Secrets Manager, Doppler etc.) a um `.env` estático.
Se um segredo já foi commitado, remover o arquivo **não resolve** — ele
continua no histórico; a correção é rotacionar a credencial (torná-la
inválida e gerar uma nova).

## Verificação

### Estático (revisão de código)

- [ ] Nenhuma string com cara de chave/token/senha está hardcoded no
      código (padrões comuns: `sk-`, `AKIA`, `-----BEGIN`, URLs de
      conexão com senha embutida)
- [ ] `.env` está no `.gitignore`; o repositório não versiona nenhum
      arquivo `.env` real (só `.env.example` com placeholders)
- [ ] Segredos de produção são diferentes dos usados em
      desenvolvimento/exemplo

### Dinâmico (teste executado)

- [ ] Rodar um scanner de segredo (gitleaks, trufflehog, detect-secrets)
      contra o **histórico completo** do repositório, não só o HEAD

### Manual / agente

- [ ] Se um segredo for encontrado, confirmar se ele já apareceu em
      outro branch, PR fechado ou issue antes de decidir se precisa
      rotacionar (geralmente precisa)

## Erros comuns

- Remover o segredo do arquivo atual mas esquecer que ele continua no
  histórico do git — precisa rotacionar, não só apagar.
- `.env.example` com um valor real em vez de um placeholder óbvio.
- Confiar que "é um repo privado" — repo pode virar público, e
  colaborador com acesso pode vazar o segredo por engano.

## Relacionado

- `webhook-signature-verification` — o segredo usado pra verificar
  assinatura de webhook segue as mesmas regras.
- Skill `owasp-asvs`, capítulo V13 (Configuration).
- Skill `owasp-top10-web`, categoria A02 (Security Misconfiguration).
