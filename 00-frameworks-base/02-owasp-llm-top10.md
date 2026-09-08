# OWASP Top 10 for LLM Applications

**Versão de referência:** 2025, v2.0 — mantida pelo OWASP GenAI Security
Project. Fonte: <https://genai.owasp.org/>

> 🔧 **Skill instalável:** [`skills/owasp-llm-top10`](../skills/owasp-llm-top10/SKILL.md)
> — um arquivo por risco (LLM01–LLM10: descrição, subtipos, mitigação,
> cenário de ataque), atualizável via `scripts/sync-owasp-llm-top10.sh`.

## O que é

Equivalente ao Top 10 tradicional, mas para riscos que só existem — ou
ficam muito piores — porque há um modelo de linguagem no meio do
sistema: agente, chatbot, pipeline RAG, ou qualquer feature que manda
texto do usuário para um LLM e faz algo com a resposta.

## Os 10 riscos (2025 v2.0)

| ID | Risco | O que significa na prática |
|---|---|---|
| LLM01 | **Prompt Injection** | Entrada (direta do usuário ou indireta, via documento/site que o modelo lê) sobrescreve o comportamento pretendido do prompt |
| LLM02 | **Sensitive Information Disclosure** | PII, credenciais ou dado proprietário vaza pelo prompt, pelos dados de treino/contexto ou pela resposta do modelo |
| LLM03 | **Supply Chain** | Modelo pré-treinado, adapter (LoRA), dataset ou plataforma de deploy comprometidos |
| LLM04 | **Data and Model Poisoning** | Dado de treino/fine-tuning/embedding manipulado introduz viés ou backdoor no modelo |
| LLM05 | **Improper Output Handling** | Saída do LLM é usada sem sanitizar em shell, banco, browser — abre XSS, SSRF ou execução de comando |
| LLM06 | **Excessive Agency** | Agente com permissões, ferramentas ou autonomia amplas demais realiza ações não pretendidas |
| LLM07 | **System Prompt Leakage** | System prompt guarda segredo (chave, regra de negócio) que não deveria depender de "ficar escondido" |
| LLM08 | **Vector and Embedding Weaknesses** | Específico de RAG: injeção via conteúdo recuperado, inversão de embedding, falha de controle de acesso no índice vetorial |
| LLM09 | **Misinformation** | Resposta errada mas confiante (alucinação) é usada a jusante como se fosse fato |
| LLM10 | **Unbounded Consumption** | Volume de inferência sem limite — custo ou negação de serviço ("denial of wallet") |

## Por que importa especificamente em vibe coding

- **LLM06 (Excessive Agency)** é o risco nº 1 em SaaS vibe-coded com
  agentes: é comum copiar um exemplo de tool-calling da documentação e dar
  ao agente acesso de escrita/delete "porque funcionou no teste".
- **LLM01 (Prompt Injection)** aparece assim que o produto lê conteúdo
  externo (e-mail, site, PDF de upload) e passa para o modelo — muito
  comum em features de "IA que resume seus dados".
- **LLM02 e LLM07** acontecem quando a IA que *escreveu* o código também
  escreveu o system prompt com dados de exemplo reais, ou quando o prompt
  vira o único lugar onde uma regra de negócio sensível é aplicada.
- **LLM10** é fácil de esquecer no MVP: sem rate limit por usuário, uma
  chamada em loop (bug ou abuso) vira uma conta alta da API do modelo.

## Como uso isso no repositório

Detalhado em `04-seguranca-llm-ia/`, um arquivo por risco (LLM01–LLM10),
seguindo a mesma estrutura da skill: descrição, subtipos, mitigação,
cenário de ataque de exemplo. Itens de agente (LLM06) cruzam com
`02-autenticacao-autorizacao/` (permissão/least privilege) e itens de RAG
(LLM08) cruzam com `06-infraestrutura-cloud/` (controle de acesso ao
vetor store).
