import * as THREE from './three/build/three.module.js'
import {GLTFLoader} from './three/examples/jsm/loaders/GLTFLoader.js'
import {OrbitControls} from './three/examples/jsm/controls/OrbitControls.js'

//function init(){
    const canvas = document.querySelector(".webgl");
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xdddddd);

    const loader = new GLTFLoader();
    loader.load('./assets/wraith.glb', function(gltf){
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
    const hlight = new THREE.AmbientLight (0x404040,100);    
    dlight.position.set(0,1,0);
    dlight.castShadow = true;
    scene.add(dlight);
    scene.add(hlight);

    const light = new THREE.PointLight(0xc4c4c4,10);
    light.position.set(0,300,500);
    scene.add(light);

    const light2 = new THREE.PointLight(0xc4c4c4,10);
    light2.position.set(500,100,0);
    scene.add(light2);

    const light3 = new THREE.PointLight(0xc4c4c4,10);
    light3.position.set(0,100,-500);
    scene.add(light3);

    const light4 = new THREE.PointLight(0xc4c4c4,10);
    light4.position.set(-500,300,0);
    scene.add(light4);

    //COMENTAR CASO O GLTF NÃO FUNCIONE::
    const geometry = new THREE.BoxGeometry(1,1,1)
    const material = new THREE.MeshBasicMaterial({
        color: 0x00ff00
    })
    const boxMesh = new THREE.Mesh(geometry, material)
   
    //TERMINAR AQUI!!!

    //Boler plate Code
    const sizes = {
        width: window.innerWidth,
        height: window.innerHeight
    }

    const camera = new THREE.PerspectiveCamera(100, window.innerWidth, window.innerHeight, 0.1, 1000);
    camera.position.set(2,2,1);
    camera.rotation.y = 45/180*Math.PI;
    // camera.position.x = 1;
    // camera.position.y = 1;
    // camera.position.z = 1;
    scene.add(camera)
    scene.add(boxMesh)    

    const renderer = new THREE.WebGLRenderer({
        antialias: true,
        canvas: canvas
    })

    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
    renderer.shadowMap.enabled = true
    renderer.gammaOutput = true
    //renderer.outputEncoding = new THREE.SRGBEncoding

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