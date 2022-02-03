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
const proxyChain = require('proxy-chain');
const proxyII = (() => __awaiter(void 0, void 0, void 0, function* () {
    const oldProxyUrl = 'http://proxyuser:proxypassword@100.100.100.100:3128';
    const newProxyUrl = yield proxyChain.anonymizeProxy(oldProxyUrl);
    const browser = yield puppeteer.launch({
        headless: false,
        args: [`--proxy-server=${newProxyUrl}`],
    });
    // Do your magic here...
    const page = yield browser.newPage();
    yield page.goto('https://www.websocket.org/echo.html');
    // oh wait a minute
    yield page.waitFor(60000);
    yield browser.close();
    // Clean up
    yield proxyChain.closeAnonymizedProxy(newProxyUrl, true);
}))();
