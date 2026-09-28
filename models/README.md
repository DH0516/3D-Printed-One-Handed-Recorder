# Model data

Each model directory holds `model.json`, the machine-readable backend for the
interactive fingering viewer: the complete tonehole map plus the full chromatic
fingering chart. These files are generated from the project's CAD model; if a
number looks wrong, please open an issue rather than editing the JSON. The
viewer embeds a generated minimal projection of the same data (station ids,
types, key names, layout, fingerings), so the page works with no server at
all.

## Schema `ohr-model/1`

Top level:

- `id`, `name`, `description`: model identity.
- `layout`: optional. Station ids in top-to-bottom diagram order (a double
  hole is its base id). This is physical placement only; the fingering chart
  itself maps each hole id the same way regardless of layout.
- `pitch`: `reference` (tuning standard), `lowest`, `highest`.
- `holes`: one entry per tonehole.
- `fingerings`: one entry per chromatic note.

Hole entry fields:

- `id`: hole name used everywhere in the project (`1` to `6`, `7L`, `7R`, `8L`, `8R`).
- `part`: `body` or `foot` joint.
- `type`: `key` (a printed key closes this hole) or `finger_hole`.
- `key`: which printed key operates the hole, present when `type` is `key`.
- `z`: station of the hole along the bore, millimeters.
- `angle`: bearing of the hole around the bore axis, degrees.
- `diameter`: drilled diameter, millimeters.
- `offset`: lateral shift of the drill axis along the tangent, double holes only.

Fingering entry fields:

- `note`: chromatic note name, `C5` through `C#7`.
- `holes`: map of every hole id to `C` (closed), `O` (open), or `H` (half-hole).

## Units and bearings

All lengths are millimeters. `z` runs from the head-joint tenon end of the
body toward the bell. Bearings are taken verbatim from the CAD tables: the
finger holes under the operating hand sit at +90, the keyed holes for the
missing hand's fingers sit near 0 to -60 at the front, and the back of the
instrument is near 180 (the A2 thumb key's hole 1 sits at -103.6).

## Models

- [`A1-2/`](A1-2/): the soprano model in two physical variants, A1 (Key 1 in
  the key cluster) and A2 (Key 1 at the back as a thumb key). One shared
  fingering chart.
