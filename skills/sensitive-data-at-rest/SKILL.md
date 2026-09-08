---
name: sensitive-data-at-rest
description: Use ao desenhar ou revisar como uma aplicação armazena dado sensível (CPF, cartão, saúde, senha) — cobre dado regulado guardado em texto puro no banco, confiar só na criptografia de disco do provedor de cloud como se bastasse, e armazenar dado que nem precisava ser guardado (ex. número de cartão completo) em vez de tokenizar.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: dados-e-privacidade
  owasp_top10: A04
  owasp_asvs: V14,V11
---

# Dado sensível sem criptografia em repouso

## Padrão de falha

Dado sensível e regulado (CPF, número de cartão, dado de saúde) fica
armazenado em texto puro numa coluna comum do banco, porque foi o jeito
mais rápido de fazer a feature funcionar. É comum confundir "o provedor
de cloud criptografa o disco" com "o dado está protegido" — criptografia
de disco protege contra roubo físico do disco, não contra um dump de
banco vazado por SQL injection, um backup mal protegido, ou um acesso
indevido de alguém com credencial ao banco.

## Como corrigir

Primeiro pergunte se o dado precisa mesmo ser armazenado: número de
cartão completo, por exemplo, quase nunca precisa — um gateway de
pagamento (Stripe, Pagar.me) tokeniza o cartão e a aplicação guarda só o
token, nunca o número real. Para o que precisa ficar (CPF, dado de
saúde), criptografe a nível de coluna — não confie só na criptografia de
disco do provedor, que não protege contra um dump via injection ou um
backup exposto. Garanta que backups têm a mesma proteção que o banco
principal; um backup em texto puro anula a criptografia da tabela
original.

## Verificação

### Estático (revisão de código)

- [ ] Dado de cartão completo não é armazenado — o fluxo usa tokenização
      de um gateway de pagamento
- [ ] Colunas com dado sensível regulado (CPF, saúde, biometria) usam
      criptografia a nível de coluna/aplicação, não só a criptografia de
      disco do provedor
- [ ] O processo de backup criptografa o backup com o mesmo padrão do
      banco principal

### Dinâmico (teste executado)

- [ ] Fazer um dump direto do banco (ou consultar a tabela via SQL como
      um usuário com acesso de leitura ao banco, não pela API) e
      conferir se o dado sensível aparece em claro — esperado: aparece
      cifrado, não legível
- [ ] Verificar um backup recente e confirmar que ele está cifrado, não
      só o banco em produção

### Manual / agente

- [ ] Listar todo campo que armazena dado pessoal ou regulado e
      perguntar, campo a campo: "isso precisa mesmo ficar guardado, ou dá
      pra tokenizar/não guardar?"

## Erros comuns

- Achar que "o provedor de cloud já criptografa tudo" é suficiente —
  isso protege só contra roubo físico do disco, não contra vazamento via
  aplicação ou backup exposto.
- Guardar número de cartão completo em vez de usar tokenização do
  gateway de pagamento.
- Backup do banco sem a mesma proteção que a tabela original, tornando a
  criptografia da tabela irrelevante.

## Relacionado

- `secrets-management` — mesma disciplina de "não guarde o que não
  precisa", aplicada a dado de usuário em vez de credencial da
  aplicação.
- Skill `owasp-asvs`, capítulos V14 (Data Protection) e V11
  (Cryptography).
- Skill `owasp-top10-web`, categoria A04 (Cryptographic Failures).
