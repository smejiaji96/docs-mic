"""Nombres de archivo estables para cada documento.

Regla única (la usan el generador, la validación y la aplicación, que tiene la misma función en JavaScript):
  1. se quita el texto entre paréntesis;
  2. se quitan acentos y se pasa a minúsculas;
  3. todo lo que no sea letra o número se vuelve «-»;
  4. si dos herramientas quedan con el mismo nombre, se agrega el tipo: -dashboard, -form o -database.
Archivo final:  <slug>.<idioma>.md   (por ejemplo costco-report.es.md)
"""
import re
import unicodedata
from collections import Counter

CENTER_KEY = {"Dashboard": "dashboard", "Form": "form", "Base de datos Excel": "database"}
LANGS = ("es", "en")
SPECIAL = ("full-report", "general-report")


def slugify(name):
    n = re.sub(r"\([^)]*\)", "", name)
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    n = re.sub(r"[^a-zA-Z0-9]+", "-", n).strip("-").lower()
    return n or "documento"


def doc_slugs(tools):
    """tools: lista de (id, nombre, tipo). Devuelve {id: slug}."""
    base = {i: slugify(n) for i, n, c in tools}
    count = Counter(base.values())
    return {i: (base[i] if count[base[i]] == 1 else base[i] + "-" + CENTER_KEY.get(c, "x")) for i, n, c in tools}


def file_name(slug, lang):
    return "%s.%s.md" % (slug, lang)
