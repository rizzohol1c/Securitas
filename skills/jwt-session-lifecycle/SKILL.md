---
name: jwt-session-lifecycle
description: Use ao projetar ou revisar autenticação baseada em JWT — cobre onde o token é armazenado e transmitido, tempo de vida (TTL), e como revogar sessão no logout, incluindo o padrão de access token curto com refresh token rotacionado e revogável.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: autenticacao-autorizacao
  owasp_top10: A07
  owasp_asvs: V7,V9,V10
---

# JWT tratado como sinônimo de segurança

## Padrão de falha

Usar JWT não resolve sozinho o problema de autenticação. Erros comuns:
enviar o token pela URL (fica em logs de servidor, histórico do browser,
header Referer); e fazer "logout" apagando o token só no navegador —
dependendo da arquitetura, o token continua válido no servidor até
expirar, mesmo depois do usuário "sair".

## Como corrigir

Revise três pontos:

1. **Onde o token é armazenado e transmitido** — nunca em query string/URL;
   preferir header `Authorization` ou cookie `HttpOnly` + `Secure` +
   `SameSite`.
2. **Quanto tempo ele permanece válido** — TTL curto para o token de
   acesso (minutos, não dias).
3. **Como a aplicação revoga sessão** quando precisa de logout imediato
   — precisa existir um mecanismo server-side, não só apagar o token no
   client.

Em muitos casos, a abordagem mais adequada é: **access token de vida
curta** combinado com **refresh token rotacionado e revogável** (cada
uso gera um novo refresh token, e o anterior é invalidado — reuso de um
refresh token antigo é sinal de comprometimento).

## Verificação

### Estático (revisão de código)

- [ ] Token nunca trafega em query string/URL
- [ ] Armazenamento no client é seguro (cookie `HttpOnly`+`Secure`+`SameSite`,
      ou proteção equivalente contra XSS se for `localStorage`/memória)
- [ ] Access token tem TTL curto (minutos) — checar a config, não supor
- [ ] Existe endpoint/mecanismo de revogação server-side, não só
      "esquecer" o token no client

### Dinâmico (teste executado)

- [ ] Fazer logout e reusar o access token antigo numa rota protegida —
      esperado: rejeitado, não continua válido até expirar sozinho
- [ ] Usar um refresh token duas vezes seguidas (reuso) — esperado: a
      segunda tentativa é rejeitada e, idealmente, invalida a sessão
      inteira (sinal de token roubado)
- [ ] Trocar a senha do usuário e reusar uma sessão antiga — esperado:
      sessão revogada

### Manual / agente

- [ ] Revisar se existe uma forma de revogar **todas** as sessões de um
      usuário de uma vez (comprometimento de conta), não só uma sessão
      por vez

## Erros comuns

- "Usei JWT, então tá seguro" — JWT é só o formato do token, não uma
  garantia de segurança.
- TTL longo "porque é mais prático" — aumenta a janela de uso de um
  token roubado.
- Refresh token que não é rotacionado — permite replay se vazar uma vez.

## Relacionado

- Skill `owasp-asvs`, capítulos V7 (Session Management), V9
  (Self-contained Tokens) e V10 (OAuth and OIDC).
- Skill `owasp-top10-web`, categoria A07 (Authentication Failures).
