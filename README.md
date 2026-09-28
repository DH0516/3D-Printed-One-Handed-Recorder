# 3D-Printed-One-Handed-Recorder

An open-source, fully acoustic **one-handed soprano recorder** for players who use a single hand (upper-limb differences such as hemiplegia, stroke, cerebral palsy, or congenital limb difference). Home-buildable on a standard desktop FDM 3D printer with no screws and no bought parts: pivot pins and springs are cut from 1.75 mm printer filament, and the body mates with any standard plastic soprano recorder head joint. Chromatic compass C5 to C#7 (26 fingerings) at A = 440.

## Documentation

The [`docs/`](docs/1-index.html) folder is the documentation site, served by GitHub Pages as plain static HTML (`.nojekyll`): project overview, background, printing guidelines, assembly instructions, troubleshooting, and the soprano build guide. Edit the `.md` chapters, then run `python3 docs/render.py` to regenerate the `.html` pages.

## Interactive fingering chart

[`docs/fingering_viewer.html`](docs/fingering_viewer.html) is a standalone, client-side fingering chart with a model selector, showing a simplified instrument diagram per note. It is fully static: the model list comes from `models/manifest.json` and each model's data from its `model.json`, so serve the folder on any static host.

## Models

- **A1**: 4-key system. Key 1 (index finger/octave) sits at the front top with Keys 2 to 4 that lies between the bottom holes. 
- A2: Key 1, the octave key, moves to the back of the body as an actual thumb key. Both Model A variants share the same keys, finger holes, and fingering chart.

## Authors

- Design, CAD, printing, acoustics, and documentations: **Daniel Ha** (Master's researcher in music technology, CAML, McGill University).
- Funding and publication: **Alberto Acquilino**(Western University).

## License

Released under the Creative Commons Attribution-NonCommercial 4.0 International License ([CC BY-NC 4.0](LICENSE)). Free for personal, academic, and non-commercial educational use. Resale, commercial manufacture, or commercial reproduction requires prior written permission from Daniel Ha.

Generative AI tools assisted with documentation drafting and software scripting; all CAD models, acoustic designs, and physical prototypes were created, verified, and directed by the human authors.
