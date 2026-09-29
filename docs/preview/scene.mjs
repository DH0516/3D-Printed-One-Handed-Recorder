// Pure scene construction for the 3D previews: no DOM, no WebGL, so it
// can be built and checked in Node (test_scene.mjs).
import * as THREE from './vendor/three.module.min.js';

// Corners within WELD millimetres merge into one vertex, then normals
// average only across faces within CREASE deg of each other: bores and
// pillars shade smooth, square key edges stay sharp.
const WELD = 1e-4;
const CREASE_COS = Math.cos((35 * Math.PI) / 180);

function weldedGeometry(f) {
  const tris = f.length / 9;
  const fn = new Float32Array(tris * 3);
  for (let t = 0; t < tris; t++) {
    const i = t * 9;
    const ux = f[i + 3] - f[i], uy = f[i + 4] - f[i + 1], uz = f[i + 5] - f[i + 2];
    const vx = f[i + 6] - f[i], vy = f[i + 7] - f[i + 1], vz = f[i + 8] - f[i + 2];
    let x = uy * vz - uz * vy, y = uz * vx - ux * vz, z = ux * vy - uy * vx;
    const l = Math.hypot(x, y, z);
    if (l > 1e-12) { x /= l; y /= l; z /= l; }
    fn[t * 3] = x; fn[t * 3 + 1] = y; fn[t * 3 + 2] = z;
  }
  const buckets = new Map();
  const px = [], py = [], pz = [], nx = [], ny = [], nz = [], nc = [];
  const index = new Uint32Array(tris * 3);
  for (let t = 0; t < tris; t++) {
    const tx = fn[t * 3], ty = fn[t * 3 + 1], tz = fn[t * 3 + 2];
    for (let c = 0; c < 3; c++) {
      const i = t * 9 + c * 3;
      const x = f[i], y = f[i + 1], z = f[i + 2];
      const key = Math.round(x / WELD) + ',' + Math.round(y / WELD) + ',' + Math.round(z / WELD);
      let ids = buckets.get(key);
      if (!ids) buckets.set(key, ids = []);
      let s = -1;
      for (let k = 0; k < ids.length; k++) {
        const id = ids[k];
        const dot = nx[id] * tx + ny[id] * ty + nz[id] * tz;
        const mag = Math.sqrt(nx[id] * nx[id] + ny[id] * ny[id] + nz[id] * nz[id]);
        if (mag > 0 && dot > CREASE_COS * mag) { s = id; break; }
      }
      if (s < 0) {
        s = px.length;
        px.push(x); py.push(y); pz.push(z);
        nx.push(0); ny.push(0); nz.push(0); nc.push(0);
        ids.push(s);
      }
      nx[s] += tx; ny[s] += ty; nz[s] += tz; nc[s]++;
      index[t * 3 + c] = s;
    }
  }
  const pos = new Float32Array(px.length * 3);
  const nor = new Float32Array(px.length * 3);
  for (let v = 0; v < px.length; v++) {
    pos[v * 3] = px[v]; pos[v * 3 + 1] = py[v]; pos[v * 3 + 2] = pz[v];
    let x = nx[v], y = ny[v], z = nz[v];
    const l = Math.hypot(x, y, z);
    if (l > 1e-12) { x /= l; y /= l; z /= l; }
    nor[v * 3] = x; nor[v * 3 + 1] = y; nor[v * 3 + 2] = z;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  geo.setAttribute('normal', new THREE.BufferAttribute(nor, 3));
  geo.setIndex(new THREE.BufferAttribute(index, 1));
  return geo;
}

export function buildGroup(bin, index) {
  const group = new THREE.Group();
  group.rotation.x = -Math.PI / 2;  // data is Z-up
  let off = 0;
  for (const p of index.parts) {
    const n = p.tris * 9;
    const f = new Float32Array(bin, off * 4, n);
    const geo = weldedGeometry(f);
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
