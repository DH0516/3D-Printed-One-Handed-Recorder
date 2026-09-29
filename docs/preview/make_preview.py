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

Usage: python3 make_preview.py <viewdata.json> [cell_mm] [variant]
       variant A1 (default) writes viewdata.*; A2 rotates the key-1
       group by the design delta and writes viewdata-A2.*
"""
import json
import math
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


# A2 is A1 with the key-1 group rigidly rotated about the bore axis
# (the documented design delta: -213.6 deg, hole 1 from 110 to -103.6).
A2_ROTATE = {
    "Hole_1_Mount", "Hole_1_Bushing_Rim", "Hole_1_Vent_Plug",
    "Key_Hole_1_Pad_Cup", "Key_Hole_1_Lever", "Key_Hole_1_Hole",
    "Saddle_Hole_1", "Pin_Hole_1",
}
A2_ANGLE_DEG = -213.6


def rotate_z(tris, deg):
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    out = list(tris)
    for i in range(0, len(out), 3):
        x, y = out[i], out[i + 1]
        out[i] = x * c - y * s
        out[i + 1] = x * s + y * c
    return out



def load_stl(path):
    data = path.read_bytes()
    n = struct.unpack('<I', data[80:84])[0]
    assert len(data) == 84 + n * 50, path
    tris = []
    for i in range(n):
        off = 84 + i * 50 + 12
        for v in range(3):
            tris.extend(struct.unpack('<3f', data[off + v * 12:off + v * 12 + 12]))
    return tris


def build_stl_set(model, cell=0.35):
    """Preview built from the shipped print-set STLs themselves, laid out
    in a row on the print bed (part orientation exactly as printed)."""
    parts_dir = OUT.parent.parent / 'models' / model / 'parts'
    order = ['Body', 'Foot', 'Key_1', 'Key_2', 'Key_3', 'Key_4']
    color = {'Body': '#C9BFA8', 'Foot': '#C9BFA8', 'Key_1': '#4169E1',
             'Key_2': '#8B0000', 'Key_3': '#8B0000', 'Key_4': '#8B0000'}
    parts, chunks, total = [], [], 0
    xslot = 0.0
    for name in order:
        f = parts_dir / ('%s-%s.stl' % (model, name))
        tris = decimate(load_stl(f), cell)
        xs = tris[0::3]; zs = tris[2::3]
        w = max(xs) - min(xs)
        # sit the part on the bed (y=0) and space slots along x
        ymin = min(tris[1::3]); xmin = min(xs)
        for i in range(0, len(tris), 3):
            tris[i] += xslot - xmin
            tris[i + 1] -= ymin
        parts.append({'name': '%s-%s' % (model, name), 'color': color[name],
                      'tris': len(tris) // 9})
        chunks.append(tris)
        total += len(tris) // 9
        xslot += w + 25.0
    stem = 'viewdata-stlset-%s' % model
    with open(OUT / (stem + '.bin'), 'wb') as fh:
        for c in chunks:
            fh.write(struct.pack('<%df' % len(c), *c))
    (OUT / (stem + '-index.json')).write_text(json.dumps(
        {'totalTris': total, 'parts': parts}, separators=(',', ':')) + '\n')
    print('%s stlset: parts %d, tris %d, bin %.2f MB'
          % (model, len(parts), total,
             (OUT / (stem + '.bin')).stat().st_size / 1048576))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--stlset':
        build_stl_set(sys.argv[2] if len(sys.argv) > 2 else 'A2',
                      float(sys.argv[3]) if len(sys.argv) > 3 else 0.35)
        return
    cell = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    variant = sys.argv[3] if len(sys.argv) > 3 else "A1"
    stem = "viewdata" if variant == "A1" else "viewdata-A2"
    src = json.load(open(sys.argv[1]))
    parts, chunks, total = [], [], 0
    for p in src["parts"]:
        if p["name"] in DROP:
            continue
        tris = p["tris"]
        if variant == "A2" and p["name"] in A2_ROTATE:
            tris = rotate_z(tris, A2_ANGLE_DEG)
        kept = decimate(tris, cell)
        parts.append({"name": p["name"], "color": p["color"],
                      "tris": len(kept) // 9})
        chunks.append(kept)
        total += len(kept) // 9
    with open(OUT / (stem + ".bin"), "wb") as f:
        for c in chunks:
            f.write(struct.pack("<%df" % len(c), *c))
    (OUT / (stem + "-index.json")).write_text(json.dumps(
        {"totalTris": total, "parts": parts}, separators=(",", ":")) + "\n")
    print("%s cell %.2f mm: parts %d, tris %d, bin %.2f MB"
          % (variant, cell, len(parts), total,
             (OUT / (stem + ".bin")).stat().st_size / 1048576))


if __name__ == "__main__":
    main()
