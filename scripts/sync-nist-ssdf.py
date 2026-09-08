#!/usr/bin/env python3
"""Re-baixa a tabela de práticas do NIST SSDF (SP 800-218) e regenera
skills/nist-ssdf/references/{PO,PS,PW,RV}.md.

O NIST não publica a tabela do SP 800-218 em formato estruturado (CSV/
JSON) na própria página — este script usa o mirror mantido pela
Chainguard (github.com/chainguard-dev/self-attestation), que reproduz a
tabela oficial em HTML dentro de um Markdown. Se esse mirror sumir ou
mudar de formato, baixe o PDF oficial e ajuste o parser:
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf

Uso:
    python3 scripts/sync-nist-ssdf.py
"""

import html
import os
import re
import urllib.request
from collections import defaultdict

SOURCE_URL = (
    "https://raw.githubusercontent.com/chainguard-dev/self-attestation/"
    "main/ssdf.md"
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO_ROOT, "skills", "nist-ssdf", "references")

GROUPS = {
    "PO": "Prepare the Organization",
    "PS": "Protect the Software",
    "PW": "Produce Well-Secured Software",
    "RV": "Respond to Vulnerabilities",
}

PRACTICE_RE = re.compile(
    r'<span>([^<]+?)\s*<a id="([A-Z]{2}\.\d+)" href="#\2">\(\2\)</a></span>'
    r'<span>:\s*([^<]+)</span>'
)
TASK_RE = re.compile(
    r'<a id="([A-Z]{2}\.\d+\.\d+)" href="#\1">\1</span><span>:</a>\s*([^<]+)</span>'
)


def fetch(url: str) -> str:
    with urllib.request.urlopen(url) as resp:  # noqa: S310 - trusted mirror
        return resp.read().decode("utf-8")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    text = fetch(SOURCE_URL)

    practices = [
        (pid, html.unescape(title.strip()), html.unescape(desc.strip()))
        for title, pid, desc in PRACTICE_RE.findall(text)
    ]
    tasks: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for tid, desc in TASK_RE.findall(text):
        pid = ".".join(tid.split(".")[:2])
        tasks[pid].append((tid, html.unescape(desc.strip())))

    by_group: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for pid, title, desc in practices:
        by_group[pid.split(".")[0]].append((pid, title, desc))

    for g, gname in GROUPS.items():
        lines = [f"# {g} — {gname}\n"]
        lines.append(
            "Fonte: NIST SP 800-218 (SSDF v1.1), tabela oficial de práticas "
            "(domínio público — publicação do governo dos EUA).\n"
        )
        for pid, title, desc in by_group[g]:
            lines.append(f"## {pid} — {title}\n")
            lines.append(f"{desc}\n")
            lines.append("| Task | Descrição |")
            lines.append("|---|---|")
            for tid, tdesc in tasks.get(pid, []):
                lines.append(f"| {tid} | {tdesc.replace('|', chr(92) + '|')} |")
            lines.append("")

        out_path = os.path.join(OUT_DIR, f"{g}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        n_tasks = sum(len(tasks.get(p[0], [])) for p in by_group[g])
        print(f"synced {g}.md ({len(by_group[g])} practices, {n_tasks} tasks)")

    print("Done. Compare with: git diff skills/nist-ssdf/references")
    print("Note: references/GenAI-profile.md is a hand-written summary, not synced by this script.")


if __name__ == "__main__":
    main()
