//EventEmitter
const EventEmitter = require('events');
const emitter = new EventEmitter();

emitter.on('user Logged', data => {
    console.log(data)
})
emitter.emit('User Logged', {user: 'pastel'})