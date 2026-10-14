#!/usr/bin/env python3
"""Comprueba, SIN autenticación, que cada enlace del manifiesto responde y que la descarga es directa.

- download_url: debe responder 200 y traer Content-Disposition: attachment (la descarga empieza sola).
- raw_url: debe responder 200 (muestra el texto en el navegador; no fuerza la descarga).

Uso:
  python scripts/check_public_urls.py --manifest dist/manifest.json [--retries 6 --wait 10]
  python scripts/check_public_urls.py --manifest dist/manifest.json --rewrite https://github.com=http://localhost:8090   (pruebas)
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mic-docs-check"})   # sin cookies ni token
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, {k.lower(): v for k, v in r.getheaders()}, r.read(2048)
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}, b""
    except Exception as e:
        return 0, {"error": str(e)}, b""


def check(item, rewrite, retries, wait):
    problems = []
    for kind in ("download_url", "raw_url"):
        url = item.get(kind)
        if not url:
            continue
        for old, new in rewrite:
            url = url.replace(old, new)
        for attempt in range(retries + 1):
            st, h, _ = fetch(url)
            ok = st == 200 and (kind == "raw_url" or h.get("content-disposition", "").lower().startswith("attachment"))
            if ok or attempt == retries:
                break
            time.sleep(wait)          # GitHub tarda unos segundos en publicar
        if not ok:
            why = "HTTP %s" % st if st != 200 else "sin Content-Disposition: attachment"
            problems.append("%s %s (%s)" % (kind, item["name"], why))
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--retries", type=int, default=0)
    ap.add_argument("--wait", type=float, default=5)
    ap.add_argument("--rewrite", action="append", default=[], help="VIEJO=NUEVO para probar contra un servidor local")
    a = ap.parse_args(argv)
    rewrite = [tuple(r.split("=", 1)) for r in a.rewrite]
    with open(a.manifest, encoding="utf-8") as fh:
        manifest = json.load(fh)
    bad = []
    for item in manifest["files"]:
        bad += check(item, rewrite, a.retries, a.wait)
    for b in bad:
        print("FALLA", b)
    print("%d archivos comprobados, %d problemas" % (len(manifest["files"]), len(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
