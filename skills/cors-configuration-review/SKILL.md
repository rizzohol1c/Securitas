---
name: cors-configuration-review
description: Use ao configurar ou revisar cabeçalhos CORS de uma API — cobre configuração permissiva demais como Access-Control-Allow-Origin "*" em aplicações com dado privado, e o erro de confundir CORS com autorização, já que CORS é uma regra respeitada pelo navegador e não protege chamadas feitas fora dele.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: infraestrutura-cloud
  owasp_top10: A02
  owasp_asvs: V13
---

# CORS permissivo demais

## Padrão de falha

Uma configuração como `Access-Control-Allow-Origin: *` pode ser
inadequada para uma aplicação que trabalha com dados privados,
especialmente quando combinada com outras configurações de autenticação
(como `Access-Control-Allow-Credentials: true`, que não deveria nunca
conviver com origem `*`).

## Como corrigir

Revise quais origens realmente precisam acessar a API e permita apenas
essas — uma allowlist explícita, não um wildcard copiado de um exemplo
ou tutorial. E não confunda CORS com autorização: mesmo com CORS bem
configurado, cada endpoint precisa verificar autenticação e permissões
no servidor. CORS é uma regra que o **navegador** obedece; qualquer
outro tipo de cliente (curl, Postman, um serviço server-to-server, ou um
atacante script) ignora CORS completamente — ele não é uma camada de
proteção contra acesso direto à API.

## Verificação

### Estático (revisão de código)

- [ ] `Access-Control-Allow-Origin` não é `*` em API com dado
      autenticado/privado
- [ ] A lista de origens permitidas é explícita e foi revisada (não
      copiada de um template/tutorial)
- [ ] Se usa `Access-Control-Allow-Credentials: true`, a origem
      correspondente nunca é `*` (combinação inválida e perigosa)
- [ ] CORS não é a única defesa contra CSRF (usar token CSRF ou cookie
      `SameSite` quando aplicável)

### Dinâmico (teste executado)

- [ ] Mandar uma requisição com header `Origin` de um domínio fora da
      allowlist — esperado: resposta sem `Access-Control-Allow-Origin`
      correspondente (browser bloqueia)
- [ ] Chamar o endpoint direto por fora do browser (curl), sem header
      `Origin` — esperado: continua exigindo autenticação/autorização
      normalmente (prova que CORS não é a única barreira)

### Manual / agente

- [ ] Revisar se cada endpoint checa autenticação e autorização no
      servidor, independente de o CORS estar "correto" — CORS sozinho
      não é controle de acesso

## Erros comuns

- Copiar `Access-Control-Allow-Origin: *` de um exemplo/tutorial e
  deixar em produção.
- Achar que CORS "protege" a API — CORS é uma regra do browser, não uma
  barreira de acesso; um script fora do browser ignora CORS.

## Relacionado

- Skill `owasp-asvs`, capítulo V13 (Configuration).
- Skill `owasp-top10-web`, categoria A02 (Security Misconfiguration).
