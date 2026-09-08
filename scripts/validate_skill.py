#!/usr/bin/env python3
"""Valida skills contra a spec agentskills.io + convenções deste repo.

Sem dependências externas (sem PyYAML) — o frontmatter deste repo é
simples o bastante para um parser manual. Se algum dia o frontmatter
ficar mais complexo, troque por um parser YAML de verdade.

Uso:
    python3 scripts/validate_skill.py skills/*/
    python3 scripts/validate_skill.py skills/login-rate-limiting

Saída: um resultado por skill. Sai com código 1 se qualquer skill falhar
em uma regra obrigatória (spec). Regras de convenção do repo (taxonomia)
geram aviso, não falha —úteis para PR review, não bloqueiam CI sozinhas.
"""

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SKILL_REF_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`")
ALLOWED_TYPES = {"framework-mirror", "vulnerability-pattern"}


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]

    data: dict = {}
    current_map_key = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current_map_key:
            key, _, value = line.strip().partition(":")
            data.setdefault(current_map_key, {})[key.strip()] = value.strip().strip('"')
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        key = key.strip()
        value = value.strip().strip('"')
        if value == "":
            current_map_key = key
            data[key] = {}
        else:
            current_map_key = None
            data[key] = value
    return data


def referenced_skill_names(body: str) -> set[str]:
    """Extrai nomes tipo-skill citados em backtick na seção '## Relacionado'.

    Heurística, não parser de markdown: pega o texto da primeira seção
    '## Relacionado' até o próximo '## ' (ou fim do arquivo) e coleta
    tokens entre backtick que batem com o formato de nome de skill
    (minúsculas/números/hífen). Filtra o resto por construção — termos
    com maiúscula, ponto ou parênteses (ex.: `HttpOnly`, `err.message`,
    `.pick()`) não casam com o regex.
    """
    match = re.search(r"^## Relacionado\s*$(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not match:
        return set()
    return set(SKILL_REF_RE.findall(match.group(1)))


def validate_skill(skill_dir: Path, all_skill_names: set[str] | None = None) -> list[str]:
    errors = []
    warnings = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return [f"FAIL missing SKILL.md in {skill_dir}"]

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return [f"FAIL {skill_dir.name}: SKILL.md has no valid frontmatter block"]

    # --- spec-required checks (agentskills.io) ---
    name = fm.get("name")
    if not name:
        errors.append("missing required field 'name'")
    else:
        if len(name) > 64:
            errors.append(f"'name' exceeds 64 chars ({len(name)})")
        if not NAME_RE.match(name):
            errors.append(f"'name' ({name!r}) must be lowercase letters/digits/hyphens, no leading/trailing/double hyphen")
        if name != skill_dir.name:
            errors.append(f"'name' ({name!r}) must match directory name ({skill_dir.name!r})")

    description = fm.get("description")
    if not description:
        errors.append("missing required field 'description'")
    elif len(description) > 1024:
        errors.append(f"'description' exceeds 1024 chars ({len(description)})")

    # --- repo convention checks (taxonomy) — warnings, not hard failures ---
    if not fm.get("license"):
        warnings.append("no 'license' field set (repo convention expects one)")

    metadata = fm.get("metadata")
    if not isinstance(metadata, dict) or not metadata:
        warnings.append("no 'metadata' block (repo convention expects type/domain)")
    else:
        skill_type = metadata.get("type")
        if skill_type not in ALLOWED_TYPES:
            warnings.append(f"metadata.type {skill_type!r} not in {sorted(ALLOWED_TYPES)}")
        if not metadata.get("domain"):
            warnings.append("metadata.domain not set")

    if all_skill_names is not None:
        referenced = referenced_skill_names(text) - {skill_dir.name}
        dangling = sorted(referenced - all_skill_names)
        for ref in dangling:
            warnings.append(f"'Relacionado' references unknown skill `{ref}`")

    label = skill_dir.name
    out = [f"FAIL {label}: {e}" for e in errors] + [f"WARN {label}: {w}" for w in warnings]
    if not errors and not warnings:
        out = [f"PASS {label}"]
    elif not errors:
        out.insert(0, f"PASS {label} (with warnings)")
    return out


def main(argv: list[str]) -> int:
    if not argv:
        print("uso: validate_skill.py <skill-dir> [<skill-dir> ...]", file=sys.stderr)
        return 2

    dirs = [Path(raw) for raw in argv if Path(raw).is_dir()]
    # Nomes de referência para checar links cruzados só fazem sentido
    # quando o repo inteiro (ou pelo menos skills/*) é passado de uma vez
    # — com uma skill isolada, all_skill_names fica {ela mesma} e a
    # checagem não teria com o que comparar, então é pulada nesse caso.
    all_names = {d.name for d in dirs}
    check_refs = len(dirs) > 1

    had_error = False
    for d in dirs:
        for line in validate_skill(d, all_names if check_refs else None):
            print(line)
            if line.startswith("FAIL"):
                had_error = True

    return 1 if had_error else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
