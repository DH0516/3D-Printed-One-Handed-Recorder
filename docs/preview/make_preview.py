#!/usr/bin/env python3
"""Build the compact 3D preview data for the Model A1 documentation page.

Input: the assembled-model triangle dump (parts with name, color, and a
flat [x,y,z,...] triangle soup in world millimeters, Z up). Output:
docs/preview/viewdata.bin (raw float32 triangles, parts concatenated)
and docs/preview/viewdata-index.json (part name, color, triangle count).

Decimation: parts above 2000 triangles keep every k-th triangle so the
total lands near 130k; small parts are kept whole. Parts removed from
the current design are dropped by name.

Usage: python3 make_preview.py <viewdata.json>
"""
import json
import math
import struct
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
DROP = {"Key_Hole_1_Travel_Stop"}  # removed from the design after the dump


def stride_for(n):
    if n <= 2000:
        return 1
    # keep roughly n/2 up to 30k, then thinner
    return max(2, math.ceil(n / 30000) + 1)


def main():
    src = json.load(open(sys.argv[1]))
    parts, total = [], 0
    chunks = []
    for p in src["parts"]:
        if p["name"] in DROP:
            continue
        t = p["tris"]
        k = stride_for(len(t) // 9)
        kept = []
        for i in range(0, len(t), 9 * k):
            kept.extend(t[i:i + 9])
        parts.append({"name": p["name"], "color": p["color"],
                      "tris": len(kept) // 9})
        chunks.append(kept)
        total += len(kept) // 9
    with open(OUT / "viewdata.bin", "wb") as f:
        for c in chunks:
            f.write(struct.pack("<%df" % len(c), *c))
    (OUT / "viewdata-index.json").write_text(json.dumps(
        {"totalTris": total, "parts": parts}, separators=(",", ":")) + "\n")
    print("parts %d, tris %d, bin %.1f MB"
          % (len(parts), total,
             (OUT / "viewdata.bin").stat().st_size / 1048576))


if __name__ == "__main__":
    main()
