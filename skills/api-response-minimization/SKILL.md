---
name: api-response-minimization
description: Use ao projetar ou revisar o payload de resposta de um endpoint de API — cobre exposição excessiva de dados (over-fetching) quando o endpoint devolve o registro inteiro do banco em vez de só os campos necessários, com filtragem e autorização no servidor antes de buscar ou devolver dado sensível.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: autenticacao-autorizacao
  owasp_top10: A01
  owasp_asvs: V4,V8
---

# API devolvendo dados demais

## Padrão de falha

A interface precisa do nome e do e-mail, mas o endpoint devolve o
registro inteiro do banco. É comum encontrar APIs retornando informações
internas (hash de senha, IDs internos, dados de outros usuários, campos
administrativos) que nem sequer são usados pelo frontend — mas que
qualquer cliente que chame a API direto (não só o frontend oficial)
consegue ler.

## Como corrigir

Cada endpoint deve definir explicitamente **quais campos pode retornar**
— uma allowlist de saída (schema/DTO), nunca serializar o model do banco
inteiro por conveniência. Faça a filtragem no servidor, não confie que o
frontend "esconde" o campo que não usa. Aplique autorização **antes** de
buscar ou devolver o dado sensível — não busque tudo e filtre só na
resposta.

## Verificação

### Estático (revisão de código)

- [ ] O endpoint tem um schema de saída explícito (allowlist de campos),
      não serializa o model/entidade do banco direto
- [ ] Autorização é checada antes da query/leitura do dado, não só
      filtrada depois na resposta
- [ ] Diferentes níveis de permissão (admin vs. usuário comum) usam
      schemas de saída diferentes, não o mesmo payload "escondido" no
      frontend

### Dinâmico (teste executado)

- [ ] Chamar o endpoint direto (curl/Postman, fora do frontend oficial)
      e conferir campo a campo o que volta — esperado: só os campos do
      schema de saída, nunca hash de senha, token interno ou dado de
      outro usuário
- [ ] Chamar o mesmo endpoint autenticado como usuário comum e como
      admin — esperado: payloads diferentes, não o mesmo JSON com campo
      "escondido" só na UI

### Manual / agente

- [ ] Revisar todo endpoint novo perguntando "quais campos a interface
      realmente usa?" e comparar com o que o schema de saída retorna —
      qualquer campo a mais é over-fetching

## Erros comuns

- "O frontend não usa esse campo, então tá ok expor" — a API pode ser
  chamada direto, fora do frontend (curl, outro serviço, um atacante).
- Serializar o ORM/model inteiro (`SELECT *` → JSON) por conveniência.
- Filtrar campo só na resposta (`.pick()`/`.omit()`) em vez de já buscar
  só o necessário — mais fácil de esquecer um campo novo no futuro.

## Relacionado

- Skill `owasp-asvs`, capítulos V8 (Authorization) e V4 (API and Web
  Service).
- Skill `owasp-top10-web`, categoria A01 (Broken Access Control).
- Skill `owasp-llm-top10`, risco LLM02, se o campo devolvido alimentar
  um prompt de IA.
