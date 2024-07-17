import random

#created the class 
class RockPaperScrissors:
    #initialized the constructor
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.stats = {
            "wins": 0,
            "losses": 0, 
            "ties": 0
        }

    #getting the computers choice from the constructor
    def getComputerChoice(self):
        return random.choice(self.choices)
    #getting the players choice and checking for valid answer
    def getPlayerChoice(self):
        choice = input("Enter rock, paper or scissors (or quit if you want to exit)").strip().lower()
        while choice not in self.choices and choice != "quit":
            choice = input("Invalid answer, please enter rock, paper or scissors").strip().lower()
        return choice
    #this method is used for seeing who will win depending on the input of the player and the random choice of the computer
    def determineWinner(self, playerChoice, computerChoice):
        if playerChoice == computerChoice:
            self.stats["ties"] += 1
            print("It's a tie! Here are your current stats: {stats}".format(stats=self.stats))

        elif playerChoice == "rock" and computerChoice == "paper" or playerChoice == "scissors" and computerChoice == "paper" or playerChoice == "scissors" and computerChoice == "paper":
            self.stats["wins"] += 1
            print("You win! Your current stats are: {stats}".format(stats=self.stats))

        else:
            self.stats["losses"] += 1
            print("You lose! here are your current stats: {stats}".format(stats=self.stats))

        #the method that lets you play the game itself    
    def play(self):
        print("Welcome to rock, paper, scissors!")
        while True:
            playerChoice = self.getPlayerChoice()
            if playerChoice == "quit":
                print("Thanks for playing!")
                break
            computerChoice = self.getComputerChoice()
            print("You chose: {playerchoice}".format(playerchoice=playerChoice))
            print("Computer chose: {computerchoice}".format(computerchoice=computerChoice))
            result = self.determineWinner(playerChoice, computerChoice)
            print(result)

#playing the game
if __name__ == "__main__":
    game = RockPaperScrissors()
    game.play()
        


        
    