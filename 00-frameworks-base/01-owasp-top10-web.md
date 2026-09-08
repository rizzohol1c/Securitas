# OWASP Top 10 (aplicações web)

**Versão de referência:** OWASP Top 10:2025 (lista final publicada em
janeiro de 2026, anunciada no Global AppSec de novembro de 2025).
Substitui a edição de 2021. Fonte: <https://owasp.org/Top10/2025/>

> 🔧 **Skill instalável:** [`skills/owasp-top10-web`](../skills/owasp-top10-web/SKILL.md)
> — espelha o texto oficial completo (A01–A10: background, CWEs,
> prevenção, cenários de ataque) direto do repositório da OWASP, via
> `scripts/sync-owasp-top10-web.sh`. Este arquivo aqui é só o resumo e o
> porquê de importar para vibe coding; o conteúdo integral vive na skill,
> não é reescrito à mão aqui.

## O que é

Documento de conscientização mantido pela OWASP com as 10 categorias de
risco mais críticas em aplicações web, baseado em dados reais (mais de
175 mil CVEs analisados e centenas de CWEs mapeados) e em pesquisas com
praticantes de segurança. Não é uma lista fechada de bugs — são
*categorias* de falha.

## As 10 categorias (2025)

| ID | Categoria | O que significa na prática |
|---|---|---|
| A01 | **Broken Access Control** | Usuário consegue acessar dado/ação que não deveria (inclui SSRF, que foi absorvido aqui em 2025) |
| A02 | **Security Misconfiguration** | Configuração insegura por padrão: CORS aberto demais, debug ligado em produção, permissões de bucket/storage erradas |
| A03 | **Software Supply Chain Failures** | Categoria nova em 2025: falhas na cadeia de build/distribuição/atualização de software (pacotes comprometidos, pipelines inseguros) |
| A04 | **Cryptographic Failures** | Dado sensível sem criptografia adequada em trânsito ou repouso, uso de algoritmo fraco |
| A05 | **Injection** | SQL/NoSQL/OS command/XSS — entrada não sanitizada interpretada como código |
| A06 | **Insecure Design** | Falha estrutural de arquitetura/threat modeling, não um bug de implementação |
| A07 | **Authentication Failures** | Login, sessão e recuperação de senha implementados de forma fraca |
| A08 | **Software or Data Integrity Failures** | Confiar em atualizações, plugins ou dados sem verificar integridade (ex.: CI/CD sem assinatura, deserialização insegura) |
| A09 | **Security Logging and Alerting Failures** | Sem log/alerta suficiente para detectar e responder a um incidente a tempo |
| A10 | **Mishandling of Exceptional Conditions** | Categoria nova em 2025: erros, exceptions e casos de borda tratados de forma que expõe dado ou quebra a lógica de segurança |

## Por que importa especificamente em vibe coding

- **A02 e A03** são os que mais aparecem em SaaS gerado rapidamente com IA:
  a IA sugere configurações "que funcionam" (CORS `*`, chave pública
  exposta no client) e pacotes npm/pip sem que ninguém audite a origem.
- **A05 (Injection)** continua comum quando a IA monta queries por
  concatenação de string em vez de usar bindings/ORM parametrizado.
- **A06 (Insecure Design)** é o risco mais fácil de ignorar em vibe coding:
  a IA resolve o pedido literal ("crie um endpoint que retorna o pedido
  pelo ID"), não o problema de segurança implícito ("...só para o dono do
  pedido").
- **A10** é novo e relevante: código gerado por IA tende a tratar o
  caminho feliz muito bem e o `catch`/exceção de forma genérica, às vezes
  vazando stack trace ou dado sensível na resposta de erro.

## Como uso isso no repositório

Serve de checklist de arquitetura/código para `01-fundamentos/`,
`02-autenticacao-autorizacao/`, `05-dependencias-supply-chain/` e
`06-infraestrutura-cloud/`. O ASVS (`03-owasp-asvs.md`) detalha cada
categoria acima em requisitos verificáveis linha a linha.
