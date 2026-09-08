#!/usr/bin/env bash
# Re-baixa o conteúdo oficial do OWASP Top 10 for LLM Applications do
# GitHub e sobrescreve skills/owasp-llm-top10/references/LLM*.md.
#
# Uso:
#   ./scripts/sync-owasp-llm-top10.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$REPO_ROOT/skills/owasp-llm-top10/references"
BASE="https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/2_0_vulns"

mkdir -p "$OUT_DIR"

for n in 01 02 03 04 05 06 07 08 09 10; do
  case $n in
    01) name="PromptInjection" ;;
    02) name="SensitiveInformationDisclosure" ;;
    03) name="SupplyChain" ;;
    04) name="DataModelPoisoning" ;;
    05) name="ImproperOutputHandling" ;;
    06) name="ExcessiveAgency" ;;
    07) name="SystemPromptLeakage" ;;
    08) name="VectorAndEmbeddingWeaknesses" ;;
    09) name="Misinformation" ;;
    10) name="UnboundedConsumption" ;;
  esac
  fname="LLM${n}_${name}"
  curl -sL "${BASE}/${fname}.md" -o "${OUT_DIR}/${fname}.md"
  echo "synced ${fname}.md"
done

echo "Done. Compare with: git diff skills/owasp-llm-top10/references"
