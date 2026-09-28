#!/usr/bin/env python3
"""Build the compact 3D preview data for the Model A1 documentation page.

Input: the assembled-model triangle dump (parts with name, color, and a
flat [x,y,z,...] triangle soup in world millimeters, Z up). Output:
docs/preview/viewdata.bin (raw float32 triangles, parts concatenated)
and docs/preview/viewdata-index.json (part name, color, triangle count).

Decimation is vertex clustering: vertices snap to a grid (default
0.5 mm cells) and triangles whose three corners collapse together are
dropped. Surfaces stay closed; small features below the cell size
merge away. Parts removed from the current design are dropped by name.

Usage: python3 make_preview.py <viewdata.json> [cell_mm]
"""
import json
import struct
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
DROP = {"Key_Hole_1_Travel_Stop"}  # removed from the design after the dump


def decimate(tris, cell):
    verts = {}
    out = []
    def vid(x, y, z):
        key = (int(x // cell), int(y // cell), int(z // cell))
        v = verts.get(key)
        if v is None:
            v = len(verts)
            verts[key] = v
        return v
    for i in range(0, len(tris), 9):
        a = vid(*tris[i:i + 3])
        b = vid(*tris[i + 3:i + 6])
        c = vid(*tris[i + 6:i + 9])
        if a != b and b != c and a != c:
            out.extend(tris[i:i + 9])
    # weld each surviving triangle's corners onto the shared cell
    # position (first vertex seen in that cell) for a seamless mesh
    cells = {}
    for key, v in verts.items():
        cells[v] = key
    for i in range(0, len(out), 3):
        v = cells.get(vid(out[i], out[i + 1], out[i + 2]))
        if v is not None:
            k = v
            out[i] = (k[0] + 0.5) * cell
            out[i + 1] = (k[1] + 0.5) * cell
            out[i + 2] = (k[2] + 0.5) * cell
    return out


def main():
    cell = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    src = json.load(open(sys.argv[1]))
    parts, chunks, total = [], [], 0
    for p in src["parts"]:
        if p["name"] in DROP:
            continue
        kept = decimate(p["tris"], cell)
        parts.append({"name": p["name"], "color": p["color"],
                      "tris": len(kept) // 9})
        chunks.append(kept)
        total += len(kept) // 9
    with open(OUT / "viewdata.bin", "wb") as f:
        for c in chunks:
            f.write(struct.pack("<%df" % len(c), *c))
    (OUT / "viewdata-index.json").write_text(json.dumps(
        {"totalTris": total, "parts": parts}, separators=(",", ":")) + "\n")
    print("cell %.2f mm: parts %d, tris %d, bin %.2f MB"
          % (cell, len(parts), total,
             (OUT / "viewdata.bin").stat().st_size / 1048576))


if __name__ == "__main__":
    main()
