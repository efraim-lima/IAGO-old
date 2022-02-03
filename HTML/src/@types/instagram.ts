const puppeteer = require('puppeteer');
const argv = require('minimist')(process.argv.slice(2));
const fs = require('fs');

const REQUIRED_ARGS = ['iago.develop', 'pasteldefrango'];
const INSTAGRAM_LOGIN_URL = 'https://instagram.com/accounts/login';
const INSTAGRAM_URL = 'https://instagram.com/';


(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(INSTAGRAM_URL + 'jadepicon');
  const ls = await page.evaluate(() => JSON.stringify(localStorage))
  await page.evaluate(() => {
        const nodeList = document.querySelectorAll('article img')
        const imgArray = [...nodeList]
        const List = imgArray.map( img => {
            return {src: img}
        })
    console.log(List)
  });


  await browser.close();
})();