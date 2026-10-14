#!/usr/bin/env python3
"""Valida los .md antes de publicarlos: nombre, formato y privacidad.

Falla (código 1) si encuentra algo que no debe publicarse en un repositorio público:
correos, teléfonos, direcciones IP, enlaces http(s) fuera de la lista permitida o términos prohibidos
(un nombre por línea en scripts/forbidden_terms.txt).

Uso:  python scripts/validate_docs.py --docs docs
"""
import argparse
import os
import re
import sys

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.(es|en)\.md$")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
URL = re.compile(r"https?://[^\s)>\]]+", re.I)
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
PHONE = re.compile(r"(?<![\w.])\+?\d[\d\s().-]{8,}\d(?![\w.])")
MAX_BYTES = 1_000_000


def strip_comments(text):
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)


def check_file(path, forbidden, allowed_urls):
    problems = []
    name = os.path.basename(path)
    if not NAME.match(name):
        problems.append("nombre no válido (usa <slug>.<es|en>.md)")
    with open(path, "rb") as fh:
        raw = fh.read()
    if len(raw) > MAX_BYTES:
        problems.append("pesa más de %d bytes" % MAX_BYTES)
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append("tiene BOM")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return problems + ["no es UTF-8 válido"]
    body = strip_comments(text).lstrip()
    if not body.startswith("# "):
        problems.append("no empieza con un título «# »")
    if re.search(r"<\s*script", text, re.I):
        problems.append("contiene <script>")
    if EMAIL.search(text):
        problems.append("contiene un correo electrónico")
    for m in URL.finditer(text):
        if not any(m.group(0).startswith(a) for a in allowed_urls):
            problems.append("contiene un enlace no permitido: %s" % m.group(0)[:60])
            break
    if IPV4.search(text):
        problems.append("contiene una dirección IP")
    for m in PHONE.finditer(text):
        if sum(c.isdigit() for c in m.group(0)) >= 10:
            problems.append("parece contener un teléfono")
            break
    low = text.lower()
    for term in forbidden:
        if term in low:
            problems.append("contiene un término prohibido: «%s»" % term)
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--forbidden", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "forbidden_terms.txt"))
    ap.add_argument("--allow-url", action="append", default=[])
    a = ap.parse_args(argv)
    forbidden = []
    if os.path.exists(a.forbidden):
        with open(a.forbidden, encoding="utf-8") as fh:
            forbidden = [l.strip().lower() for l in fh if l.strip() and not l.startswith("#")]
    files = sorted(f for f in os.listdir(a.docs) if f.endswith(".md"))
    if not files:
        print("ERROR: no hay archivos .md en %s" % a.docs)
        return 1
    bad = 0
    for f in files:
        problems = check_file(os.path.join(a.docs, f), forbidden, a.allow_url)
        if problems:
            bad += 1
            print("FALLA  %s" % f)
            for p in problems:
                print("         - %s" % p)
    print("%d archivos revisados, %d con problemas" % (len(files), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
