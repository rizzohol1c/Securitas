#!/usr/bin/env bash
# Re-baixa o conteúdo oficial do OWASP Top 10:2025 (aplicações web) do
# GitHub e sobrescreve skills/owasp-top10-web/references/A0*.md.
#
# Uso:
#   ./scripts/sync-owasp-top10-web.sh
#
# Depois de rodar, revise o diff (`git diff skills/owasp-top10-web`) —
# a OWASP pode ter reestruturado seções ou trocado o nome de um arquivo,
# o que quebraria o mapeamento abaixo.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$REPO_ROOT/skills/owasp-top10-web/references"
BASE="https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en"

mkdir -p "$OUT_DIR"

declare -A FILES=(
  [A01]="A01_2025-Broken_Access_Control"
  [A02]="A02_2025-Security_Misconfiguration"
  [A03]="A03_2025-Software_Supply_Chain_Failures"
  [A04]="A04_2025-Cryptographic_Failures"
  [A05]="A05_2025-Injection"
  [A06]="A06_2025-Insecure_Design"
  [A07]="A07_2025-Authentication_Failures"
  [A08]="A08_2025-Software_or_Data_Integrity_Failures"
  [A09]="A09_2025-Security_Logging_and_Alerting_Failures"
  [A10]="A10_2025-Mishandling_of_Exceptional_Conditions"
)

for id in "${!FILES[@]}"; do
  curl -sL "${BASE}/${FILES[$id]}.md" -o "${OUT_DIR}/${id}.md"
  echo "synced ${id}.md"
done

echo "Done. Compare with: git diff skills/owasp-top10-web/references"
