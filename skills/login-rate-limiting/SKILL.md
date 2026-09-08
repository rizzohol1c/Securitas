---
name: login-rate-limiting
description: Use ao projetar ou revisar endpoints de login, recuperação de senha ou verificação MFA/OTP — cobre proteção contra força bruta e credential stuffing quando o endpoint aceita tentativas ilimitadas, com rate limiting por IP e por conta, atraso progressivo, bloqueio temporário e verificação adicional.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: autenticacao-autorizacao
  owasp_top10: A07
  owasp_asvs: V6
---

# Login sem rate limiting

## Padrão de falha

Se o endpoint de login (ou recuperação de senha, ou verificação de MFA)
aceita tentativas ilimitadas, um script automatizado pode testar milhares
de combinações de senha por minuto até encontrar uma válida — força
bruta clássica, ou credential stuffing usando listas de senhas vazadas
em outros serviços.

## Como corrigir

Coloque limites de requisição para login, recuperação de senha e MFA,
considerando **IP e conta ao mesmo tempo** — um limite só por IP é
contornável com rotação de IP/VPN; um limite só por conta permite que um
atacante tente senhas em várias contas a partir do mesmo IP sem ser
pego. Para comportamento suspeito, escale a resposta: atraso progressivo
entre tentativas, bloqueio temporário da conta ou do IP, ou uma etapa
adicional de verificação (captcha, step-up de MFA).

## Verificação

### Estático (revisão de código)

- [ ] Existe rate limiting configurado no login, na recuperação de senha
      e na verificação de MFA/OTP — os três, não só o login
- [ ] O limite considera IP **e** conta ao mesmo tempo, não só um dos dois
- [ ] O limite é aplicado no servidor — não depende de JS no client, que
      pode ser ignorado por quem chama a API direto

### Dinâmico (teste executado)

- [ ] Fazer N tentativas de login inválidas seguidas — esperado: atraso
      progressivo, bloqueio temporário ou desafio extra a partir de um
      limite definido, não tentativas infinitas
- [ ] Repetir o mesmo teste variando o IP a cada tentativa — esperado:
      o limite por conta ainda bloqueia
- [ ] Confirmar que a resposta de bloqueio não revela se a conta existe
      (mesma mensagem que "senha incorreta" — ver `prevent-user-enumeration`)

### Manual / agente

- [ ] Revisar se recuperação de senha e MFA usam a mesma infraestrutura
      de rate limit do login, ou se é uma implementação paralela que foi
      esquecida

## Erros comuns

- Rate limit só por IP: contornável com rotação de IP.
- Rate limit só por conta: permite varrer muitas contas do mesmo IP.
- Mensagem de "conta bloqueada" diferente de "senha incorreta" — vaza
  quais contas existem (combine com a skill `prevent-user-enumeration`).

## Relacionado

- `prevent-user-enumeration` — evitar que a própria resposta de bloqueio
  vaze quem tem conta.
- Skill `owasp-asvs`, capítulo V6 (Authentication).
- Skill `owasp-top10-web`, categoria A07 (Authentication Failures).
