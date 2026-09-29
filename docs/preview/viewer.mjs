// Shared click-to-load 3D preview: mounts into the given button,
// status, and box elements, fetching the given mesh binary and index.
// Left-drag rotate, wheel zoom, right-drag pan. The button listener
// attaches immediately; three.js and the mesh load only on click.
export function mountPreview({ button, status, box, binUrl, indexUrl }) {
  button.addEventListener('click', async () => {
    button.disabled = true;
    try {
      status.textContent = 'loading...';
      const [{ buildGroup, frameCamera }, THREE] = await Promise.all([
        import('./scene.mjs'),
        import('./vendor/three.module.min.js'),
      ]);
      const [bin, index] = await Promise.all([
        fetch(binUrl).then(r => { if (!r.ok) throw new Error('mesh data HTTP ' + r.status); return r.arrayBuffer(); }),
        fetch(indexUrl).then(r => r.json()),
      ]);
      status.textContent = 'building scene...';
      const scene = new THREE.Scene();
      scene.background = new THREE.Color(0xf4f1e8);
      const group = buildGroup(bin, index);
      scene.add(group);
      scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8578, 1.0));
      const sun = new THREE.DirectionalLight(0xffffff, 1.6);
      sun.position.set(80, 120, 160);
      scene.add(sun);
      const { camera, center, maxDim } = frameCamera(group);
      const renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setPixelRatio(window.devicePixelRatio);
      box.style.display = 'block';
      box.appendChild(renderer.domElement);
      const target = center.clone();
      const sph = new THREE.Spherical().setFromVector3(camera.position.clone().sub(target));
      const dom = renderer.domElement;
      let dragging = 0, lastX = 0, lastY = 0;
      dom.style.touchAction = 'none';
      dom.addEventListener('contextmenu', (e) => e.preventDefault());
      // Left-drag rotates. Pan: right-drag, middle-drag, Shift+left-drag,
      // or a two-finger touch drag. Wheel zooms.
      const panMode = (e) => e.button === 2 || e.button === 1 || e.shiftKey ||
                             (e.pointerType === 'touch' && e.isPrimary === false);
      dom.addEventListener('pointerdown', (e) => {
        dragging = panMode(e) ? 2 : 1;
        lastX = e.clientX; lastY = e.clientY;
        try { dom.setPointerCapture(e.pointerId); } catch (err) { /* fine */ }
        if (e.pointerType === 'touch') e.preventDefault();
      }, { passive: false });
      dom.addEventListener('pointerup', (e) => {
        dragging = 0;
        try { dom.releasePointerCapture(e.pointerId); } catch (err) { /* fine */ }
      });
      dom.addEventListener('pointercancel', () => { dragging = 0; });
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
          target.addScaledVector(right, dx * panScale);
          target.addScaledVector(camera.up, dy * panScale);
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
      // test handle: lets automation prove rotate/pan/zoom actually move
      // the camera; harmless in normal use
      window.__pv = {
        target: () => target.toArray(),
        radius: () => sph.radius,
      };
      status.textContent = '';
      button.textContent = '3D preview loaded';
    } catch (e) {
      status.textContent = 'failed: ' + e.message;
      button.disabled = false;
    }
  });
}
