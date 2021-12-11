import * as THREE from './three/build/three.module.js'
import {GLTFLoader} from './three/examples/jsm/loaders/GLTFLoader.js'
import {OrbitControls} from './three/examples/jsm/controls/OrbitControls.js'

const canvas = document.querySelector("canvas");
const scene = new THREE.Scene();
const fov = 75; 
const aspect = 3; //estica ou desestica a imagem
const near = 0.001;
const far = 500; //ajuda a alterar a cena no eixo y
const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
//const camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1,400);
const renderer = new THREE.WebGLRenderer({
    alpha: true,
    antialias: true,
    canvas: canvas,
});
canvas.frustumCulled = false;

const axesHelper = new THREE.AxesHelper( 5 );
scene.add( axesHelper );


renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
renderer.shadowMap.enabled = true
renderer.gammaOutput = true
renderer.setClearColor( 0x000000, 0 );
//document.body.appendChild( renderer.domElement );
//document.addEventListener('mousemove', onDocumentMouseMove, false);


const geometry = new THREE.BoxBufferGeometry(1,1,1);
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
const boxMesh = new THREE.Mesh(geometry, material);
geometry.center();

//scene.background = new THREE.Color(0x000000, 0);
scene.add( canvas );


camera.position.set(1,1,1);
//camera.rotation.y = 45/180*Math.PI;
camera.position.x = 0;
camera.position.y = 0;
camera.position.z = 15;

const loader = new GLTFLoader();
loader.load('./assets/sun/scene.gltf', function(gltf){
    gltf.scene.traverse( function ( child ) {
        if ( child.isMesh ) {
            child.geometry.center(); // center here
        }
    });
    console.log(gltf);
    scene.add(gltf.scene);
    const root = gltf.scene;
    root.scale.set(10,10,10);
    gltf.scene.position.set(100,100,100);
    scene.add( gltf.scene );
    console.log(gltf.scene.children[0])
}, function(xhr){
    console.log((xhr.loaded/xhr.total * 100) + '% loaded')
}, function(error){
    console.log('texto falando do erro')
});

const geometryy = meshData[0];
loader.geometryy.center();

const dlight = new THREE.DirectionalLight(0xffffff, 1);
const hlight = new THREE.AmbientLight (0x404040,1);
scene.add(hlight);
scene.add(dlight);

// {
//     const loader = new THREE.CubeTextureLoader();
//     const texture = loader.load([
//       './img/space.png',
//     ]);
//     scene.background = texture;
//   }

//   const loaderTexture = new THREE.TextureLoader();
//   const texture = loaderTexture.load(
//     './img/background/space3.jpg',
//     () => {
//       const rt = new THREE.WebGLCubeRenderTarget(texture.image.height);
//       rt.fromEquirectangularTexture(renderer, texture);
//       scene.background = rt.texture;
//     });

const controls = new OrbitControls(camera, canvas);
controls.target.set(0,0,0);
controls.update();
// controls.minDistance = 10;
// controls.maxDistance = 50;



//window.addEventListener()

function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
    //canvas.rotation.x += 0.01;
    scene.rotation.y += 0.005;
}
animate();

// const modelDiv = document.getElementsByClassName('webgl');
// modelDiv.appendChild(renderer);
// renderer.setSize(modelDiv.offsetWidth, modelDiv.offsetHeight);
