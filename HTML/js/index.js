import * as THREE from './three/build/three.module.js'
import {GLTFLoader} from './three/examples/jsm/loaders/GLTFLoader.js'

const canvas = document.querySelector(".webgl")
const scene = new THREE.Scene()

const loader = new GLTFLoader()
loader.load('./assets/wraith.glb', function(glb){
    console.log(glb)
    const root = glb.scene;
    root.scale.set(0.1, 0.1, 0,1)
}, function(xhr){
    console.log((xhr.loaded/xhr.total * 100) + '% loaded')
}, function(error){
    console.log('texto falando do erro')
})

const light = new THREE.DirectionalLight(0xffffff, 1)
light.position.set(2,2,5)
scene.add(light)

//COMENTAR CASO O GLTF NÃO FUNCIONE::
// const geometry = new THREE.BoxGeometry(1,1,1)
// const material = new THREE.MeshBasicMaterial({
//     color: 0x00ff00
// })
// const boxMesh = new THREE.Mesh(geometry, material)
// scene.add(boxMesh)
//TERMINAR AQUI!!!

//Boler plate Code
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}

const camera = new THREE.PerspectiveCamera(75, sizes.width/sizes.height, 0.1, 100)
camera.position.set(1,1,1)
scene.add(camera)

const renderer = new THREE.WebGL1Renderer({
    canvas: canvas
})

renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
renderer.shadowMap.enabled = true
renderer.gammaOutput = true
//renderer.outputEncoding = new THREE.SRGBEncoding

function animate (){
    requestAnimationFrame(animate)
    renderer.render(scene, camera)
}

animate()