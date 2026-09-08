---
name: ci-cd-pipeline-hardening
description: Use ao configurar ou revisar um pipeline de CI/CD — cobre segredo de produção acessível a partir de um pull request de fork externo, branch de deploy sem revisão obrigatória, e action/plugin de terceiro fixado por tag mutável em vez de hash de commit.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: ci-cd-deploy
  owasp_top10: A08
  owasp_asvs: V15
---

# Pipeline de CI/CD sem proteção

## Padrão de falha

O pipeline de CI/CD roda com segredo de produção acessível em qualquer
execução, inclusive a partir de um pull request de um fork externo — um
padrão comum quando o workflow usa o evento `pull_request_target` (que
roda com acesso aos secrets do repositório base) combinado com checkout
do código do próprio PR (que pode ter sido escrito por qualquer um).
Outro padrão comum: a branch principal ou de deploy aceita merge direto
sem revisão nem status check obrigatório, "porque o time é pequeno e dá
pra confiar".

## Como corrigir

Segredo de produção só deve estar disponível em workflows que rodam a
partir da branch protegida, nunca em contexto que executa código vindo
de um PR externo sem revisão. Configure proteção de branch: revisão
obrigatória antes de merge, status checks obrigatórios (incluindo
`validate-skills`-style CI), sem permitir force-push na branch de
deploy. Fixe actions e plugins de terceiro por hash de commit
(`uses: owner/action@<sha completo>`), não por tag (`@v2`) — uma tag
pode ser reapontada pelo mantenedor (ou por quem comprometer a conta
dele) sem aviso.

## Verificação

### Estático (revisão de código)

- [ ] Nenhum workflow usa `pull_request_target` com checkout do código
      do PR em contexto que tem acesso a secret de produção
- [ ] Actions/plugins de terceiro usados no workflow estão fixados por
      hash de commit, não por tag mutável
- [ ] A branch de deploy/principal tem proteção configurada (revisão
      obrigatória, status check obrigatório, sem force-push)

### Dinâmico (teste executado)

- [ ] Abrir um pull request a partir de um fork e conferir, no log do
      workflow, se algum secret de produção fica acessível nesse
      contexto — esperado: não
- [ ] Tentar dar merge numa branch protegida sem aprovação/sem os status
      checks passarem — esperado: bloqueado pela regra de proteção

### Manual / agente

- [ ] Revisar todos os workflows do repositório procurando por
      `pull_request_target`, e para cada ocorrência confirmar que não há
      checkout de código não confiável na mesma execução

## Erros comuns

- Usar `pull_request_target` para rodar CI em PRs de fork "porque
  `pull_request` normal não dá acesso aos secrets que o teste precisa" —
  a correção certa é não precisar do secret nesse contexto, não trocar o
  evento.
- Fixar action de terceiro por tag (`@v2`, `@main`) em vez de hash de
  commit.
- Achar que branch protection é overhead desnecessário pra um time
  pequeno — o pipeline continua tendo acesso total de deploy
  independente do tamanho do time.

## Relacionado

- `secrets-management` — os segredos que esse pipeline expõe ou protege
  seguem as mesmas regras de armazenamento.
- Skill `owasp-top10-web`, categoria A08 (Software or Data Integrity
  Failures).
- Skill `nist-ssdf`, prática PS (Protect the Software).
