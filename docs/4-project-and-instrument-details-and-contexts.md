---
title: Project and Instrument Details and Contexts
layout: default
---

# 3. Project and Instrument Details and Contexts

### 3.1 Target Audience
- Individuals with accessibility needs of upper-limbs with some limitations (one hand, or two hands with partial limitations).
- Organizations working with such accessibility-need individuals wanting to provide a starting point of a solution.
- Performers looking for a double-soprano-recorder solution.
- Researchers and educators interested in assistive musical technology.

### 3.2 Instrument Details
- **Type:** Currently scoped for only Descant (Soprano) variant. Descant is typically recommended for children, while treble (alto) may be equally considered in professional or ensemble settings.
- **Key System:** Four keys replace the missing hand's fingers and thumb.
- **Fingering:** Requires specialized fingering chart, which is an inversion of the holes to keys where keys are replacing the holes. Left-hand and right-hand models use mirrored variants of the fingering system.
- **Handedness:** The primary instrument design (v1) is right-handed. A left-handed instrument can be made by mirroring everything horizontally along the axis of the bore.

### 3.3 Development Realities
- **Prototyping vs. Mass Production:** For this project, the advantage of 3D printing is rapid prototyping and customizability rather than high-speed mass production.
- **Development Process:** Creating a functional acoustic instrument with 3D printing involves significant calibration, testing, and fine-tuning of acoustic tolerances.
- **Iterative Adjustment:** Print calibration and trial-and-error are expected parts of the process, and designs may need adjustments to fit individual printer tolerances.
- **The Key Challenge:** Mechanical keys have been a major focus in our initial research. Because keys require airtight padding and precise pivots, we invited a professional instrument repairer for direct consultation.
- **Iterative Redesign:** We went through numerous redesign cycles to achieve reliable key seals and responsive movement.
- **Our Goal:** Our goal is to empower users and local makers to fabricate and iterate on these designs themselves using accessible consumer tools.
- **Core Purpose is "Accessibility":** The project is designed to serve upper-limb accessibility, utilizing consumer-grade FDM printers and common, safe FDM thermoplastics (including PLA, PETG, and other safe filaments).
- **Access and Upgrade Barriers:** While mass-produced plastic soprano recorders are widely available and affordable, upgrading to wooden instruments or obtaining customized parts is costly and difficult. The inherent sophistication of the recorder makes it challenging to customize, particularly due to the complexity of the fipple, but also extending to key layouts and custom sizing.
- **No Proprietary Hardware:** Any non-printed hardware additions (e.g., rubber bands, springs, pads, pins) must be readily purchasable by the general public at standard hardware stores or online retailers. No proprietary or custom-engineered hardware is required. If a specific part is not available, we will suggest alternative items, and users are welcome to contact us for suggestions.
- **Freedom to Print & Modify:** Users are encouraged to print, replicate, test, and modify the files to fit their personal anatomical requirements.
- **Academic Licensing & IP Attribution:** While users have freedom to print and modify the designs, the core design ideas and research development belong to the original author/team, protected under an open-source non-commercial license (such as Creative Commons Attribution-NonCommercial CC BY-NC). This allows anyone to print, share, and modify the designs for personal or educational use, but strictly prohibits commercial sale or exploitation of the design files or finished instruments for money, and requires that the original project and author/team are cited when the design is used or shared.

### 3.4 Materials Selection & UV Resin Safety Hazards
- **We know many materials out there:** When designing a 3D-printable instrument, there are numerous options available, ranging from liquid photopolymers to various meltable thermoplastics.
- **Toxicity of Consumer-Grade UV Resin:** Standard consumer-grade photopolymer UV resins used in stereolithography (SLA/DLP) printers present severe health and safety risks, making them unsuitable for mouth-contact instruments like recorders. In their liquid state, these resins contain reactive monomers, oligomers, and photoinitiators that are known skin and respiratory irritants. Direct contact can cause severe allergic contact dermatitis and chemical sensitization over time (Macdonald et al., 2016; Alifui-Segbaya et al., 2017). Furthermore, standard UV resins are not approved for oral contact, as uncured monomer residues can leach into saliva.
- **Incomplete Curing in Opaque Resins:** If non-translucent (opaque) UV resin is used, it is highly likely that the inside of the printed parts was not cured properly because UV light cannot reach there. Opaque pigments (like Titanium Dioxide or Carbon Black) absorb and scatter UV light, reducing the cure depth (Tomec et al., 2022). This leaves toxic, uncured liquid resin trapped within the internal structures of the instrument, posing severe contact health hazards.
- **FDM with PLA Selection:** Due to these safety concerns, we had to choose FDM (Fused Deposition Modeling) with PLA (Polylactic Acid) in the end as our main baseline (though other FDM materials like PETG should work fine too). Unless using certified biocompatible medical/dental-grade resins subjected to strict medical curing procedures, SLA resins must be avoided for mouth-contact instruments.

### 3.5 Design Integrity & Intellectual Property Compliance
To ensure respect for intellectual property while keeping our work completely open-source, the project operates under a set of design integrity and compliance guidelines:
- **Independent Expressive Creation:** All CAD models (such as `body default/`), photographs, instructions, and text in this repository are created independently by the team.
- **Factual Data Re-derivation:** The fingering layout and acoustic measurements are independently compiled and re-tabulated, rather than copying the graphic layout or arrangement of existing third-party fingering charts.
- **Trademark Boundaries:** We market this project under its descriptive name, **3D-Printed-One-Handed-Recorder**. Historical names (such as "Dolmetsch") are referenced purely descriptively and historically to identify the design inspiration, never as a product logo or trademark.
- **Academic Licensing & IP Attribution:** As described in Section 3.3, the project utilizes the Creative Commons Attribution-NonCommercial (CC BY-NC) license. This permits free non-commercial recreation, customization, and study of the design files, provided that the original project and author/team are cited when shared or used.

### 3.6 Fipple Mechanics & Head Joint Exclusion
At this stage, this project does not include design files for printing the head joint (mouthpiece) of the recorder. This decision is based on two primary considerations:
- **Design and Acoustic Complexity:** The fipple and jet mechanisms of the recorder are highly complex and are subjects of popular acoustics studies. In particular, the labium is a very complicated construct, requiring precise sizing of all four sides and the internals. A poorly designed or printed labium causes severe sound defects, commonly observed in low-quality recorders. To avoid providing a low-quality instrument, we recommend using a generic, easily available commercial head joint that plays well.
- **Safety and Liability:** We are hesitant to instruct users to place home-printed objects directly into their mouths. Even if the materials used are certified as safe, the project team cannot assume responsibility or liability for any health concerns that may arise from using home-fabricated mouthpieces.

The **soprano-440-v1** model is designed to pair with any standard 440-442Hz plastic soprano recorder head (for example, a Yamaha plastic soprano head will work).

## References
1. **Photopolymer Biocompatibility & Toxicity:** Macdonald, N. P., et al. (2016). *Assessment of biocompatibility of 3D printed photopolymers*. PLoS ONE, 11(8), e0160741. This study documents the high cytotoxicity of standard 3D printed photopolymers on living cells and warns of leachable toxic compounds.
2. **Dental Resin Toxicity:** Alifui-Segbaya, F., et al. (2017). *Biocompatibility of 3D-printed dental resins*. Dental Materials, 33(11), 1251-1258. Discusses toxic monomer leaching and sensitization risks in oral mucosal contact.
3. **Curing Depth of Pigmented Resins:** Tomec, M., et al. (2022). *Influence of Pigment Concentration on the Cure Depth and Degree of Conversion of Dental Resins*. Journal of Photopolymer Science and Technology, 35(3), 241-248. This study explains how pigments absorb and scatter UV light, exponentially reducing light penetration depth (cure depth) and leaving liquid uncured resin trapped inside the model.
4. **Factual Data & Copyright:** *Feist Publications, Inc. v. Rural Telephone Service Co.*, 499 U.S. 340 (1991). Landmark legal case establishing that factual data and information are not protected by copyright.
5. **Useful Articles Doctrine:** U.S. Copyright Act, 17 U.S.C. §§101, 102(b). Details the exclusion of functional aspects and procedures of useful physical articles from copyright protection.
