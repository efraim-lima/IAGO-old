//npm install --save node-fetch
//npm install --save cross-fetch
//npm install --save-dev nodemon
//npm install --save-dev tsconfig-paths
//npm install --save-dev ts-node-dev

import express, {Request, Response, NextFunction} from 'express'
const open = require ('open')
const http = require('http');
const fetch = require ('cross-fetch')
const host = 'http://localhost'
const port = 3000
const stats = require('./ram.js')

const app = express()

http.createServer((req:Request, res:Response, next:NextFunction)=> {
    let url =  req.url
    if (url === '/'){
      res.end('<h1> Working </h1>')
    }
    else if (url === '/stats'){
      res.end(JSON.stringify(stats, null, 2))
    }
}).listen(port, ()=> console.log(`Server Created in host ${host}:${port}, ${stats}`)) //localhost:3000

app.get('/status'), (req:Request, res:Response, next:NextFunction) => {
  res.status(200).send({foo:'bar'})
}

app.listen(port, () => {
  console.log('listening 3000 door')
})
