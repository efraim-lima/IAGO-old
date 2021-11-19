import * as THREE from './three/build/three.module.js'
import {GLTFLoader} from './three/examples/jsm/loaders/GLTFLoader.js'

//function init(){
function animate (){
    const canvas = document.querySelector(".webgl");
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xdddddd);

    const loader = new GLTFLoader();
    loader.load('./assets/wraith.glb', function(gltf){
        console.log(gltf);
        scene.add(gltf.scene);
        const root = gltf.scene;
        root.scale.set(0.2, 0.2, 0,2)
    }, function(xhr){
        console.log((xhr.loaded/xhr.total * 100) + '% loaded')
    }, function(error){
        console.log('texto falando do erro')
    })

    const light = new THREE.DirectionalLight(0xffffff, 1)
    const hlight = new THREE.AmbientLight (0x404040,100)
    scene.add(hlight)  
    light.position.set(2,2,5)
    scene.add(light)

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

    const camera = new THREE.PerspectiveCamera(150, window.innerWidth/window.innerHeight, 1, 5000)
    camera.position.set(1,1,1)
    scene.add(camera)

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
// }
// init()


    requestAnimationFrame(animate)
    renderer.render(scene, camera)
}

animate()