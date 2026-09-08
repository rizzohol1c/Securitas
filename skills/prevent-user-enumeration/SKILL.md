---
name: prevent-user-enumeration
description: Use ao projetar ou revisar fluxos de login, cadastro ou recuperação de senha — cobre vazamento de quais contas existem quando a aplicação responde de forma diferente para "e-mail não cadastrado" e "senha incorreta", com respostas genéricas e sem endpoints públicos de checagem de existência de usuário.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: autenticacao-autorizacao
  owasp_top10: A07
  owasp_asvs: V6
---

# Enumeração de usuários

## Padrão de falha

Se o sistema responde "e-mail não cadastrado" para uma conta inexistente
e "senha incorreta" para uma conta existente, ele está entregando
informação útil para quem estiver testando a aplicação — um atacante
consegue montar uma lista de contas válidas antes mesmo de tentar
adivinhar a senha (útil para força bruta direcionada). O mesmo problema
aparece em telas de cadastro que confirmam diretamente "e-mail já em
uso", ou em endpoints públicos que permitem consultar se um usuário
existe.

## Como corrigir

Use respostas genéricas no login e nos fluxos de recuperação de senha —
a mesma mensagem, o mesmo código HTTP e, idealmente, o mesmo tempo de
resposta, independente de a conta existir ou não (ex.: "se esse e-mail
estiver cadastrado, você vai receber um link de recuperação"). Evite
endpoints públicos que permitam consultar diretamente se um determinado
usuário/e-mail existe.

## Verificação

### Estático (revisão de código)

- [ ] Login e recuperação de senha usam a mesma mensagem/código HTTP de
      resposta independente de a conta existir
- [ ] Cadastro não confirma diretamente "e-mail já cadastrado" sem
      alguma mitigação (rate limit, captcha, ou fluxo assíncrono por
      e-mail)
- [ ] Não existe endpoint público não autenticado dedicado a checar
      "usuário existe: sim/não"

### Dinâmico (teste executado)

- [ ] Tentar login com um e-mail que existe (senha errada) e um que não
      existe — esperado: mesma mensagem, mesmo código HTTP
- [ ] Medir o tempo de resposta dos dois casos acima — esperado: sem
      diferença perceptível (senão é um timing side-channel)
- [ ] Pedir recuperação de senha pra um e-mail que não existe —
      esperado: mesma resposta genérica de quando existe

### Manual / agente

- [ ] Revisar o fluxo de cadastro perguntando: alguma resposta,
      diferença de tempo, ou header permite distinguir "e-mail já
      cadastrado" de "e-mail novo"?

## Erros comuns

- Mensagens diferentes "por usabilidade" — ajuda o usuário legítimo, mas
  ajuda igualmente quem está testando contas.
- Checar a senha só depois de confirmar que a conta existe, criando uma
  diferença de tempo de resposta mensurável entre os dois casos.

## Relacionado

- `login-rate-limiting` — mesma superfície de ataque (força bruta),
  complementar a este controle.
- Skill `owasp-asvs`, capítulo V6 (Authentication).
- Skill `owasp-top10-web`, categoria A07 (Authentication Failures).
