const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
const express  = require('express')

var app  = express()

const url = 'https://api.github.com/users'


fetch(url)
    .then((res) => res.json())
    .then((res) => console.log(res))


app.listen(3000)

