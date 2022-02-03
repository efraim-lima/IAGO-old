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
    const url = 'https://instagram.com/';
    const browser = yield puppeteer.launch({ headless: false });
    const page = yield browser.newPage();
    yield page.goto(url);
    const REQUIRED_ARGS = ['iago.develop', 'pasteldefrango'];
    // Login
    yield page.type("input[name='username']", REQUIRED_ARGS[0]);
    yield page.type("input[name='password']", REQUIRED_ARGS[1]);
    yield page.click('#loginbutton input');
    yield page.waitForNavigation();
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
