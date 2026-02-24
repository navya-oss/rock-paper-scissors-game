let userScore = 0;
let compScore = 0;

const choices = document.querySelectorAll(".choice");
const msg = document.querySelector("#msg");

const userScorepara = document.querySelector("#user-score");
const compScorepara = document.querySelector("#comp-score");

const genCompChoice = () => {
    const options = ["rock", "paper", "scissors"];
    const randIdx = Math.floor(Math.random() * 3);
    return options[randIdx];
    
};

const drawGame = () => {
    console.log("Draw Match");
    para.textContent = "Game was drawGame, play agian";
    para.style.background = "#081b31";
 
};

const showWinner = (userWin) => {
    if(userWin) {
        userScore++;
        userScorepara.textContent = userScore;
        msg.textContent = 'you won!';
        msg.style.background = "green";
    } else {
        compScore++;
        compScorepara.textContent = compScore;
        msg.textContent = 'you lose.';
        msg.style.background = "red";
        
    }
}

const playGame = (userChoice) => {
    console.log("user choice =", userChoice);
    //generate comp choice
    const compChoice = genCompChoice();
    console.log("comp choice =", compChoice);
    if(userChoice === compChoice) {
      drawGame();
    } else {
        let userWin = true;  
        if(userChoice === "rock") {
            userWin = compChoice === "paper" ? false : true;
        } else if(userChoice === "paper"){
            userWin = compChoice === "scissors" ? false : true
        } else {
            userWin = compChoice === "rock" ? false : true;
        }
      showWinner(userWin);
      }
}

choices.forEach((choice) => {
    choice.addEventListener("click", () => {
        const userChoice = choice.getAttribute("id");
        playGame(userChoice);
    });
});