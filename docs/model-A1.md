---
title: Model A1
layout: default
---

# Model A1

Model A1 is the standard variant of the one-handed soprano recorder: Key 1 (the octave key) sits in the key cluster at the front top with Keys 2 to 4, each lying between the lower finger holes. Right-handed by default; mirror all parts along the bore axis for a left-handed instrument.

## Specifications

- Type: Soprano (Descant) recorder in C
- Pitch reference: A = 440
- Keys: 4 printed keys (Key 1 octave key, Keys 2 to 4 tone keys)
- Pin diameter: 2.00 mm bores (pinned with 1.75 mm printer filament, which also forms the key springs)
- Head joint: any standard plastic soprano recorder head joint (not printed)
- Assembly: snap joints, no screws; see [How to Assemble](6-how-to-assemble.md)

## Print Files

Binary STL, meshed at 0.005 mm chordal deviation and 0.1 rad angular tolerance, in print orientation. Printing guidelines are in [How to 3D Print](5-how-to-3d-print.md).

| Part               | File                                      | Print height | File size |
| ------------------ | ----------------------------------------- | ------------ | --------- |
| Body               | [A1-Body.stl](../models/A1/parts/A1-Body.stl)   | 171.9 mm     | 6.5 MB    |
| Foot joint         | [A1-Foot.stl](../models/A1/parts/A1-Foot.stl)   | 63.6 mm      | 7.9 MB    |
| Key 1 (octave key) | [A1-Key_1.stl](../models/A1/parts/A1-Key_1.stl) | 10.9 mm      | 4.1 MB    |
| Key 2              | [A1-Key_2.stl](../models/A1/parts/A1-Key_2.stl) | 25.6 mm      | 2.0 MB    |
| Key 3              | [A1-Key_3.stl](../models/A1/parts/A1-Key_3.stl) | 17.7 mm      | 2.3 MB    |
| Key 4              | [A1-Key_4.stl](../models/A1/parts/A1-Key_4.stl) | 26.6 mm      | 6.1 MB    |

Keys 2 to 4 print as one piece each in this set. The fingering chart shared by both model variants is in the [fingering viewer](fingering_viewer.html).

## 3D Preview

*Be aware that the 3D previewer is purely experimental and cannot accurately render the instrument*

Assembled body, foot, and keys (the commercial head joint is not part of the model). Drag to rotate, scroll to zoom, right-drag or two-finger drag to pan. Loads about 3 MB of mesh data on first click.

<div>
<button id="previewBtnA1" type="button" style="padding:10px 16px;border-radius:8px;border:1px solid #0e6f66;background:#0e6f66;color:#fff;font-weight:600;cursor:pointer;">3D preview viewer</button>
<span id="previewStatusA1" style="margin-left:10px;color:#68747d;"></span>
</div>
<div id="previewBoxA1" style="display:none;margin-top:12px;border:1px solid #d8d2c2;border-radius:10px;height:440px;overflow:hidden;"></div>
<script type="module">
import { mountPreview } from './preview/viewer.mjs';
mountPreview({
  button: document.getElementById('previewBtnA1'),
  status: document.getElementById('previewStatusA1'),
  box: document.getElementById('previewBoxA1'),
  binUrl: 'preview/viewdata.bin?v=2',
  indexUrl: 'preview/viewdata-index.json?v=2',
});
</script>
