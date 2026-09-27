---
title: How to 3D Print
layout: default
---

# 4. How to 3D Print

### 4.1 What is Needed (Tools & Materials)

*This section lists the necessary parts, filaments, and tools.*

**Materials:**

- **Filament / Material Choice:** We recommend **FDM (Fused Deposition Modeling) using safe thermoplastics such as PLA or PETG** (though other safe FDM filaments work well too). Liquid photopolymer resins are excluded from this project due to the safety hazards detailed in [Project and Instrument Details and Contexts](4-project-and-instrument-details-and-contexts.md).
  * *Note on ABS/ASA:* While standard safe FDM filaments work well, materials like ABS and ASA are known to warp during printing and should be avoided.
- **Commercial Recorder Head Joint:** A standard 440-442Hz plastic soprano recorder head joint (e.g., from a Yamaha plastic soprano recorder) is required for the **soprano-440-v1** model, as the head joint is not printed in this project. (See [Fipple Mechanics & Head Joint Exclusion](4-project-and-instrument-details-and-contexts.md#36-fipple-mechanics--head-joint-exclusion) for details).
- **Springs / Elastic Bands:** Small stainless steel torsion springs (0.3 mm – 0.5 mm wire diameter) or orthodontic-grade elastic bands / small silicone O-rings to provide reliable key return tension.
- **Padding / Cork:** 1.0 mm – 1.5 mm closed-cell neoprene, natural instrument cork sheets, or soft leather pads cut to key cup diameters for airtight tone hole sealing.
- **Glue / Adhesive:** Medium/gel cyanoacrylate (super glue) or contact cement for securing pads to key cups.
- **Pivot Pins:** 1.0 mm or 1.2 mm stainless steel wire, brass rod, or standard dressmaker steel pins for key hinge axles.

**Tools:**

- **3D Printer:** A generic FDM printer that you can find at home. The middle joint (the tallest part of the instrument) is expected to be around 15 to 16 cm in height, which safely clears the build volume of a Bambu A1 Mini.
- **Finishing Tools:** 400 to 1200 grit wet/dry sandpaper, miniature needle files, and deburring tools to clean up tone holes and clear away print hair if you experience stringing/hairing issues.
- **Pliers & Tweezers:** Needle-nose pliers, fine tweezers, and flush cutters for assembling pivot pins, bending spring ends, and positioning key pads.

### 4.2 What Settings to Use (Suggested Recommendations)

*Detailed slicer settings to ensure the recorder is airtight and dimensionally accurate.*

> [!NOTE]
> Most generic or general slicing settings should be okay for a standard print. The fine settings detailed below are recommended from a troubleshooting perspective to optimize print quality, airtightness, and acoustic performance.

- **Calibration & Tolerances:** Ensure your printer is properly calibrated for dimensional precision before printing. The instrument design is optimized so that standard tolerances of ~0.5 mm are generally okay.
- **Layer Height:** ~0.16 mm is acceptable, but a smaller layer height of 0.12 mm is recommended for better acoustic seal and detail on tone hole bevels.
- **Wall Perimeters:** Use at least 4 to 6 wall loops (perimeters) to ensure complete airtightness through layer lines and provide structural rigidity.
- **Infill:** Printing as a full solid (100% infill) is ideal, but if printing with sparse infill, keep the infill density high (60%+). The sparse infill pattern itself does not matter; choose a simple pattern (such as grid or rectilinear) to save print time.
- **Bridges:** Disable "thick internal bridges" in your slicer settings to prevent internal bore distortions.
- **Supports:** Try to not add supports on the tone holes, as supported holes can come out dirtier and rougher than expected. If supports are needed, they can be added on the middle joint tenon.
- **Seams (Scarf Seams):** Do not use scarf seams or random seams for the inside of the instrument bore. The best results for Scarf Seams is to place aligned seams on the exterior back or side of the instrument to maintain a smooth internal bore.
- **Brim:** (Recommended) Use an ample amount of outer brim of 5 mm minimum to ensure solid bed adhesion when printing tall joint sections vertically.

### 4.3 Pitch Precision & Tone Hole Resizing

Because 3D printing involves material shrinkage, slicing variations, and internal bore surface textures, the printed instrument's acoustic pitches might not be perfectly precise out of the box.

- **Tone Hole Adjustment:** Depending on your specific printing context (filament type, printer calibration, and slicing tolerances), you may need to resize the tone holes on the side plane of the recorder.
- **Tuning Guidelines:** If a note plays too flat, carefully enlarge the corresponding tone hole using a sand paper or similar tools. If a note plays too sharp, the hole size can be slightly reduced by rubbing to add some beewax around the tone hole. 

## References

1. **ISMA 2026 Paper:** [Author/Team's research paper on 3D-printed one-handed recorders, International Symposium on Musical Acoustics (ISMA 2026)].
