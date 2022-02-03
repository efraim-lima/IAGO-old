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
(() => __awaiter(void 0, void 0, void 0, function* () {
    const url = 'https://instagram.com/jadepicon';
    const browser = yield puppeteer.launch({
        headless: false,
        args: ['--no-sandbox']
    });
    const page = yield browser.newPage();
    yield page.goto(url, { waitUntil: "networkidle0" });
    yield page.waitFor(2500);
    const REQUIRED_ARGS = ['iago.develop', 'pasteldefrango'];
    yield page.click(`input[type="text"]`); // Da um click falso no input de login
    yield page.keyboard.type(REQUIRED_ARGS[0]); // digita uma string no input
    yield page.click('input[type="password"]'); //Da um click falso no input de sennha
    yield page.keyboard.type(REQUIRED_ARGS[1]); // digita uma string no input
    yield page.click(".L3NKy");
    yield page.waitFor(2500);
    yield page.click("button.aOOlW");
    yield page.click("nav a._2dbep.qNELH.kIKUG");
    yield page.waitForNavigation();
    let data = yield page.evaluate(() => {
        const infos = document.querySelectorAll(".g47SY");
        const posts = infos[0].textContent;
        const followers = infos[1].textContent;
        const following = infos[2].textContent;
        return {
            posts,
            followers,
            following,
        };
    });
    console.log(data);
    // Get cookies
    const cookies = yield page.cookies();
    console.log(JSON.stringify(cookies));
    // Use cookies in other tab or browser
    const page2 = yield browser.newPage();
    yield page2.setCookie(...cookies);
    yield page2.goto('https://instagram.com'); // Opens page as logged user
    yield browser.close();
    console.log('Done.');
}))();
