---
name: webhook-signature-verification
description: Use ao implementar ou revisar um endpoint que recebe webhooks de um serviço externo — cobre verificação de assinatura HMAC, validação de timestamp contra replay de evento antigo, e idempotência por ID de evento.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: autenticacao-autorizacao
  owasp_top10: A07
  owasp_asvs: V4,V11
---

# Webhook sem verificação de assinatura

## Padrão de falha

Um endpoint recebe webhooks de um serviço externo (provedor de
pagamento, GitHub, um parceiro) e processa o payload confiando só que
"a requisição chegou na URL certa" — sem verificar a assinatura
criptográfica que o provedor envia num header. Qualquer um que descubra
a URL do endpoint (não é segredo — costuma aparecer em configuração
pública ou ser adivinhável) pode forjar um evento, como "pagamento
aprovado", e a aplicação aceita como se fosse legítimo.

## Como corrigir

Valide a assinatura HMAC do payload usando o segredo compartilhado com o
provedor, comparando com uma função de **tempo constante** (não `==`/
`===` simples, que vaza timing e permite adivinhar a assinatura byte a
byte). Valide o timestamp do evento contra uma janela de tolerância
curta, para rejeitar replay de um webhook antigo capturado. Torne o
processamento idempotente pelo ID do evento — provedores reenviam
webhooks em caso de timeout, e processar o mesmo evento duas vezes (dois
créditos, dois e-mails) é um bug de negócio, não só de segurança.

## Verificação

### Estático (revisão de código)

- [ ] O endpoint valida a assinatura do header (`X-Signature`,
      `Stripe-Signature`, etc.) antes de processar qualquer coisa do
      payload
- [ ] A comparação da assinatura usa uma função de tempo constante
      (`crypto.timingSafeEqual` ou equivalente da linguagem)
- [ ] O timestamp do evento é validado contra uma janela de tolerância
      (ex.: rejeitar eventos com mais de 5 minutos)
- [ ] O processamento é idempotente por ID de evento
- [ ] O segredo usado para validar a assinatura vem de configuração/
      secret manager (ver `secrets-management`), não está hardcoded

### Dinâmico (teste executado)

- [ ] Enviar um payload válido sem header de assinatura, e outro com
      assinatura incorreta — esperado: ambos rejeitados (4xx), sem
      processar o evento
- [ ] Reenviar exatamente o mesmo evento (mesmo ID) duas vezes —
      esperado: processado uma única vez
- [ ] Reenviar um evento válido com timestamp antigo (fora da janela de
      tolerância) — esperado: rejeitado como replay

### Manual / agente

- [ ] Conferir a documentação do provedor específico (Stripe, GitHub
      etc.) para o nome exato do header e o algoritmo de assinatura —
      cada provedor tem sua própria convenção

## Erros comuns

- Confiar só no IP de origem do provedor — é spoofável, e provedores
  mudam de range de IP sem aviso.
- Validar a assinatura mas não o timestamp — um webhook capturado uma
  vez continua podendo ser reenviado (replay) indefinidamente.
- Comparar a assinatura com `===`/`==` em vez de uma função de tempo
  constante.

## Relacionado

- `secrets-management` — o segredo compartilhado usado para assinar/
  verificar segue as mesmas regras de armazenamento.
- Skill `owasp-top10-web`, categoria A07 (Authentication Failures —
  verificar assinatura é autenticar o chamador).
- Skill `owasp-asvs`, capítulos V4 (API and Web Service) e V11
  (Cryptography).
