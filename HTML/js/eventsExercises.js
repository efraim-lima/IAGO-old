//EventEmitter
const EventEmitter = require('events');
class Users extends EventEmitter {
    userLogged(data) {
        this.emit('User Logged', data)
    }
}
const users = new Users();

users.on('user Logged', data => {
    console.log(data)
})

const data ={
    user: 'pastel'
}

users.userLogged({
    user: 'pastel'
})