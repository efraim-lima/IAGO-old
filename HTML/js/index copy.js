import * as THREE from './three/build/three.module.js'
import {GLTFLoader} from './three/examples/jsm/loaders/GLTFLoader.js'
import {OrbitControls} from './three/examples/jsm/controls/OrbitControls.js'

const canvas = document.querySelector(".webgl");
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1,400);
const renderer = new THREE.WebGLRenderer({
    alpha: true,
    antialias: true,
    canvas: canvas
});

renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
renderer.shadowMap.enabled = true
renderer.gammaOutput = true
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxBufferGeometry(2,2,2);
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
const boxMesh = new THREE.Mesh(geometry, material)


scene.background = new THREE.Color(0x000000, 0);
scene.add( canvas );


//camera.position.set(1,1,1);
//camera.rotation.y = 45/180*Math.PI;
// camera.position.x = 1;
// camera.position.y = 1;
camera.position.z = 5;

const loader = new GLTFLoader();
loader.load('./assets/skateboard.gltf', function(gltf){
    console.log(gltf);
    scene.add(gltf.scene);
    const root = gltf.scene;
    root.scale.set(0.1, 0.1, 0.1)
}, function(xhr){
    console.log((xhr.loaded/xhr.total * 100) + '% loaded')
}, function(error){
    console.log('texto falando do erro')
});

const dlight = new THREE.DirectionalLight(0xffffff, 1);
const hlight = new THREE.AmbientLight (0x404040,3);
scene.add(hlight)
scene.add(dlight)

// const controls = new OrbitControls(camera, cube);
// controls.update();

function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
    canvas.rotation.x += 0.01;
    canvas.rotation.y += 0.01;
}
animate();