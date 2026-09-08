---
name: ssrf-prevention
description: Use ao implementar ou revisar qualquer funcionalidade que faça uma requisição HTTP a partir de uma URL fornecida ou influenciada pelo usuário — fetch de imagem, webhook de callback, import por URL, ou uma tool de agente de IA que navega a web — cobre Server-Side Request Forgery contra endpoints internos e metadata de nuvem.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: infraestrutura-cloud
  owasp_top10: A01
  owasp_asvs: V2,V4
---

# SSRF em requisições a partir de URL do usuário

## Padrão de falha

A aplicação faz uma requisição HTTP para uma URL fornecida (ou
influenciada) pelo usuário — um "buscar imagem por URL", um webhook de
callback configurável, ou um agente de IA com tool de fetch/scraping —
sem validar o destino. Um atacante aponta para
`http://169.254.169.254/latest/meta-data` (endpoint de metadata das
nuvens AWS/GCP/Azure, que expõe credenciais da instância) ou para um
endereço interno (`localhost`, uma rede privada) e a aplicação vira um
proxy involuntário para a rede interna.

## Como corrigir

Nunca aceite uma URL arbitrária sem validar o destino **resolvido** —
valide o IP depois de resolver o DNS, não só a string do hostname
declarado, porque o hostname pode apontar para um IP diferente no
momento da requisição (TOCTOU). Bloqueie por padrão ranges privados,
loopback e link-local (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`,
`127.0.0.0/8`, `169.254.0.0/16`, e os equivalentes IPv6). Prefira uma
allowlist de domínios quando o conjunto de destinos legítimos é
conhecido. Não siga redirects HTTP automaticamente sem revalidar o novo
destino a cada salto.

## Verificação

### Estático (revisão de código)

- [ ] Toda função que faz requisição HTTP a partir de input do usuário
      passa por um validador de destino central antes de disparar a
      requisição
- [ ] A validação resolve o DNS e checa o **IP resultante** contra
      ranges privados/loopback/link-local — não só a string do hostname
- [ ] Redirects HTTP não são seguidos automaticamente sem revalidar o
      novo destino

### Dinâmico (teste executado)

- [ ] Apontar o fetcher para `http://169.254.169.254`,
      `http://localhost`, `http://127.0.0.1` e um IP de rede privada —
      esperado: requisição bloqueada nos quatro casos
- [ ] Usar um domínio que resolve para um IP público mas redireciona
      (HTTP 3xx) para um IP privado — esperado: bloqueado na
      revalidação do redirect, não só na primeira checagem

### Manual / agente

- [ ] Listar toda feature que aceita URL do usuário (webhook, import por
      URL, fetch de imagem/PDF, tool de agente com acesso à web) e
      confirmar que todas passam pelo mesmo validador central, não uma
      checagem duplicada e potencialmente inconsistente por feature

## Erros comuns

- Validar só o hostname declarado, sem resolver o DNS — um atacante usa
  um domínio próprio que resolve para um IP interno.
- Bloquear só `localhost` literal, esquecendo `127.0.0.1`, `0.0.0.0`,
  `::1` (IPv6) ou a notação decimal do IP (`2130706433` = `127.0.0.1`).
- Tratar allowlist de esquema (`http`/`https`) como se fosse suficiente
  — o problema é o destino da requisição, não o protocolo usado.

## Relacionado

- Skill `owasp-top10-web`, categoria A01 (Broken Access Control — SSRF
  foi absorvido nessa categoria no Top 10:2025).
- Skill `owasp-asvs`, capítulo V2 (Validation and Business Logic).
- Skill `owasp-llm-top10`, risco LLM06 (Excessive Agency), quando o
  fetcher é uma tool de agente sem sandboxing de rede.
