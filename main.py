"""Entry program for the 25 November 2026 news image.

The repository carries the finished front page as entry.png; this
program's whole job is to place those exact bytes at the output
path the harness reads. Standard library only, no network.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUT_DIR, "entry.png")


def digest(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    same_size = os.path.getsize(SOURCE) == os.path.getsize(TARGET)
    if not same_size or digest(SOURCE) != digest(TARGET):
        raise SystemExit("entry.png copy failed verification")


if __name__ == "__main__":
    main()
