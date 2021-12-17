//import { finishing } from "./basic_functions.js";

const theme = window.prompt('Learn to search your theme. What theme shoud you wanna know about?') //aparece um popup com input
window.alert(`Your theme is: ${theme}`) //aparece um popup
const views = Number(window.prompt('How many views in your video?'))
const likes = Number(window.prompt("how many likes in your video?"))
const subscribers = Number(window.prompt("how many subscribers in your channel?"))
const videos = Number(window.prompt("how many videos in your channel?"))
// const price = likes.toLocaleString('pt-BR', {style:'currency', currency:'BRL'}) // brincando de converter para moedas
window.alert(`Have you ${views} views and ${likes} likes?`)

const data = {
    theme,
    views,
    likes,
    subscribers,
    videos
}
console.log(data)


//total sum without rest operator
function filtering(views, likes) {
    var value = 0;
    for (var i=0; i<arguments.length; i++) {
        value += arguments[i];
    }
    return value;
}
console.log(filtering(data.views,data.likes, data.subscribers, data.videos))


//total sum with rest operator
function filteringRest(...args){
    return args.reduce((acc, values) => acc + values, 0)
}
console.log(filteringRest(data.views,data.likes, data.subscribers, data.videos))


//total sum with rest operator pt2
const filteringTook = (...args) => args.reduce((acc, values) => acc * values, 1)
const taking = (...rest) => {
    return filteringTook.apply(undefined, rest)
}
console.log(taking(data.views,data.likes, data.subscribers, data.videos))

const lista = [data.views,data.likes, data.subscribers, data.videos]
//total sum with rest and spread operator pt2
const filteringTook2 = (...args) => args.reduce((acc, values) => acc * values, 1)
const taking2 = (...rest) => {
    return filteringTook2(...rest)
}
console.log(taking2(data.views,data.likes, data.subscribers, data.videos))


//Rest operator with strings and objects
function wordBroke(){
    console.log(arguments)
}
wordBroke(...theme)
wordBroke(...lista)
const data2 = {
    ...data,
    channel: "pastel de frango"
}
console.log(data2)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//arrays
var [theme2, likes2, [views2, comments2]] = [data.theme, data.likes, [data.views, data.comments]]
console.log(`Here we have elements from an array: theme2: ${theme2}, likes2: ${likes2}`)
console.log(`Here we have an array inside another array: views2: ${views2}, Comments2: ${views2[1]}`)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

var arrayo = [data.views,data.likes, data.subscribers, data.videos]
const it = arrayo[Symbol.iterator]()
// const a_coisa = arrayo[Symbol.split]()
// const palhaço = arrayo[Symbol.toStringTag]()
console.log(`iterator: ${it}`)
// console.log(`split: ${a_coisa}`)
// console.log(`toStringTag: ${palhaço}}`)

//Symbols and Iterators
//Well known symbols
Symbol.iterator;
Symbol.split;
Symbol.toStringTag;

//it run in all the data structure
while (true) {
    let {value, done} = it.next()

    if(done){
        break
    }
    console.log(value)
}

//how we can work, but we can not do this in a object...
for (let value of arrayo){
    console.log(value)
}

//using Symbols in a object
const data3 = {
    followers: [10, 20, 40, 10],
    [Symbol.iterator](){
        let i = 0

        return{
            next: () => {
                i++
                return {
                    value: this.followers[i-1],
                    done: i > this.followers.length 
                }
            }
        }
    }
}

const it2 = data3[Symbol.iterator]()
console.log(it2.next())
console.log(it2.next())
console.log(it2.next())
console.log(it2.next())

//using "for of"
for (let newValue in data3.values){
    console.log(newValue)
}

//Generators
function* printData(){
    console.log(data.views)
    yield 1 //it put a value indicator in consoloe
    console.log(`printing data ${data}`)
    yield 2 //it put a value indicator in consoloe
    console.log(`printing randomic stuff ${data.followers}`)
    const outside = yield 3 //it put a value indicator in consoloe
    console.log(outside)
}

const batata = printData()
console.log(batata.next())
console.log(batata.next())
console.log(batata.next("I don't now what I really did here!!!"))

//constructing a new array
const arrayoNew = [...data3]

//don't works the way above
console.log(`Aqui está uma maneira que não funciona: iter ${it2.next()}`) 


console.log(`Our data collected: Theme = ${data.theme}, Views = ${data.views}, Likes = ${data.likes}`)

//Generators2
const data4 = {
    followers: [10, 20, 40, 10],
    *[Symbol.iterator](){
        for (i = 0; i < this.followers.length; i++){
            yield this.followers[i]
        }
    }
}

for (let valueNext in data4){
    console.log(valueNext)
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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