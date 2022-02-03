"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const THREE = __importStar(require("./three/build/three.module.js"));
const GLTFLoader_js_1 = require("./three/examples/jsm/loaders/GLTFLoader.js");
const OrbitControls_js_1 = require("./three/examples/jsm/controls/OrbitControls.js");
const canvas = document.querySelector("canvas");
const scene = new THREE.Scene();
const fov = 85;
const aspect = 1; //estica ou desestica a imagem
const near = 1;
const far = 400; //ajuda a alterar a cena no eixo y
const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
//const camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1,400);
const renderer = new THREE.WebGLRenderer({
    alpha: true,
    antialias: true,
    canvas: canvas,
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.gammaOutput = true;
//document.body.appendChild( renderer.domElement );
//document.addEventListener('mousemove', onDocumentMouseMove, false);
const geometry = new THREE.BoxBufferGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
const boxMesh = new THREE.Mesh(geometry, material);
//scene.background = new THREE.Color(0x000000, 0);
scene.add(canvas);
//camera.position.set(1,1,1);
//camera.rotation.y = 45/180*Math.PI;
camera.position.x = 1;
camera.position.y = 1;
camera.position.z = 24;
const loader = new GLTFLoader_js_1.GLTFLoader();
loader.load('./assets/earth/scene.gltf', function (gltf) {
    console.log(gltf);
    scene.add(gltf.scene);
    const root = gltf.scene;
    root.scale.set(34, 34, 34);
    gltf.scene.position.set(1, 1, 1);
    scene.add(gltf.scene);
    console.log(gltf.scene.children[0]);
}, function (xhr) {
    console.log((xhr.loaded / xhr.total * 100) + '% loaded');
}, function (error) {
    console.log('texto falando do erro');
});
const dlight = new THREE.DirectionalLight(0xffffff, 1);
const hlight = new THREE.AmbientLight(0x404040, 3);
scene.add(hlight);
scene.add(dlight);
// {
//     const loader = new THREE.CubeTextureLoader();
//     const texture = loader.load([
//       './img/space.png',
//     ]);
//     scene.background = texture;
//   }
const loaderTexture = new THREE.TextureLoader();
const texture = loaderTexture.load('./img/background/space3.jpg', () => {
    const rt = new THREE.WebGLCubeRenderTarget(texture.image.height);
    rt.fromEquirectangularTexture(renderer, texture);
    scene.background = rt.texture;
});
const controls = new OrbitControls_js_1.OrbitControls(camera, canvas);
controls.target.set(0, 0, 0);
controls.update();
controls.minDistance = 10;
controls.maxDistance = 50;
const section = renderer.domElement;
camera.aspect = section.clientWidth / section.clientHeight;
camera.updateProjectionMatrix();
//window.addEventListener()
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    //canvas.rotation.x += 0.01;
    scene.rotation.y += 0.005;
}
animate();
// const modelDiv = document.getElementsByClassName('webgl');
// modelDiv.appendChild(renderer);
// renderer.setSize(modelDiv.offsetWidth, modelDiv.offsetHeight);
