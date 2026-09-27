# 3D-Printed-One-Handed-Recorder

An open-source, fully acoustic **one-handed soprano recorder** for players who
use a single hand (upper-limb differences such as hemiplegia, stroke, cerebral
palsy, or congenital limb difference). Home-buildable on a standard desktop
FDM 3D printer with no screws and no bought parts: pivot pins and springs are
cut from 1.75 mm printer filament, and the body mates with any standard plastic
soprano recorder head joint. Chromatic compass C5 to C#7 (26 fingerings) at A = 440.

## Documentation

The [`docs/`](docs/1-index.md) folder is the documentation site (GitHub Pages
+ Jekyll): project overview, background, printing guidelines, assembly
instructions, troubleshooting, and the soprano build guide.

## Interactive fingering chart

[`docs/fingering_viewer.html`](docs/fingering_viewer.html) is a standalone,
client-side fingering chart; open it directly in a browser. Machine-readable
per-model data lives in [`models/`](models/README.md) as `model.json`
(tonehole map plus the full fingering chart), the backend for the per-model
viewer.

## Models

- **A1**, the standard model (OHR-Soprano-v0.1): four printed keys close
  toneholes 1 to 4.
- **A2**: A1 with key 1, the octave lever, moved to the back as a thumb key.

Both models share one fingering chart. Print files are published at first
release.

## Authors

- Design, CAD, and acoustics: **Daniel Ha** (Master's researcher in music
  technology, IDMIL, McGill University).
- Funding, educator workshops, and classroom testing: **Alberto Acquilino**
  (Western University).

## License

Released under the Creative Commons Attribution-NonCommercial 4.0
International License ([CC BY-NC 4.0](LICENSE)). Free for personal, academic,
and non-commercial educational use. Resale, commercial manufacture, or
commercial reproduction requires prior written permission from Daniel Ha.

Generative AI tools assisted with documentation drafting and software
scripting; all CAD models, acoustic designs, and physical prototypes were
created, verified, and directed by the human authors.
