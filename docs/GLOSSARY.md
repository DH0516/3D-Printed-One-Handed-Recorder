# One-Handed Recorder Project Dictionary and Glossary

This document defines the authorized vocabulary for the One-Handed Recorder project. It enforces the rules from the repository glossary skill (`.agents/skills/glossary/SKILL.md`) to prevent vocabulary drift, eliminate jargon, and prevent made-up terms.

---

## 1. Authority Hierarchy

When writing code, documentation, proposals, or communications, words must follow this strict priority:

1. **The User's Own Messages:** The user's vocabulary is the highest authority for this domain (for example, the male pivot stub is the "insert" in prose).
2. **`cad/NAMING.md` / `cad/naming.py`:** Pre-defined terms classified as `maker` (woodwind maker term), `eng` (mechanical engineering), or `ours` (project-specific term).
3. **Existing Code Identifiers:** Exact variable names and comments in the existing scripts.
4. **Directly Cited Sources:** Exact terminology from referenced publications (for example, Inria Openwind, FLOW project).

**Strict Rule:** Never introduce an acronym, shorthand, category name, or external jargon not found in the sources above. If no authorized term exists, describe the physical thing in a plain sentence.

---

## 2. Authorized Project Vocabulary

### The Instrument and Major Sections
* **the body** (*maker*): The middle tube of the recorder, carrying the toneholes, mounts, tone hole rims, octave hole, six pillars, and the pin slot.
* **the foot joint** (*maker*): The lower bell end of the instrument, printed separately and fitted on the bore axis with paper tape, thread, O-ring, or cork.
* **head joint** (*maker*): The mouthpiece and fipple section. The recorder is engineered to mate with any standard commercial 440 Hz Yamaha soprano recorder head (no specific model numbers).
* **key 1** (*maker*): The octave thumb key on the back of the body, rocking on a 1.75 mm filament cross pin in the pin slot. Resting position keeps the octave hole closed; thumb press opens it.
* **keys 2 to 4** (*maker*): The three front articulated finger keys. Each key is named strictly for the tonehole it covers, never for the finger that presses it.

### Keywork Anatomy
* **pillar** (*user*): The extruding post on the body that receives the key.
* **pillar slot** (*user*): The open slot in the pillar into which the key bracket snaps.
* **bracket** (*user*): The actual insert part on the key shaft that snaps into the pillar slot.
* **touchpiece** (*user* / *maker*): The button/key surface that the player presses.
* **key arm** (*maker*): The lever arm extending from the pivot shaft to the touchpiece.
* **pad cup** (*maker*): The shallow dish at the end of the pad arm that holds the sealing pad.
* **pad arm** (*maker*): The arm extending from the pivot shaft to the pad cup.
* **tone hole rim** (*user*): The raised, flat annular rim surrounding a tonehole against which the pad seals.
* **mount** (*maker*): The raised boss around a keyed tonehole that thickens the body wall.
* **travel stop** (*eng*): The domed post under the touchpiece that lands on the body to limit key stroke.
* **octave hole** (*user*): The 1.0 mm octave hole on the back of the body (Tonehole 1).
* **pin slot** (*user*): The slotted mount on the body holding the filament cross pin for Key 1.
* **spring bed** (*ours*): The integrated body feature holding the root of a pin spring or sheet spring.
* **compensatory additional openings** (*user*): Geometric openings modeled in Inria Openwind to keep toneholes fully rounded while satisfying print overhang limits.

### Springs and Assembly
* **filament pin** (*user*): A snippet of standard 1.75 mm FDM printer filament used as the pivot cross pin for Key 1 in the pin slot.
* **pin spring** (*user*): A straight flexible spring cut from standard 1.75 mm FDM printer filament, anchored in the lower pillar base to hold Keys 2 to 4 closed.
* **sheet spring** (*maker*): The 3D-printed flexible cantilever spring strip that slides into the body spring bed to return Key 1 and keep the octave hole closed at rest.
* **snap assembly** (*user*): The tool-free method by which key brackets snap directly into body pillar slots without screws or aftermarket fasteners.
* **sealing pads** (*user*): Craft foam, adhesive neoprene, leather pads, or any sealing disc material that creates an airtight seal over the tone hole rims.
* **tenon seal** (*user*): Sealing material for head-to-body and body-to-foot friction tenon joints; paper tape, thread, O-ring, or cork all work fine.

### Key Motions
* **press** (*maker*): The linear distance (in mm) the touchpiece moves under the finger from rest to the travel stop.
* **lift** (*maker*): The distance (in mm) the pad lifts off the tone hole rim during key travel.
* **travel** (*maker*): The angular rotation (in degrees) of the key about its pivot axis.
* **turn** (*eng*): The rotational movement of Keys 2 to 4 about their longitudinal hinge axes.
* **rock** (*maker*): The seesaw motion of Key 1 rocking on its tangential cross pin in the pin slot.

### Acoustics and Pedagogy
* **conical bore** (*maker*): The internal acoustic taper of the recorder air column.
* **Inria Openwind** (*cited source*): The open-source Python acoustic modeling toolbox used to compute air column impedance, intonation, and tonehole dimensions.
* **Interactive Fingering Viewer** (*ours*): The web application (`fingering_viewer.html`) displaying inverted single-handed fingerings on dynamic musical staff notation.

---

## 3. Banned Terms and Jargon (Do Not Use)

| Banned Jargon | Why It Is Banned | Authorized Replacement |
|:---|:---|:---|
| **BOM / Bill of Materials** | Manufacturing and corporate jargon. | Say "what comes off the printer" or provide a plain list of parts. |
| **Screws / Screw mechanism** | False and non-existent on this instrument. | Say "snap assembly" or "screwless assembly". |
| **Bought metal springs** | False on this instrument. | Say "1.75 mm filament pin springs" and "printed sheet spring". |
| **Needle spring** | Inaccurate here. | Use "pin spring" (made from 1.75 mm filament). |
| **Saddle** | Inaccurate here; not a maker term for this instrument. | Use "pin slot". |
| **Bushing rim** | Inaccurate CAD jargon. | Use "tone hole rim". |
| **Sacrificial aid / cradle / jig** | Banned engineering concept (except authorized shaft stakes). | Describe the specific part itself without aid jargon. |
| **STEP (in public release / docs)** | Internal development format only; never tell the public. | Refer strictly to plain downloadable STL files. |
| **Dolmetsch** | Inaccurate; this project's mechanics and design are completely different. | Do not use to describe this project's mechanics. |
| **Touch crank** | Hallucinated jargon. | Use "touchpiece" for the button/key pressed, or "key arm" for the lever arm. |
| **Paddle** | Agent shorthand for the removed touchpiece plate; from no source. | Use "touchpiece" for the face the player presses; keys 2 to 4 have no separate part. |
| **Octave vent plug** | Hallucinated jargon. | Use "octave hole" or "thumb hole (Hole 1)". |
| **Octave vent** | Hallucinated jargon. | Use "octave hole" or "thumb hole (Hole 1)". |
| **Fingerpad / Keypad / Button** | Ambiguous or non-standard. | Use "touchpiece" for the button/key that you press. |
| **Thumb hole cover** | Inaccurate; it covers nothing. | Use "octave hole" or "thumb hole (Hole 1)". |
