// npm install --save node-fetch
//npm install --save cross-fetch

const open = require ('open')
const http = require('http');
const fetch = require ('cross-fetch')
const host = 'http://localhost'
const port = 3000
const stats = require('./ram.js')


http.createServer((req,res)=>{
    let url =  req.url
    if (url === '/'){
      res.end('<h1> Working </h1>')
    }
    else if (url === '/stats'){
      res.end(JSON.stringify(stats, null, 2))
    }
}).listen(port, ()=> console.log(`Server Created in host ${host}:${port}, ${stats}`)) //localhost:3000