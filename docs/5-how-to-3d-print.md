---
title: How to 3D Print
layout: default
---

# 4. How to 3D Print

### 4.1 What is Needed (Tools & Materials)

**Materials:**

- **Filament:** Standard 1.75 mm PLA or PETG. Warping materials like ABS and ASA have not been tested at all, and we never recommend using photopolymer resin, especially for any mouth-contact part; see [Project and Instrument Details and Contexts](4-project-and-instrument-details-and-contexts.md).
- **Commercial Recorder Head Joint:** A standard 440-442 Hz plastic soprano recorder head joint is required for the **soprano-440** model, as the head joint is not printed in this project. (See [Fipple Mechanics & Head Joint Exclusion](4-project-and-instrument-details-and-contexts.md#36-fipple-mechanics--head-joint-exclusion) for details).
- **1.75 mm Filament Snippets:** A few short pieces of ordinary printer filament. One acts as the pivot pin for Key 1; the others are the bending pin springs that close Keys 2 to 4.
- **Sealing Pads:** Discs of 1.0-1.5 mm closed-cell neoprene, natural cork, craft foam, or soft leather, cut to the key cup diameters. This is the only part of the instrument where it cannot be "3D printed".

- **Tenon Seal:** Paper tape, thread, O-ring, or cork for the friction joints.

**Tools:**

- **3D Printer:** Any consumer FDM printer with at least 160 mm of Z height. The middle joint is the tallest part at roughly 15 to 16 cm.
- **Finishing Tools:** 400 to 1200 grit wet/dry sandpaper, miniature needle files, and deburring tools to clean up tone holes and clear away print stringing hair if you experience stringing issues.
- **Pliers & Tweezers:** Needle-nose pliers, fine tweezers, flush cutters, or a small craft knife.

### 4.2 What Settings to Use (Suggested Recommendations)

> [!NOTE]
> Most generic or general slicing settings should be okay for a standard print. The fine settings detailed below are recommended from a troubleshooting perspective to optimize print quality, airtightness, and acoustic performance.

- **Calibration & Tolerances:** Ensure your printer is properly calibrated for dimensional precision before printing. The instrument design is optimized so that standard tolerances of ~0.5 mm are generally okay.
- **Orientation:** Print the body and foot joint vertically along the bore axis with the tenon on the build plate. Never print the acoustic body horizontally: horizontal layer lines cause bore distortion and air leakage. Print the keys with standard slicer supports.
- **Layer Height:** 0.12 mm is recommended for better acoustic seal and detail on tone hole bevels; 0.16 mm is acceptable.
- **Wall Perimeters:** Use at least 4 to 6 wall loops (minimum 2.0 mm total wall thickness) to ensure complete airtightness through layer lines and provide structural rigidity.
- **Infill:** Printing as a full solid (100% infill) is ideal, but if you are experiencing over extrusion issues, you could print with sparse infill, while keeping the infill density high (80%+). The sparse infill pattern itself does not affect the sound; choose a simple pattern (such as grid or rectilinear) to save print time and ensure complete sealing around the bore.
- **Bridges:** Disable "thick internal bridges" and "detect overhang walls" in your slicer settings to prevent internal bore distortions. (Unless you have a specific way to handle these).
- **Supports:** Try to not add supports on the tone holes, as supported holes can come out dirtier and rougher than expected. Supports are needed for the keys, tenons, and key holders. I prefer tree supports for easier detachment.
- **Seams:** Random seams provide stronger seals for the bore. Avoid using scarf seams as they can introduce leaks.
- **Brim:** Use an outer brim of at least 5 mm to ensure solid bed adhesion when printing tall joint sections vertically.

### 4.3 Pitch Precision & Tone Hole Resizing

Because 3D printing involves material shrinkage, and slicing variations, the printed instrument's acoustic pitches might not be perfectly precise out of the box. 

Generally speaking, adjusting the tone holes are not advised. You can consider cleaning the holes and the bore if the print produced stringings, but further changes are not necessary. There are compensatory shapes around tone holes to offset the overhang sagging. Please consider reprinting after checking your calibrations and measurements rather than jumping to making manual changes on the printed instrument.

## References

1. **Related Acoustic Research:** Ha, D. and Scavone, G. (2026). "Acoustic Impedance and Viscothermal Losses in FDM-Printed Cylindrical Waveguides: Influence of Surface Conditions and Infill Structures." *Proceedings of Meetings on Acoustics*, International Symposium on Musical Acoustics (ISMA 2026), Helsinki, Finland, 15-17 June 2026. DOI: TBD.
