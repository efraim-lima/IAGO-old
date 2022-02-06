"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// program
const puppeteer = require('puppeteer');
const fs = require('fs');
const cookiesPath = "HTML/src/@types/cookies/cookies.txt";
((profile) => __awaiter(void 0, void 0, void 0, function* () {
    const url = 'https://instagram.com/' + profile;
    // const cookie = [{
    //   name: 'IAGO_dev',
    //   value: 'iago.develop',
    //   domain: '.instagram.com',
    //   httpOnly: true,
    //   secure: true,
    // },
    // {
    //   name: 'IAGO_dev2',
    //   value: 'iago.develop',
    //   domain: '.instagram.com',
    //   httpOnly: true,
    //   secure: true,
    // }
    // ]
    const REQUIRED_ARGS = ['iago.develop', 'pasteldefrango'];
    const chromeOptions = {
        headless: false,
        slowMo: 10,
        defaultViewport: null,
        args: [
            "--no-sandbox",
            "--disable-setuid-sandbox"
        ],
    };
    const browser = yield puppeteer.launch(chromeOptions);
    const page = yield browser.newPage();
    const userAgent = "Mozilla/5.0 (X11; Linux x86_64)" +
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36";
    yield page.setUserAgent(userAgent);
    // If the cookies file exists, read the cookies.
    const previousSession = fs.existsSync(cookiesPath);
    if (previousSession) {
        const content = fs.readFileSync(cookiesPath);
        const cookiesArr = JSON.parse(content);
        if (cookiesArr.length !== 0) {
            for (let cookie of cookiesArr) {
                yield page.setCookie(cookie);
            }
            console.log('Cookie has been loaded in the browser');
        }
    }
    yield page.goto(url, { waitUntil: "networkidle0" });
    //await page.waitFor(2500)
    // Write Cookies
    const cookiesObject = yield page.cookies();
    fs.writeFileSync(cookiesPath, JSON.stringify(cookiesObject));
    console.log('Session has been saved to ' + cookiesPath);
    try {
        const entrar = page.waitForSelector('button.sqdOP.L3NKy.y3zKF');
        yield page.click(entrar);
        yield page.click(`input[type="text"]`); // Da um click falso no input de login
        yield page.keyboard.type(REQUIRED_ARGS[0]); // digita uma string no input
        yield page.click('input[type="password"]'); //Da um click falso no input de sennha
        yield page.keyboard.type(REQUIRED_ARGS[1]); // digita uma string no input
        yield page.click(".L3NKy");
        //await page.waitFor(2500);
        yield page.click("button.aOOlW");
        yield page.click("nav a._2dbep.qNELH.kIKUG");
        yield page.waitForNavigation();
        // Get cookies
        const cookies = yield page.cookies();
        console.log(JSON.stringify(cookies));
        // Use cookies in other tab or browser
        const page2 = yield browser.newPage();
        yield page2.goto('https://instagram.com/');
        // await page2.setCookie(... cookie);//aqui temos os cookies que estão comentados no topo da página
        const cookiesString = yield fs.readFile('./cookies/cookies.json');
        const cookieless = JSON.parse(cookiesString);
        yield page.setCookie(...cookieless);
    }
    catch (e) {
        yield page.click(`input[type="text"]`); // Da um click falso no input de login
        yield page.keyboard.type(REQUIRED_ARGS[0]); // digita uma string no input
        yield page.click('input[type="password"]'); //Da um click falso no input de sennha
        yield page.keyboard.type(REQUIRED_ARGS[1]); // digita uma string no input
        yield page.click(".L3NKy"); // click no Login
        // const cookies = await page.cookies();
        // await fs.writeFile('./cookies/cookies.json', JSON.stringify(cookies, null, 2));
        // console.log(JSON.stringify(cookies))
        //await page.waitForXPath('//*[@id="react-root"]/section/main/div/div/div/section/div/button');
        yield page.click('//*[@id="react-root"]/section/main/div/div/div/section/div/button');
        // Get cookies
        // await page.click("button .sqdOP.L3NKy.y3zKF");
        //await page.click("nav a._2dbep.qNELH.kIKUG");
        yield page.waitForNavigation();
        // Use cookies in other tab or browser
        const page2 = yield browser.newPage();
        yield page2.goto('https://instagram.com/'); // Opens page as logged user
        const cookiesString = yield fs.readFile('./cookies/cookies.json');
        const cookieless = JSON.parse(cookiesString);
        yield page.setCookie(...cookieless);
        yield browser.close();
        console.log(e);
    }
    finally {
        let data = yield page.evaluate(() => {
            const name = document.querySelector('.Yk1V7').textContent;
            const bio = document.querySelector('.QGPIr');
            const category = document.querySelector('._829vi');
            const description = document.querySelector('.QGPIr span');
            const link = document.querySelector('.heKAw');
            const infos = document.querySelectorAll(".g47SY");
            const posts = infos[0].textContent;
            const followers = infos[1].textContent;
            const following = infos[2].textContent;
            return {
                name,
                category,
                description,
                link,
                bio,
                posts,
                followers,
                following,
            };
        });
        console.log(data);
    }
    console.log('Done.');
}))('jadepicon');
