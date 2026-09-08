---
name: dependency-supply-chain-review
description: Use ao adicionar ou revisar uma dependência de terceiros (npm/pip/etc.) — cobre instalar um pacote só porque um agente de IA sugeriu o nome sem confirmar que ele existe de verdade (typosquatting/"slopsquatting"), lockfile ausente ou desatualizado, e dependência sem manutenção ativa aceita sem revisão.
license: MIT
metadata:
  type: vulnerability-pattern
  domain: dependencias-supply-chain
  owasp_top10: A03
  owasp_asvs: V15
---

# Dependência instalada sem revisão

## Padrão de falha

Um agente de IA sugere `npm install <pacote>` ou `pip install <pacote>`
como parte de uma solução, e o pacote é instalado sem ninguém confirmar
que ele é o pacote real e legítimo. Isso abre dois riscos distintos:

- **Typosquatting/slopsquatting.** Um nome parecido com um pacote
  popular (`reqeusts` em vez de `requests`) ou um nome que a própria IA
  alucinou (um pacote que soa plausível mas nunca existiu) pode já ter
  sido registrado por um atacante com código malicioso, especialmente
  depois que se tornou público que LLMs alucinam nomes de pacote de
  forma previsível.
- **Dependência sem manutenção.** Um pacote real, mas abandonado, sem
  atividade há anos, com uma única pessoa mantendo, ou com poucas
  instalações — superfície de risco maior e sem ninguém corrigindo
  vulnerabilidade encontrada.

## Como corrigir

Antes de instalar qualquer pacote sugerido por IA, confirme no registry
oficial (npmjs.com, pypi.org) que o nome existe, é o pacote esperado
(confira o repositório-fonte vinculado) e tem histórico de manutenção.
Sempre commite o lockfile (`package-lock.json`, `poetry.lock`,
`requirements.txt` com hash) — sem ele, builds diferentes podem resolver
versões diferentes da mesma dependência. Rode um scanner de
vulnerabilidade conhecida (`npm audit`, `pip-audit`, `osv-scanner`) como
parte do processo de adicionar uma dependência nova, não só
esporadicamente.

## Verificação

### Estático (revisão de código)

- [ ] O lockfile está commitado e não está no `.gitignore`
- [ ] Toda dependência nova tem o nome confirmado contra o registry
      oficial antes do merge (não só copiado do que a IA sugeriu)
- [ ] Existe um scanner de vulnerabilidade (`npm audit`, `pip-audit`,
      `osv-scanner` ou equivalente) rodando em CI, não só manual

### Dinâmico (teste executado)

- [ ] Rodar o scanner de vulnerabilidade contra o lockfile atual e
      conferir que não há CVE crítico/alto sem tratamento
- [ ] Tentar `npm ci` / instalação a partir só do lockfile (sem
      `node_modules` prévio) — esperado: build reprodutível, sem
      resolver versão diferente

### Manual / agente

- [ ] Para toda dependência adicionada nos últimos PRs, checar: data do
      último release, número de mantenedores, se o repositório-fonte no
      registry bate com o que era esperado

## Erros comuns

- Confiar no nome sugerido pela IA sem visitar o registry — o pacote
  pode nunca ter existido, ou existir com conteúdo malicioso registrado
  por outra pessoa depois que o nome alucinado virou público.
- Lockfile ausente ou desatualizado, "resolvido" rodando `npm install`
  de novo sem revisar o diff do lockfile gerado.
- Aceitar uma dependência só porque "funciona no teste", sem checar
  manutenção ou histórico de segurança.

## Relacionado

- Skill `nist-ssdf`, práticas PS (Protect the Software) e PW.4 (Reuse
  Existing, Well-Secured Software).
- Skill `owasp-top10-web`, categoria A03 (Software Supply Chain
  Failures).
