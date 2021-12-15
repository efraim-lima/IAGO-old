//import { finishing } from "./basic_functions.js";

const theme = window.prompt('Learn to search your theme. What theme shoud you wanna know about?') //aparece um popup com input
window.alert(`Your theme is: ${theme}`) //aparece um popup
const views = Number(window.prompt('How many views in your video?'))
const likes = Number(window.prompt("how many likes in your video?"))
// const price = likes.toLocaleString('pt-BR', {style:'currency', currency:'BRL'}) // brincando de converter para moedas
window.alert(`Have you ${views} views and ${likes} likes?`)

const data = {
    theme,
    views,
    likes
}
console.log(`Our data collected: Theme = ${data.theme}, Views = ${data.views}, Likes = ${data.likes}`)

//using random variable for cluster in future
function randomVar(){
    return Math.random() * 10
}
console.log(randomVar())

//normalfunction
function variablesSum(views, likes){
    const final = views + likes
    //clustering variables (mantaining 'b' randomize variable as backup) and calculating some variable that we can need in future
    var calculating = (final, va = randomVar()) => (final * va) * 0.1
    console.log(calculating(final))
    return calculating(final)
}

//in arrow function
var sum = (views, likes) => views + likes

console.log(variablesSum(views, likes))
console.log(sum(views, likes))

//tying to log elements in html (I now that this is the wrong way rsrsrs)
// document.onload(`<h2>Your Theme analysis <br> </h2>`)
// document.onload(`<p>Your theme is <b>${theme.toString().toUpperCase()}</b> <br></p>`)
// document.onload(`<p>You have ${views} views<br></p>`)
// document.onload(`<p>You have ${likes} likes</p>`)
// document.onload(`Your variable sum is ${variablesSum}`)
console.log(theme)
window.confirm('Im doing a research') //aparece outro popup, só que pode cancelar

//finishing()