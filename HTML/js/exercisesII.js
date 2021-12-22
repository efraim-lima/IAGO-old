import {data} from "./exercises.js"

//for XML and HTTP requests, this case we're getting a data.j   son from localhost/data.json

// const response = fetch('../../../content/pastel/pastel.json', {
//     method : 'post',
//     body : JSON.stringify()
// })

const response = fetch('../../../content/pastel/pastel.json')
    .then(responseStream => {
        console.log('Json Here!!!',responseStream)
        if (responseStream.status === 200){
            return responseStream.json()
        } 
        else {
            throw new Error('Request Error')
        }
    })
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.log(error)
    })
    // .then(v => Papa.parse(v))
    .catch(err => console.log(err))

//ES6 - Async/Await

const functionA = new Promise ((resolve, reject) => {
    setTimeout(() => {
        var a = 200 * 2
        console.log(a)
        resolve(a)
    })
})

const functionB = async () => {
    var waiting = await functionA
    var waitingJSON = await fetch('../../../content/pastel/pastel.json')
        .then(data => {
            console.log(data)
            var pastel = data.json()
            console.log(pastel)
            return pastel
        })
        .catch(error => {
            console.log(error )
        })
    var a = 'pastel'
    console.log(`Here we see the variable a: ${a}`)
    return waitingJSON
}

functionB()
    .then(data =>{
        console.log(data)
    })
    .catch(error => {
        console.log(error)
    })