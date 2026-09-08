# NIST SSDF (+ perfil para IA generativa)

**Versões de referência:** NIST SP 800-218 (SSDF v1.1) e NIST SP 800-218A
— *"Secure Software Development Practices for Generative AI and Dual-Use
Foundation Models: An SSDF Community Profile"* (2024), que estende o SSDF
com práticas específicas para desenvolvimento envolvendo IA generativa.
Fontes: <https://csrc.nist.gov/projects/ssdf> ·
<https://csrc.nist.gov/pubs/sp/800/218/a/final>

> 🔧 **Skill instalável:** [`skills/nist-ssdf`](../skills/nist-ssdf/SKILL.md)
> — as 42 práticas oficiais (PO/PS/PW/RV) com suas tasks, mais um resumo
> do perfil GenAI, atualizável via `scripts/sync-nist-ssdf.py`.

## O que é

O SSDF não lista vulnerabilidades nem requisitos técnicos — ele organiza
**práticas de processo**: em que momento do ciclo de vida de
desenvolvimento cada prática de segurança deveria entrar. É o
complemento de processo para o conteúdo técnico do OWASP.

## As 4 famílias de prática (SSDF v1.1)

| Grupo | Nome | Pergunta central |
|---|---|---|
| **PO** | Prepare the Organization | Times, ferramentas e política estão prontos para desenvolver com segurança? |
| **PS** | Protect the Software | Código-fonte e artefatos de build estão protegidos contra alteração indevida? |
| **PW** | Produce Well-Secured Software | O software foi desenhado, codificado e testado para minimizar vulnerabilidade? |
| **RV** | Respond to Vulnerabilities | Vulnerabilidades encontradas depois do deploy são identificadas e corrigidas? |

## O que o perfil GenAI (SP 800-218A) acrescenta

Pensado para quem constrói *com* ou *sobre* modelos generativos — exatamente
o caso de vibe coding com agentes de IA:

- **PO**: documentar a tolerância a risco e o uso pretendido do modelo/IA
  antes de começar a construir.
- **PS**: proteger dado de treino e artefatos de modelo (prompts,
  fine-tunes, embeddings) contra adulteração — não só o código-fonte.
- **PW**: validar a proveniência do dado usado e fazer threat modeling do
  caminho de inferência (o que entra no modelo, o que sai, quem pode
  influenciar cada lado).
- **RV**: monitorar o modelo em produção para *behavior drift* — não só
  bug de código, mas o modelo passando a se comportar de forma diferente
  do esperado.

## Por que importa especificamente em vibe coding

Vibe coding tende a pular direto para "PW" (produzir código) e ignorar
"PO" e "RV": ninguém define upfront que dado é sensível, e ninguém volta
depois para monitorar se o agente em produção continua se comportando
como devia. O SSDF é o lembrete de que segurança não é uma etapa antes
do deploy — é uma prática distribuída ao longo de todo o ciclo.

## Como uso isso no repositório

Serve de eixo temporal para o resto do repositório: `01-fundamentos/`
usa PO/PW para estruturar "o que fazer antes de codificar";
`08-ci-cd-deploy/` cobre PS (proteção de pipeline/artefato);
`09-monitoramento-resposta/` cobre RV, incluindo o monitoramento de
drift específico de modelos de IA trazido pelo SP 800-218A.
