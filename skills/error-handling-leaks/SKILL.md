---
name: error-handling-leaks
description: Use ao projetar ou revisar tratamento de erro e exceção de uma aplicação — cobre vazamento de stack trace, mensagem de banco de dados ou detalhe interno na resposta HTTP quando algo falha, com handler de erro global e mensagens genéricas para o cliente.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: monitoramento-resposta
  owasp_top10: A10
  owasp_asvs: V16
---

# Erro vazando informação interna

## Padrão de falha

A aplicação devolve o stack trace, a mensagem de erro do banco de dados,
ou outro detalhe interno (caminho de arquivo, versão de biblioteca,
query SQL) direto na resposta HTTP quando algo falha. Acontece quando o
modo debug/verbose do framework fica ligado em produção, ou quando uma
exceção não tratada sobe até o cliente sem passar por nenhuma conversão.

## Como corrigir

Capture exceções numa borda única (middleware/handler global de erro) e
converta para uma mensagem genérica + código de erro antes de responder
ao cliente. Logue o detalhe completo só no servidor, correlacionado por
um request ID que o cliente pode citar num chamado de suporte. Desligue
o modo debug/verbose do framework em produção via configuração
explícita — não confie no valor padrão.

## Verificação

### Estático (revisão de código)

- [ ] Existe um handler de erro global que converte exceção → resposta
      genérica antes de qualquer coisa chegar no cliente
- [ ] O modo debug/verbose do framework está desligado em produção por
      configuração explícita, não por padrão do framework
- [ ] Nenhum `catch`/`except` devolve `err.message`/`err.stack` direto
      no corpo da resposta

### Dinâmico (teste executado)

- [ ] Forçar um erro não tratado (request malformado, dependência
      indisponível, campo inesperado) e inspecionar a resposta —
      esperado: mensagem genérica, sem stack trace, nome de tabela,
      caminho de arquivo ou versão de biblioteca
- [ ] Conferir headers da resposta de erro (não só o body) — não devem
      revelar framework/versão além do necessário

### Manual / agente

- [ ] Revisar se o request ID logado no servidor está de fato presente
      na resposta genérica ao cliente, pra permitir correlacionar um
      chamado de suporte com o log real

## Erros comuns

- "Só liga verbose em dev" — mas o deploy não trava se a variável de
  ambiente errada for esquecida.
- Mensagem genérica no corpo, mas o status HTTP ou um header ainda
  vazam detalhe (ex.: header expondo framework e versão exata).

## Relacionado

- `secrets-management` — um erro verboso é uma forma comum de vazar
  credencial de conexão com banco.
- Skill `owasp-top10-web`, categoria A10 (Mishandling of Exceptional
  Conditions).
- Skill `owasp-asvs`, capítulo V16 (Security Logging and Error
  Handling).
