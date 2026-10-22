"""Mechanical protected-element check: frozen raw section vs edited section.

Compares, as multisets: headings, table rows, caption lines, fenced code
blocks, parenthetical citations, narrative citations, double-quoted strings,
numbers/identifiers, and prose dashes added. Exact matches catch changes to
protected material; they do not prove meaning was preserved.

Usage: python check_protected.py RAW_DIR EDITED_DIR
"""
import collections
import os
import re
import sys

FILES = ["00-executive-summary.md", "01-introduction.md", "02-methodology.md",
         "03-quality-assurance.md", "04-ivv.md", "references.md"]


def parts(text):
    code = re.findall(r"```.*?```", text, flags=re.S)
    prose = re.sub(r"```.*?```", " ", text, flags=re.S)
    prose = re.sub(r"<!--.*?-->", " ", prose, flags=re.S)
    lines = prose.splitlines()
    tables = [l.strip() for l in lines if l.strip().startswith("|")]
    body = "\n".join(l for l in lines if not l.strip().startswith("|"))
    return {
        "headings": [l.strip() for l in lines if l.startswith("#")],
        "table rows": tables,
        "captions": [l.strip() for l in lines if re.match(r"^\*(Figure|Table) ", l.strip())],
        "code blocks": code,
        "parenthetical citations": re.findall(r"\([^()]*?(?:\d{4}[a-d]?|n\.d\.(?:-[a-k])?)(?:, (?:p|pp|para)\. [^)]*|, [A-Z][^)]*section|, Abstract)?\)", body),
        "narrative citations": re.findall(r"[A-Z][A-Za-z]+(?: et al\.| and [A-Z][a-z]+)? \((?:\d{4}[a-d]?|n\.d\.)[^)]*\)", body),
        "quotations": re.findall(r'"[^"\n]{3,}"', body),
        "numbers/identifiers": re.findall(r"\b(?:GHSA-[\w-]+|CVSS \d+(?:\.\d+)?|\d+(?:[.,]\d+)*%?)", body),
        "prose dashes": re.findall(r"[—–]", re.sub(r"\d[–]\d", "", body)),
    }


def compare(raw_dir, edit_dir):
    failures = 0
    for name in FILES:
        a_path, b_path = os.path.join(raw_dir, name), os.path.join(edit_dir, name)
        if not os.path.exists(b_path):
            print(f"MISSING {b_path}")
            failures += 1
            continue
        a = parts(open(a_path, encoding="utf-8").read())
        b = parts(open(b_path, encoding="utf-8").read())
        for key in a:
            ca, cb = collections.Counter(a[key]), collections.Counter(b[key])
            if key == "prose dashes":
                if sum(cb.values()) > sum(ca.values()):
                    print(f"{name}: {key}: {sum(ca.values())} -> {sum(cb.values())}")
                    failures += 1
                continue
            lost, added = ca - cb, cb - ca
            if lost or added:
                failures += 1
                print(f"{name}: {key} differ")
                for x in lost:
                    print(f"   - {x[:140]!r} x{lost[x]}")
                for x in added:
                    print(f"   + {x[:140]!r} x{added[x]}")
    print(f"\n{failures} check group(s) with differences")


if __name__ == "__main__":
    compare(sys.argv[1], sys.argv[2])
