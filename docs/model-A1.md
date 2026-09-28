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

Binary STL, meshed at 0.01 mm chordal deviation, in print orientation. Printing guidelines are in [How to 3D Print](5-how-to-3d-print.md).

| Part | File | Print height | File size |
|---|---|---|---|
| Body | [Body.stl](../models/A1/parts/Body.stl) | 171.9 mm | 1.6 MB |
| Foot joint | [Foot.stl](../models/A1/parts/Foot.stl) | 63.6 mm | 2.2 MB |
| Key 1 (octave key) | [Key_1.stl](../models/A1/parts/Key_1.stl) | 10.9 mm | 0.7 MB |
| Key 2 | [Key_2.stl](../models/A1/parts/Key_2.stl) | 25.6 mm | 0.4 MB |
| Key 3 | [Key_3.stl](../models/A1/parts/Key_3.stl) | 17.7 mm | 0.5 MB |
| Key 4 | [Key_4.stl](../models/A1/parts/Key_4.stl) | 26.6 mm | 0.9 MB |

Keys 2 to 4 print as one piece each in this set. The fingering chart shared by both model variants is in the [fingering viewer](fingering_viewer.html).

## 3D Preview

Assembled body, foot, and keys (the commercial head joint is not part of the model). Drag to rotate, scroll to zoom, right-drag or two-finger drag to pan. Loads about 3 MB of mesh data on first click.

<div>
<button id="previewBtn" type="button" style="padding:10px 16px;border-radius:8px;border:1px solid #0e6f66;background:#0e6f66;color:#fff;font-weight:600;cursor:pointer;">3D preview viewer</button>
<span id="previewStatus" style="margin-left:10px;color:#68747d;"></span>
</div>
<div id="previewBox" style="display:none;margin-top:12px;border:1px solid #d8d2c2;border-radius:10px;height:440px;overflow:hidden;"></div>

<script type="module">
const btn = document.getElementById('previewBtn');
btn.addEventListener('click', async () => {
  const status = document.getElementById('previewStatus');
  const box = document.getElementById('previewBox');
  btn.disabled = true;
  try {
    status.textContent = 'loading...';
    const THREE = await import('./preview/vendor/three.module.min.js');
    const [bin, index] = await Promise.all([
      fetch('preview/viewdata.bin?v=2').then(r => { if (!r.ok) throw new Error('mesh data HTTP ' + r.status); return r.arrayBuffer(); }),
      fetch('preview/viewdata-index.json?v=2').then(r => r.json()),
    ]);
    status.textContent = 'building scene...';
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf4f1e8);
    const group = new THREE.Group();
    group.rotation.x = -Math.PI / 2;  // data is Z-up
    let off = 0;
    for (const p of index.parts) {
      const n = p.tris * 9;
      const f = new Float32Array(bin, off * 4, n);
      const geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.BufferAttribute(f, 3));
      geo.computeVertexNormals();
      group.add(new THREE.Mesh(geo, new THREE.MeshStandardMaterial({
        color: new THREE.Color(p.color), roughness: 0.55, metalness: 0.1,
      })));
      off += n;
    }
    scene.add(group);
    scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8578, 1.0));
    const sun = new THREE.DirectionalLight(0xffffff, 1.6);
    sun.position.set(80, 120, 160);
    scene.add(sun);
    const box3 = new THREE.Box3().setFromObject(group);
    const center = box3.getCenter(new THREE.Vector3());
    const size = box3.getSize(new THREE.Vector3());
    const maxDim = Math.max(size.x, size.y, size.z);
    const camera = new THREE.PerspectiveCamera(40, 1, maxDim / 100, maxDim * 20);
    camera.position.copy(center).add(new THREE.Vector3(maxDim * 0.55, maxDim * 0.5, maxDim * 1.15));
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    box.style.display = 'block';
    box.appendChild(renderer.domElement);
    // Minimal orbit controls: left-drag rotate, wheel zoom, right-drag pan.
    const target = center.clone();
    let sph = new THREE.Spherical().setFromVector3(camera.position.clone().sub(target));
    const dom = renderer.domElement;
    let dragging = 0, lastX = 0, lastY = 0;
    dom.style.touchAction = 'none';
    dom.addEventListener('contextmenu', (e) => e.preventDefault());
    dom.addEventListener('pointerdown', (e) => { dragging = e.button === 2 ? 2 : 1; lastX = e.clientX; lastY = e.clientY; dom.setPointerCapture(e.pointerId); });
    dom.addEventListener('pointerup', (e) => { dragging = 0; dom.releasePointerCapture(e.pointerId); });
    dom.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      const dx = e.clientX - lastX, dy = e.clientY - lastY;
      lastX = e.clientX; lastY = e.clientY;
      if (dragging === 1) {
        sph.theta -= 2 * Math.PI * dx / dom.clientHeight;
        sph.phi -= 2 * Math.PI * dy / dom.clientHeight;
        sph.phi = Math.max(0.05, Math.min(Math.PI - 0.05, sph.phi));
      } else {
        const panScale = sph.radius * 1.2 / dom.clientHeight;
        const right = new THREE.Vector3().setFromSpherical(sph).cross(camera.up).normalize();
        const up = camera.up.clone();
        target.addScaledVector(right, dx * panScale);
        target.addScaledVector(up, dy * panScale);
      }
    });
    dom.addEventListener('wheel', (e) => {
      e.preventDefault();
      sph.radius = Math.max(maxDim * 0.2, Math.min(maxDim * 8, sph.radius * (1 + Math.sign(e.deltaY) * 0.1)));
    }, { passive: false });
    const applyCamera = () => {
      camera.position.setFromSpherical(sph).add(target);
      camera.lookAt(target);
    };
    const fit = () => {
      const w = box.clientWidth, h = box.clientHeight;
      renderer.setSize(w, h);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    };
    fit();
    new ResizeObserver(fit).observe(box);
    const loop = () => { applyCamera(); renderer.render(scene, camera); requestAnimationFrame(loop); };
    loop();
    status.textContent = '';
    btn.textContent = '3D preview loaded';
  } catch (e) {
    status.textContent = 'failed: ' + e.message;
    btn.disabled = false;
  }
});
</script>
