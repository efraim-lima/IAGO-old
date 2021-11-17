const pessoa1 = {
    name : "Jorge",
    age : 25,
    sex : "male",
    lastName : "Silva"
};
const pessoa2 = {
    name: "Paula",
    age: 40,
    sex: "female",
    lastName: "Ubuntu"
};

let pastel = "pastel de Madeira Viva";
var cocaCola = "Coca cola de pastel";

function change(){
    let pastel = "melancia";
    var cocaCola = "suco de laranja";
    console.log(pessoa1.name + " bebe " + cocaCola);
    console.log(pessoa1.name + " come " + pastel);
    console.log(pessoa2.name + " bebe " + cocaCola)
    console.log(pessoa2.name + " come " + pastel);
};
change()

console.log(pessoa1.name + " come " + pastel);
console.log(pessoa1.name + " bebe " + cocaCola);
console.log(pessoa2.name + " come " + pastel);
console.log(pessoa2.name + " bebe " + cocaCola)