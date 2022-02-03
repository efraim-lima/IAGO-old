"use strict";
// const puppeteer = require('puppeteer')
// (async () => {
//   try{
//     const browser = await puppeteer.launch({
//       userDataDir: "./cache",
//       args: ["--proxy-server=103.161.164.109:8181",
//             "--no-sandbox",
//             "--disable-setuid-sandbox", 
//             "--disable-dev-shm-usage", 
//             "--disable-gpu" ]
//     })
//     /* 
//     https://freeproxylists.net/
//     103.161.164.109   8181
//     206.253.164.110   80
//     139.99.237.62     80
//     190.26.201.194    8080
//     185.255.46.121    8080
//     164.70.119.208    3128
//     223.29.214.6      80
//     */
//     const page = await browser.newPage()
//     const pageUrl = 'https://whatsmyipaddress.com/'
//     await page.goto(pageUrl)
//     await page.authenticate({
//       username: "iago.develop",
//       password: "pasteldefrango"
//     })
//     page.setRequestInterception(true)
//     page.on('request', req => {
//       if(req.url().endsWith(".png")){
//         req.abort()
//       }
//       else {
//         req.continue()
//       }
//     })
//     page.on('error', e => console.log(e))
//     await page.goto('https://instagram.com')
//     await browser.close()
//   }
//   catch(e){
//     console.log(e)
//   }
// })()
// proxy_server.js
const ProxyChain = require('proxy-chain');
const server = new ProxyChain.Server({
    // Port where the server will listen. By default 8000.
    port: 8000,
    // Enables verbose logging
    verbose: true,
    prepareRequestFunction: ({ request, username, password, hostname, port, isHttp, connectionId }) => {
        let upstream_proxy = request.headers['x-no-forward-upstream-proxy'];
        if (!upstream_proxy) {
            throw Error('please set header `x-no-forward-upstream-proxy`');
        }
        return {
            upstreamProxyUrl: upstream_proxy,
        };
    },
});
server.listen(() => {
    console.log(`Proxy server is listening on port ${server.port}`);
});
// Emitted when HTTP connection is closed
server.on('connectionClosed', ({ connectionId, stats }) => {
    console.log(`Connection ${connectionId} closed`);
    console.dir(stats);
});
// Emitted when HTTP request fails
server.on('requestFailed', ({ request, error }) => {
    console.log(`Request ${request.url} failed`);
    console.error(error);
});
