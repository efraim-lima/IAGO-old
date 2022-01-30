// npm init
// npm i parcel-bundler
// npm install typescript
// sudo apt install node-typescript
// tsc
function soma(a:number, b:number){
    return a + b
}
console.log(soma(2,4))

interface Animal {
    nome: string
    tipo: 'terrestre'|'aquatico'
    executarRugido(alturaDb: number): void
}
interface Felino extends Animal {
    visaoNoturna: boolean
}

const animal : Animal = {
    nome: 'Elefante',
    tipo: 'terrestre',
    executarRugido: (alturaDb) => (${alturaDb})
}

const felino: Felino = {
    nome: 'Gato',
    tipo: 'terrestre',
    visaoNoturna: true
}