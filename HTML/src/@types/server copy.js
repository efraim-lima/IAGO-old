// npm install --save node-fetch
//npm install --save cross-fetch

const open = require ('open')
const http = require('http');
const fetch = require ('cross-fetch')
const host = 'http://localhost'
const port = 3000
import {withHar, createHarLog} from "node-fetch-har";
import nodeFetch from "node-fetch";


http.createServer((req,res)=>{
    res.end('<h1> Working </h1>')
}).listen(port, ()=> console.log(`Server Created in host ${host}:${port}`)) //localhost:3000



const url = 'https://instagram.com/jadepicon'

async function run() {
  const har = createHarLog();
  const fetch = withHar(nodeFetch, { har });

  await Promise.all([
    fetch("https://httpstat.us/200"),
    fetch("https://httpstat.us/200"),
    fetch("https://httpstat.us/200")
  ]);

  console.log(har);
}