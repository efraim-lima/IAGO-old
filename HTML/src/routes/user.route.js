"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const http_status_codes_1 = require("http-status-codes");
// get /users
// get /users/:uuid
// post /users
// put /users/:uuid
// delete /users/:uuid
const usersRout = (0, express_1.Router)();
usersRout.get('/users', (req, res, next) => {
    const users = [{
            userName: 'Efraim'
        }];
    res.status(http_status_codes_1.StatusCodes.OK).send(users);
});
usersRout.get('/users/:uuid', (req, res, next) => {
    const uuid = req.params.uuid;
    //bancoDeDados.getUserByUuid(uuid)
    res.status(http_status_codes_1.StatusCodes.OK).send({ uuid });
});
usersRout.post('/users', (req, res, next) => {
    const newUser = req.body;
    res.status(http_status_codes_1.StatusCodes.CREATED).send(newUser);
});
usersRout.put('/users/:uuid', (req, res, next) => {
    const uuid = req.params.uuid;
    //bancoDeDados.getUserByUuid(uuid)
    const modifiedUser = req.body;
    modifiedUser.uuid = uuid;
    res.status(http_status_codes_1.StatusCodes.OK).send({ modifiedUser });
});
usersRout.delete('/users/:uuid', (req, res, next) => {
    res.sendStatus(http_status_codes_1.StatusCodes.OK);
});
exports.default = usersRout;
