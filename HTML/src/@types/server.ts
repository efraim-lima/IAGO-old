//npm install --save node-fetch
//npm install --save cross-fetch
//npm install --save-dev nodemon
//npm install --save-dev tsconfig-paths
//npm install --save-dev ts-node-dev

import express, {Request, Response, NextFunction} from 'express'
import usersRout from "../routes/user.route"
const open = require ('open')
const http = require('http');
const fetch = require ('cross-fetch')
const host = 'http://localhost'
const port = 3000
const stats = require('./ram.js')

const app = express()

app.use(express.json())
app.use(express.urlencoded({ extended:true }))

http.createServer((req:Request, res:Response, next:NextFunction)=> {
  let url =  req.url
  
  app.use(usersRout)
  app.get('/stats'), (req:Request, res:Response, next:NextFunction) => {
    res.status(200).send({foo:'bar'})
  }
  
  app.listen(port, () => {
    console.log('listening 3000 door')
  })
    if (url === '/'){
      res.end('<h1> Working </h1>')
    }
    else if (url === '/stats'){
      res.end(JSON.stringify(stats, null, 2))
    }
}).listen(port, ()=> console.log(`Server Created in host ${host}:${port}, ${stats}`)) //localhost:3000
