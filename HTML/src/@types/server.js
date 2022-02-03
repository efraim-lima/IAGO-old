"use strict";
//npm install --save node-fetch
//npm install --save cross-fetch
//npm install --save-dev nodemon
//npm install --save-dev tsconfig-paths
//npm install --save-dev ts-node-dev
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const user_route_1 = __importDefault(require("../routes/user.route"));
const open = require('open');
const http = require('http');
const fetch = require('cross-fetch');
const host = 'http://localhost';
const port = 3000;
const stats = require('./ram.js');
const app = (0, express_1.default)();
app.use(express_1.default.json());
app.use(express_1.default.urlencoded({ extended: true }));
http.createServer((req, res, next) => {
    let url = req.url;
    app.use(user_route_1.default);
    app.get('/stats'), (req, res, next) => {
        res.status(200).send({ foo: 'bar' });
    };
    app.listen(port, () => {
        console.log('listening 3000 door');
    });
    if (url === '/') {
        res.end('<h1> Working </h1>');
    }
    else if (url === '/stats') {
        res.end(JSON.stringify(stats, null, 2));
    }
}).listen(port, () => console.log(`Server Created in host ${host}:${port}, ${stats}`)); //localhost:3000
