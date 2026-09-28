---
title: Model A2
layout: default
---

# Model A2

Model A2 is the variant with the octave key at the back: Key 1 moves from the front key cluster to the back of the body and is operated by the thumb. Keys 2 to 4 and all finger holes are identical to Model A1, and both variants share the same fingering chart. Right-handed by default; mirror all parts along the bore axis for a left-handed instrument.

## Specifications

- Type: Soprano (Descant) recorder in C
- Pitch reference: A = 440
- Keys: 4 printed keys (Key 1 thumb-operated octave key at the back, Keys 2 to 4 tone keys)
- Pin diameter: 2.00 mm bores (pinned with 1.75 mm printer filament, which also forms the key springs)
- Head joint: any standard plastic soprano recorder head joint (not printed)
- Assembly: snap joints, no screws; see [How to Assemble](6-how-to-assemble.md)

## Print Files

Binary STL, meshed at 0.005 mm chordal deviation and 0.1 rad angular tolerance, in print orientation. Printing guidelines are in [How to 3D Print](5-how-to-3d-print.md).

| Part               | File                                      | Print height | File size |
| ------------------ | ----------------------------------------- | ------------ | --------- |
| Body               | [Body.stl](../models/A2/parts/A2-Body.stl)   | 171.9 mm     | 6.2 MB    |
| Foot joint         | [Foot.stl](../models/A2/parts/A2-Foot.stl)   | 63.6 mm      | 7.9 MB    |
| Key 1 (octave key) | [Key_1.stl](../models/A2/parts/A2-Key_1.stl) | 11.0 mm      | 3.9 MB    |
| Key 2              | [Key_2.stl](../models/A2/parts/A2-Key_2.stl) | 25.6 mm      | 2.0 MB    |
| Key 3              | [Key_3.stl](../models/A2/parts/A2-Key_3.stl) | 17.7 mm      | 2.3 MB    |
| Key 4              | [Key_4.stl](../models/A2/parts/A2-Key_4.stl) | 26.6 mm      | 6.1 MB    |

The foot joint and Keys 2 to 4 are identical to Model A1. The fingering chart shared by both variants is in the [fingering viewer](fingering_viewer.html).

## 3D Preview

*Be aware that the 3D previewer is purely experimental and cannot accurately render the instrument*

Assembled body, foot, and keys with Key 1 at the back as the thumb key (the commercial head joint is not part of the model). Drag to rotate, scroll to zoom, right-drag or two-finger drag to pan. Loads about 3 MB of mesh data on first click.

<div>
<button id="previewBtnA2" type="button" style="padding:10px 16px;border-radius:8px;border:1px solid #0e6f66;background:#0e6f66;color:#fff;font-weight:600;cursor:pointer;">3D preview viewer</button>
<span id="previewStatusA2" style="margin-left:10px;color:#68747d;"></span>
</div>
<div id="previewBoxA2" style="display:none;margin-top:12px;border:1px solid #d8d2c2;border-radius:10px;height:440px;overflow:hidden;"></div>
<script type="module">
import { mountPreview } from './preview/viewer.mjs';
mountPreview({
  button: document.getElementById('previewBtnA2'),
  status: document.getElementById('previewStatusA2'),
  box: document.getElementById('previewBoxA2'),
  binUrl: 'preview/viewdata-A2.bin?v=1',
  indexUrl: 'preview/viewdata-A2-index.json?v=1',
});
</script>
