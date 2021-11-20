import * as THREE from './three/build/three.module.js'
import {GLTFLoader} from './three/examples/jsm/loaders/GLTFLoader.js'
import {OrbitControls} from './three/examples/jsm/controls/OrbitControls.js'

//function init(){
    const canvas = document.querySelector(".webgl");
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xdddddd);

    const camera = new THREE.PerspectiveCamera(70, window.innerWidth, window.innerHeight, 1,400);
    camera.position.set(1,1,1);
    camera.rotation.y = 45/180*Math.PI;
    // camera.position.x = 1;
    // camera.position.y = 1;
    camera.position.z = 5;
    scene.add(camera)
    
    const renderer = new THREE.WebGLRenderer({
        alpha: true,
        antialias: true,
        canvas: canvas
    })    
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
    renderer.shadowMap.enabled = true
    renderer.gammaOutput = true
    //renderer.outputEncoding = new THREE.SRGBEncoding

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
    })

    const dlight = new THREE.DirectionalLight(0xffffff, 1);
    const hlight = new THREE.AmbientLight (0x404040,1);    
    // dlight.position.set(0,1,0);
    // dlight.castShadow = true;
    scene.add(dlight);
    scene.add(hlight);


    //COMENTAR CASO O GLTF NÃO FUNCIONE::
    const geometry = new THREE.BoxGeometry(1,1,1)
    const material = new THREE.MeshBasicMaterial({
        color: 0x00ff00
    })
    const boxMesh = new THREE.Mesh(geometry, material)
    scene.add(boxMesh)   
   
    //TERMINAR AQUI!!!

    //Boler plate Code
    const sizes = {
        width: window.innerWidth,
        height: window.innerHeight
    }

    const controls = new OrbitControls(camera, canvas);
    controls.update();
// }
// init()

function animate (){
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}

animate()