#!/usr/bin/env python3
"""Re-baixa o CSV oficial do OWASP ASVS 5.0.0 e regenera
skills/owasp-asvs/references/V1.md ... V17.md.

Uso:
    python3 scripts/sync-owasp-asvs.py

Se a OWASP lançar uma nova versão do ASVS, ajuste CSV_URL abaixo e
confira se as colunas do CSV continuam as mesmas (chapter_id,
chapter_name, section_id, section_name, req_id, req_description, L).
"""

import csv
import io
import os
import urllib.request
from collections import OrderedDict

CSV_URL = (
    "https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/docs_en/"
    "OWASP_Application_Security_Verification_Standard_5.0.0_en.csv"
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO_ROOT, "skills", "owasp-asvs", "references")


def fetch_csv(url: str) -> str:
    with urllib.request.urlopen(url) as resp:  # noqa: S310 - trusted OWASP source
        return resp.read().decode("utf-8")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    raw = fetch_csv(CSV_URL)

    chapters: "OrderedDict[str, dict]" = OrderedDict()
    reader = csv.DictReader(io.StringIO(raw))
    for row in reader:
        cid, cname = row["chapter_id"], row["chapter_name"]
        sid, sname = row["section_id"], row["section_name"]
        rid, desc, lvl = row["req_id"], row["req_description"], row["L"]
        chapters.setdefault(cid, {"name": cname, "sections": OrderedDict()})
        chapters[cid]["sections"].setdefault(sid, {"name": sname, "reqs": []})
        chapters[cid]["sections"][sid]["reqs"].append((rid, lvl, desc))

    for cid, cdata in chapters.items():
        lines = [f"# {cid} — {cdata['name']}\n"]
        lines.append(
            "Fonte: OWASP ASVS 5.0.0 (CC BY-SA 4.0), CSV oficial "
            "`OWASP_Application_Security_Verification_Standard_5.0.0_en.csv`. "
            "Nível `L` = nível de verificação mínimo em que o requisito se aplica (1, 2 ou 3).\n"
        )
        for sid, sdata in cdata["sections"].items():
            lines.append(f"## {sid} — {sdata['name']}\n")
            lines.append("| ID | L | Requisito |")
            lines.append("|---|---|---|")
            for rid, lvl, desc in sdata["reqs"]:
                desc_clean = desc.replace("|", "\\|").replace("\n", " ").strip()
                lines.append(f"| {rid} | {lvl} | {desc_clean} |")
            lines.append("")

        out_path = os.path.join(OUT_DIR, f"{cid}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        n_reqs = sum(len(s["reqs"]) for s in cdata["sections"].values())
        print(f"synced {cid}.md ({n_reqs} requirements)")

    print("Done. Compare with: git diff skills/owasp-asvs/references")


if __name__ == "__main__":
    main()
