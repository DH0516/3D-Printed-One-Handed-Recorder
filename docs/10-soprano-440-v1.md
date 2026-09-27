---
title: One-Handed Recorders: soprano-440-v1 Build Guide
layout: default
---

# One-Handed Recorders - soprano-440-v1

Welcome to the build documentation for the **soprano-440-v1** model. This instrument design is based on a resizing of a historical instrument by J.H. Rottenburgh (originally estimated to be pitched at A = 405 to 415 Hz) to modern pitch (A = 440 Hz). For organology specialists, we can likely produce custom model designs based on different historical models upon request.

The baseline files for **soprano-440-v1** are designed for a right-handed player. To make a left-handed version of the instrument, flip all design files horizontally (mirroring along the bore axis) in your CAD or slicing software.

This guide covers everything you need to 3D print, assemble, and troubleshoot your own one-handed soprano recorder.

## Table of Contents

1. [How to 3D Print](#how-to-3d-print)
   
   - [What is Needed (Tools & Materials)](#what-is-needed-tools--materials)
   
   - [Printer Settings](#what-settings-to-use)
2. [How to Assemble](#how-to-assemble)
3. [Troubleshooting](#troubleshooting)

---

## How to 3D Print

### What is Needed (Tools & Materials)

**Materials:**

- **Filament:** High-quality PLA or PETG (e.g., standard 1.75 mm). *Do not use toxic UV photopolymer resins or high-warp materials like ABS/ASA.*
- **Commercial Soprano Head Joint:** Standard 440–442 Hz plastic soprano head joint (such as Yamaha YRS-24B or YRS-302B) with approx. 19.5–20.0 mm tenon socket diameter.
- **Springs / Return Elasticity:** Stainless steel miniature torsion springs (0.3–0.4 mm wire diameter) or orthodontic elastic bands (1/8" or 3/16" medium/heavy pull) for key returns.
- **Sealing Pads:** 1.0 mm – 1.5 mm closed-cell neoprene sheet, natural cork pads, or soft instrument pad leather cut to 9.0–11.0 mm discs matching the key cups.
- **Pivot Pins:** 1.0 mm or 1.2 mm stainless steel rods or brass wire cut to length for the 4 key hinge pivots.
- **Adhesive & Joint Wrap:** Gel cyanoacrylate (super glue) for pads, and cotton/silk thread or PTFE plumber's tape for wrapping tenons.

**Tools:**

- **3D Printer:** Any consumer FDM 3D printer with at least 160 mm Z-height build volume (e.g., Bambu Lab A1 Mini, Prusa MK3/MK4/Mini, Ender 3).
- **Finishing & Deburring:** 400, 800, and 1200 grit wet/dry sandpaper, needle files, and hobby deburring tool.
- **Assembly Tools:** Needle-nose pliers, fine tweezers, flush cutters, and a small hand pin-vise or 1.0/1.2 mm drill bit.

### What Settings to Use

Detailed slicer configuration for optimal acoustic airtightness and mechanical precision:

- **Orientation:** Print body joints vertically on the build plate (tenon facing up or down based on socket bevel).
- **Layer Height:** 0.12 mm (recommended) or 0.16 mm.
- **Wall Loops / Perimeters:** 5–6 wall loops (minimum 2.0 mm total wall thickness) to guarantee full pneumatic seal against air leakage.
- **Infill:** 100% solid infill (or high density rectilinear > 60%) to improve acoustic density and eliminate resonance dampening.
- **Seam Alignment:** Set seam position to "Aligned" or "Rear" placed along the back exterior of the instrument. Do not use random seams or scarf seams inside the bore.
- **Supports:** Disable supports inside tone holes and bore. If needed, support only the external underside of overhang pillars or tenon step lips.
- **Brim:** Outer brim of 8 mm with 0.1 mm brim gap for bed stability during tall vertical printing.

---

## How to Assemble

1. **Preparing the Body:**
   
   - Check the printed bore for strings, fuzz, or blobs. Smooth internal bore with 800-grit sandpaper rolled around a dowel if necessary.
   
   - Deburr tone hole edges using needle files so the pads will seat completely flat.
   
   - Lightly sand the male tenon to remove seam bumps and check initial dry fit into the head joint and foot joint sockets.

2. **Mounting the Keys:**
   
   - Test each key arm in its pivot pillar. If tight, ream the hinge hole with a 1.0 mm or 1.2 mm drill bit.
   
   - Slide pivot pins through the pillar posts and key hinges. Secure ends with a tiny dab of glue or mechanical friction.
   
   - Hook the torsion springs or elastic bands between the key anchors and body hooks, confirming instant, snappy return upon release.

3. **Applying Seals:**
   
   - Cut pad discs matching key cup diameters (approx. 9–11 mm).
   
   - Apply a small drop of gel super glue into the key cup and seat the pad firmly.
   
   - Close the key and check for airtight closure across 360 degrees of the tone hole rim.

4. **Final Fitting:**
   
   - Wrap the tenon joints with thread or PTFE tape until they slide smoothly into the commercial head joint with a firm, airtight friction fit.
   
   - Apply a small amount of cork grease or paraffin wax.
   
   - Play a chromatic scale from Low C up to High D following the fingering chart.

---

## Troubleshooting

- **Issue: Low notes (C, C#, D) sound airy, soft, or fail to speak.**
  - **Solution:** Check key pad seating with a light inside the bore. Re-level pads or file tone hole rims flat. Check tenon joint wrap tightness.
- **Issue: Keys stick or feel sluggish.**
  - **Solution:** Ream key hinge holes slightly with a needle file; ensure pivot pin is straight; increase spring tension.
- **Issue: Tenons are too loose or tight.**
  - **Solution:** Increase thread wrapping passes or slightly sand the tenon with 400-grit sandpaper (or other lower grit). Optionally lubricate with cork grease.