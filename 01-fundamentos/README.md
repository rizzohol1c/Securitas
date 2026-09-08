# 01-fundamentos

Conceitos base de segurança: CIA triad, threat modeling, OWASP Top 10
(web), mentalidade de segurança aplicada a vibe coding.

Parte de dois frameworks documentados em
[`00-frameworks-base/`](../00-frameworks-base/README.md):

- [OWASP Top 10](../00-frameworks-base/01-owasp-top10-web.md) — as
  categorias de risco que servem de checklist de arquitetura/código.
- [NIST SSDF](../00-frameworks-base/04-nist-ssdf.md) — o modelo de
  processo (PO/PS/PW/RV) para saber *quando* aplicar cada prática, não só
  o quê.

## CIA triad

Toda vulnerabilidade quebra pelo menos um destes três pilares:

- **Confidencialidade.** Só quem tem permissão consegue ler o dado. Uma
  API que devolve campo de mais (ver
  [`api-response-minimization`](../skills/api-response-minimization/SKILL.md))
  quebra confidencialidade mesmo sem nenhum "hack" — o dado simplesmente
  saiu pra quem não devia ver.
- **Integridade.** O dado é o que deveria ser, sem alteração indevida.
  Um webhook sem verificação de assinatura (ver
  [`webhook-signature-verification`](../skills/webhook-signature-verification/SKILL.md))
  quebra integridade: qualquer um pode forjar um evento como se fosse
  legítimo.
- **Disponibilidade.** O sistema responde quando deveria. Um endpoint
  sem rate limit não é só risco de força bruta — é risco de
  disponibilidade: uma chamada em loop derruba o serviço ou estoura o
  custo da API (denial of wallet).

Ao revisar uma feature, pergunte qual desses três ela pode quebrar antes
de perguntar "isso é seguro?" — a pergunta genérica não leva a lugar
nenhum; a específica leva direto ao controle que falta.

## Threat modeling mínimo

Não precisa de um processo formal para começar. Antes de implementar
qualquer feature que recebe input do usuário ou expõe dado, responda
três perguntas:

1. **Quem pode chamar isso?** Só o dono do dado, qualquer usuário
   autenticado, ou qualquer um na internet sem login?
2. **O que essa pessoa consegue fazer se abusar do input?** Ver dado de
   outro usuário, executar uma ação em nome de outro, ou só causar
   ruído (spam, custo)?
3. **O que acontece se essa chamada vier de fora do frontend** — via
   curl, Postman, ou um agente de IA chamando a API direto? A resposta
   quase sempre revela um controle que só existia na UI, não no
   servidor.

Isso não substitui um threat model completo (STRIDE, attack trees), mas
pega a maioria dos problemas reais de SaaS vibe-coded — que costumam
ser falta do óbvio, não ataque sofisticado.
