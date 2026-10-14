#!/usr/bin/env python3
"""Arma lo que se publica en la release: los .md planos, un .zip por idioma y el manifiesto con enlaces.

Uso:
  python scripts/build_assets.py --docs docs --out dist --owner OWNER --repo REPO [--branch main] [--tag docs] [--raw-dir docs]
"""
import argparse
import hashlib
import json
import os
import shutil
import sys
import zipfile
from datetime import datetime, timezone


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--out", default="dist")
    ap.add_argument("--owner", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--branch", default="main")
    ap.add_argument("--tag", default="docs")
    ap.add_argument("--raw-dir", default="docs", help="carpeta de los .md DENTRO del repositorio (para los enlaces raw)")
    ap.add_argument("--timestamp", default=None, help="fecha ISO fija (para pruebas)")
    a = ap.parse_args(argv)

    names = sorted(f for f in os.listdir(a.docs) if f.endswith(".md"))
    if not names:
        print("ERROR: no hay .md en %s" % a.docs)
        return 1
    if os.path.isdir(a.out):
        shutil.rmtree(a.out)
    os.makedirs(a.out)
    for n in names:
        shutil.copy2(os.path.join(a.docs, n), os.path.join(a.out, n))
    for lang in ("es", "en"):
        group = [n for n in names if n.endswith(".%s.md" % lang)]
        if group:
            with zipfile.ZipFile(os.path.join(a.out, "mic-docs-%s.zip" % lang), "w", zipfile.ZIP_DEFLATED) as z:
                for n in group:
                    z.write(os.path.join(a.docs, n), n)

    base_dl = "https://github.com/%s/%s/releases/download/%s/" % (a.owner, a.repo, a.tag)
    base_raw = "https://raw.githubusercontent.com/%s/%s/%s/%s/" % (a.owner, a.repo, a.branch, a.raw_dir.strip("/"))
    files = []
    for n in sorted(os.listdir(a.out)):
        p = os.path.join(a.out, n)
        item = {"name": n, "bytes": os.path.getsize(p), "sha256": sha256(p), "download_url": base_dl + n}
        if n.endswith(".md"):
            item["raw_url"] = base_raw + n
        files.append(item)
    manifest = {"generated": a.timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "repository": "%s/%s" % (a.owner, a.repo), "branch": a.branch, "release_tag": a.tag, "files": files}
    with open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("%d archivos en %s (incluye 2 zips y manifest.json)" % (len(files), a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
