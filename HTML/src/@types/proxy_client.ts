const puppeteer = require('puppeteer');
const proxyChain = require('proxy-chain');
const proxyII = 

(async() => {
  const oldProxyUrl = 'http://proxyuser:proxypassword@100.100.100.100:3128';
  const newProxyUrl = await proxyChain.anonymizeProxy(oldProxyUrl);

  const browser = await puppeteer.launch({
    headless: false,
    args: [`--proxy-server=${newProxyUrl}`],
  });

  // Do your magic here...
  const page = await browser.newPage();
  await page.goto('https://www.websocket.org/echo.html');

  // oh wait a minute
  await page.waitFor(60000);

  await browser.close();
  // Clean up
  await proxyChain.closeAnonymizedProxy(newProxyUrl, true);
})();