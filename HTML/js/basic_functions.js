export function finishing(){
    const pessoa1 = {
        name : window.prompt("What's your name?"),
        age : Number(window.prompt('How old are you?')),
        sex : window.prompt("What's your sex?"),
        lastName : window.prompt("What's your last name?")
        };
    const pessoa2 = {
        name : window.prompt("What's your name?"),
        age : Number(window.prompt('How old are you?')),
        sex : window.prompt("What's your sex?"),
        lastName : window.prompt("What's your last name?")
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
}