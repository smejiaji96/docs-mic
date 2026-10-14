#!/usr/bin/env python3
"""Comprueba que el reporte completo y los archivos individuales dicen EXACTAMENTE lo mismo.

Para cada idioma:
  - full-report debe contener, palabra por palabra, el archivo de cada herramienta;
  - full-report debe contener cada sección del reporte general;
  - es y en deben tener las mismas herramientas.
Si algo no coincide, la publicación se detiene (así nunca hay un archivo individual más nuevo que el consolidado, o al revés).

Uso:  python scripts/check_consistency.py --docs docs
"""
import argparse
import os
import re
import sys

SPECIAL = ("full-report", "general-report")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def clean(text):
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S).strip()


def check(docs):
    problems = []
    slugs = {}
    for lang in ("es", "en"):
        suffix = ".%s.md" % lang
        files = sorted(f for f in os.listdir(docs) if f.endswith(suffix))
        tools = [f for f in files if f[: -len(suffix)] not in SPECIAL]
        slugs[lang] = {f[: -len(suffix)] for f in tools}
        full_name, general_name = "full-report" + suffix, "general-report" + suffix
        if full_name not in files or general_name not in files:
            problems.append("[%s] faltan full-report o general-report" % lang)
            continue
        full = clean(read(os.path.join(docs, full_name)))
        for f in tools:
            if clean(read(os.path.join(docs, f))) not in full:
                problems.append("[%s] %s no coincide con lo que dice %s" % (lang, f, full_name))
        general = clean(read(os.path.join(docs, general_name)))
        sections = [s.strip() for s in general.split("\n---\n")][1:]      # la primera parte es el título y el índice
        for i, s in enumerate(sections, 1):
            if s and s not in full:
                problems.append("[%s] la sección %d de %s no está igual en %s" % (lang, i, general_name, full_name))
    if "es" in slugs and "en" in slugs and slugs["es"] != slugs["en"]:
        diff = sorted(slugs["es"] ^ slugs["en"])
        problems.append("es y en no tienen las mismas herramientas: %s" % ", ".join(diff))
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    a = ap.parse_args(argv)
    problems = check(a.docs)
    for p in problems:
        print("FALLA", p)
    print("Coherencia entre individuales y consolidado: %s" % ("CON PROBLEMAS (%d)" % len(problems) if problems else "correcta"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
