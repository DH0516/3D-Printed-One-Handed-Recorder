// Pure scene construction for the Model A1 3D preview: no DOM, no
// WebGL, so it can be built and checked in Node (test_scene.mjs).
import * as THREE from './vendor/three.module.min.js';

export function buildGroup(bin, index) {
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
  return group;
}

export function frameCamera(group) {
  const box3 = new THREE.Box3().setFromObject(group);
  const center = box3.getCenter(new THREE.Vector3());
  const size = box3.getSize(new THREE.Vector3());
  const maxDim = Math.max(size.x, size.y, size.z);
  const camera = new THREE.PerspectiveCamera(40, 1, maxDim / 100, maxDim * 20);
  camera.position.copy(center).add(
    new THREE.Vector3(maxDim * 0.55, maxDim * 0.5, maxDim * 1.15));
  camera.lookAt(center);
  return { camera, center, size, maxDim };
}
