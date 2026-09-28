// Node smoke test for the 3D preview scene: builds the real meshes from
// viewdata.bin and fails loudly on bad data, NaNs, or a broken camera
// fit. Run: node docs/preview/test_scene.mjs
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { buildGroup, frameCamera } from './scene.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const bin = readFileSync(join(here, 'viewdata.bin'));
const index = JSON.parse(readFileSync(join(here, 'viewdata-index.json'), 'utf8'));

const fail = (msg) => { console.error('SCENE TEST FAILED: ' + msg); process.exit(1); };

if (index.parts.length < 40) fail('expected the full part set, got ' + index.parts.length);
const totalTris = index.parts.reduce((s, p) => s + p.tris, 0);
if (totalTris < 50000) fail('mesh too thin: ' + totalTris + ' triangles');
const floats = totalTris * 9;
if (bin.byteLength !== floats * 4) fail('bin size ' + bin.byteLength + ' != ' + floats * 4);

for (let i = 0; i < floats; i += 97) {  // strided NaN / infinity scan
  const v = new Float32Array(bin, i * 4, 1)[0];
  if (!Number.isFinite(v)) fail('non-finite coordinate at float ' + i);
}

const group = buildGroup(bin.buffer, index);
if (group.children.length !== index.parts.length) fail('mesh count mismatch');

const { camera, center, size, maxDim } = frameCamera(group);
if (![center.x, center.y, center.z, camera.position.x, camera.position.y, camera.position.z].every(Number.isFinite))
  fail('non-finite camera fit');
if (maxDim < 150) fail('model too small: maxDim ' + maxDim);
const dist = camera.position.distanceTo(center);
if (dist < maxDim || dist > maxDim * 3) fail('camera distance ' + dist + ' implausible for maxDim ' + maxDim);
for (const mesh of group.children) {
  if (mesh.geometry.attributes.position.count < 3) fail('degenerate part: ' + mesh.uuid);
}

console.log('SCENE TEST OK: %d parts, %d tris, maxDim %.1f, camera %.1f from center',
  index.parts.length, totalTris, maxDim.toFixed(1), dist.toFixed(1));
