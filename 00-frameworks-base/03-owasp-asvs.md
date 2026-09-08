# OWASP ASVS (Application Security Verification Standard)

**Versão de referência:** ASVS 5.0.0, lançada em maio de 2025 (primeira
major release em seis anos) — reorganizada em 17 capítulos, 346
requisitos. Fonte:
<https://owasp.org/www-project-application-security-verification-standard/>

> 🔧 **Skill instalável:** [`skills/owasp-asvs`](../skills/owasp-asvs/SKILL.md)
> — os 346 requisitos oficiais (CSV publicado pela OWASP), um arquivo
> por capítulo V1–V17, cada requisito com ID e nível (L1/L2/L3),
> atualizável via `scripts/sync-owasp-asvs.py`.

## O que é

Diferente do Top 10 (que é uma lista de riscos para *conscientizar*), o
ASVS é uma lista de **requisitos verificáveis**: cada item é uma
afirmação testável do tipo "o sistema verifica que X" ou "o sistema
rejeita Y". É a ferramenta para transformar "isso aqui precisa ser
seguro" em um checklist que dá para marcar como ✅ ou ❌.

## Os 3 níveis de verificação

| Nível | Para que serve | Perfil de aplicação |
|---|---|---|
| **L1** | Segurança mínima viável, verificável até por pentest automatizado | Qualquer aplicação exposta à internet — piso mínimo |
| **L2** | Padrão recomendado para a maioria dos SaaS | Aplicações que lidam com dados de usuário, pagamento, dado de negócio sensível |
| **L3** | Alto rigor, exige revisão manual aprofundada | Aplicações críticas: financeiro, saúde, dado altamente regulado |

Para um SaaS típico feito por um time pequeno com apoio de IA, **L1 é o
piso inegociável antes de qualquer deploy em produção**; L2 é a meta a
buscar conforme o produto cresce.

## Os 17 capítulos (5.0)

`V1` Encoding and Sanitization · `V2` Validation and Business Logic ·
`V3` Web Frontend Security · `V4` API and Web Service · `V5` File
Handling · `V6` Authentication · `V7` Session Management · `V8`
Authorization · `V9` Self-contained Tokens · `V10` OAuth and OIDC ·
`V11` Cryptography · `V12` Secure Communication · `V13` Configuration ·
`V14` Data Protection · `V15` Secure Coding and Architecture · `V16`
Security Logging and Error Handling · `V17` WebRTC

## Por que importa especificamente em vibe coding

Código gerado por IA tende a "parecer certo" — compila, passa no teste
feliz, a UI funciona. O ASVS é o antídoto para essa falsa sensação de
prontidão: ele obriga a verificar item por item (ex.: "V8.2.1 — a
autorização é verificada no servidor para toda ação sensível, não só na
UI") em vez de confiar na impressão de que "a IA já deve ter feito
direito".

## Como uso isso no repositório

`10-checklists-templates/` traduz os requisitos L1 (e os L2 mais
relevantes para SaaS) em checklists práticos de pré-deploy e de revisão
de código gerado por IA, agrupados pelos mesmos capítulos V1–V17 acima.
