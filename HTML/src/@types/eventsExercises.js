"use strict";
//EventEmitter
console.log("inicio da aplicação");
const EventEmitter = require('events');
class Users extends EventEmitter {
    userLogged(data) {
        this.emit('User Logged', data);
    }
}
const users = new Users();
users.on('user Logged', data => {
    console.log(data);
});
const data = {
    user: 'pastel'
};
users.userLogged({
    user: 'pastel'
});
console.log(setTimeout(() => {
    console.log("parece que não iniciou nada rsrsrs");
}, 1000));
