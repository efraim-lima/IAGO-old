//import { finishing } from "./basic_functions.js";

const theme = window.prompt('Learn to search your theme. What theme shoud you wanna know about?') //aparece um popup com input
window.alert('Your theme is:' + theme) //aparece um popup
const views = Number(window.prompt('How many views in your video?'))
const likes = Number(window.prompt("how many likes in your video?"))
// const price = likes.toLocaleString('pt-BR', {style:'currency', currency:'BRL'}) // brincando de converter para moedas
//window.alert(`Have you ${views} views and ${likes} likes?`)

//normalfunction
function variablesSum(views, likes){
    const final = views + likes
    return final
}

//in arrow function
var sum = (views, likes) => views + likes

variablesSum(views, likes)
sum(views, likes)

document.onload(`<h2>Your Theme analysis <br> </h2>`)
document.onload(`<p>Your theme is <b>${theme.toString().toUpperCase()}</b> <br></p>`)
document.onload(`<p>You have ${views} views<br></p>`)
document.onload(`<p>You have ${likes} likes</p>`)
document.onload(`Your variable sum is ${variablesSum}`)
console.log(theme)
window.confirm('Im doing a research') //aparece outro popup, só que pode cancelar

//finishing()