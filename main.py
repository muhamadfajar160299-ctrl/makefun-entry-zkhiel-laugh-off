"""Copy the one-line joke in entry.txt (next to this file) byte-identically
to $MAKEFUN_OUTPUT_DIR/entry.txt, mode 0644, with no temp file."""

import os
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")

try:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
except KeyError:
    sys.exit("MAKEFUN_OUTPUT_DIR is not set")

try:
    with open(SRC, "rb") as f:
        data = f.read()
except OSError as exc:
    sys.exit("cannot read entry.txt: %s" % exc)

if not data.strip():
    sys.exit("entry.txt is empty")

os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
try:
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
except OSError as exc:
    sys.exit("cannot write output: %s" % exc)
