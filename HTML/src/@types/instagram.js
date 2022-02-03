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
const puppeteer = require('puppeteer');
const argv = require('minimist')(process.argv.slice(2));
const fs = require('fs');
const REQUIRED_ARGS = ['iago.develop', 'pasteldefrango'];
const INSTAGRAM_LOGIN_URL = 'https://instagram.com/accounts/login';
const INSTAGRAM_URL = 'https://instagram.com/';
(() => __awaiter(void 0, void 0, void 0, function* () {
    const browser = yield puppeteer.launch({ headless: false });
    const page = yield browser.newPage();
    yield page.goto(INSTAGRAM_URL + 'jadepicon');
    const ls = yield page.evaluate(() => JSON.stringify(localStorage));
    yield page.evaluate(() => {
        const nodeList = document.querySelectorAll('article img');
        const imgArray = [...nodeList];
        const List = imgArray.map(img => {
            return { src: img };
        });
        console.log(List);
    });
    yield browser.close();
}))();
