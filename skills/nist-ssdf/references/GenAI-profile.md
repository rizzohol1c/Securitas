# Perfil GenAI do SSDF — NIST SP 800-218A

**Título oficial:** *Secure Software Development Practices for Generative
AI and Dual-Use Foundation Models: An SSDF Community Profile* (2024).
Fonte: <https://csrc.nist.gov/pubs/sp/800/218/a/final> · PDF completo:
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf>

> Este arquivo é um **resumo de alto nível**, não uma reprodução verbatim
> do documento (o PDF completo tem práticas, tarefas, recomendações e
> exemplos de implementação detalhados que não foram extraídos aqui).
> Para o texto oficial completo, consulte o PDF acima.

## O que é

SP 800-218A **não substitui** o SSDF (SP 800-218) — ele o estende com
práticas, tarefas, recomendações e referências específicas para
desenvolvimento de modelos de IA generativa e "dual-use foundation
models" ao longo de todo o ciclo de vida de desenvolvimento de software.
Foi criado para apoiar a Executive Order 14110 (EUA) sobre
desenvolvimento seguro de IA.

Público-alvo: produtores de modelos de IA, produtores de sistemas que
usam esses modelos, e organizações que adquirem esses sistemas.

## O que ele acrescenta a cada grupo do SSDF

| Grupo | Prática adicional (resumo) |
|---|---|
| **PO** — Prepare the Organization | Documentar a tolerância a risco e o uso pretendido do modelo/IA antes de começar o desenvolvimento. |
| **PS** — Protect the Software | Proteger dado de treino e artefatos de modelo (pesos, checkpoints, prompts, fine-tunes, embeddings) contra adulteração — não só o código-fonte tradicional. |
| **PW** — Produce Well-Secured Software | Validar a proveniência/linhagem do dado usado no treino, e fazer threat modeling do caminho de inferência (o que entra no modelo, o que sai, quem pode influenciar cada lado). |
| **RV** — Respond to Vulnerabilities | Monitorar o modelo em produção para *behavior drift* — mudança de comportamento do modelo ao longo do tempo, além do monitoramento tradicional de vulnerabilidade de código. |

## Por que importa para vibe coding

Um SaaS que usa um LLM de terceiro (API da Anthropic, OpenAI etc.) ainda
é "produtor de sistema de IA" nesse perfil — mesmo sem treinar modelo
próprio, as práticas de PW (threat model do caminho de inferência: o que
o usuário pode injetar no prompt, o que o modelo pode expor na resposta)
e de RV (monitorar se o comportamento do agente mudou) se aplicam
diretamente.
