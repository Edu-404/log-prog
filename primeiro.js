// começar definindo uma variavel
// analogia de variavel: gaveta
// a depender da linguagem "rotulo" seria
// uma analogia mais indicada

// idade = 18;
// console.log(idade)
// metodos de exibição
// java -> system.out.println(idade);
// js -> console.log(idade)
// c -> print("%d", idade);
// python -> print(idade)
// PHP -> echo($idade);

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const hand = ["pedra", "papel", "tesoura"];

function randNumber() {
    return Math.floor(Math.random() * hand.length);
}

rl.question("Escolha sua mão: ", (userHand) => {

    let machineHand = hand[randNumber()];

    console.log(userHand + " vs " + machineHand);

    if (userHand === "pedra" && machineHand === "papel") {
        console.log("Papel ganha!");
    }
    else if (userHand === "pedra" && machineHand === "tesoura") {
        console.log("Pedra ganha!");
    }
    else if (userHand === "papel" && machineHand === "tesoura") {
        console.log("Tesoura ganha!");
    }
    else if (userHand === "papel" && machineHand === "pedra") {
        console.log("Papel ganha!");
    }
    else if (userHand === "tesoura" && machineHand === "pedra") {
        console.log("Pedra ganha!");
    }
    else if (userHand === "tesoura" && machineHand === "papel") {
        console.log("Tesoura ganha!");
    }
    else {
        console.log("Empate!");
    }

    rl.close();
});
