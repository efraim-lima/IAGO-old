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
Object.defineProperty(exports, "__esModule", { value: true });
//for XML and HTTP requests, this case we're getting a data.j   son from localhost/data.json
// const response = fetch('../../../content/pastel/pastel.json', {
//     method : 'post',
//     body : JSON.stringify()
// })
const response = fetch('../../../content/pastel/pastel.json')
    .then(responseStream => {
    console.log('Json Here!!!', responseStream);
    if (responseStream.status === 200) {
        return responseStream.json();
    }
    else {
        throw new Error('Request Error');
    }
})
    .then(data => {
    console.table(data);
})
    .catch(error => {
    console.log(error);
})
    // .then(v => Papa.parse(v))
    .catch(err => console.log(err));
//ES6 - Async/Await
const functionA = new Promise((resolve, reject) => {
    setTimeout(() => {
        var a = 200 * 2;
        console.log(a);
        resolve(a);
    });
});
const functionB = () => __awaiter(void 0, void 0, void 0, function* () {
    var waiting = yield functionA;
    var waitingJSON = yield fetch('../../../content/pastel/pastel.json')
        .then(data => {
        console.table(data);
        var pastel = data.json();
        console.log(pastel);
        return pastel;
    })
        .catch(error => {
        console.log(error);
    });
    var a = 'pastel';
    console.log(`Here we see the variable a: ${a}`);
    return waitingJSON;
});
functionB()
    .then(data => {
    console.table(data);
})
    .catch(error => {
    console.log(error);
});
