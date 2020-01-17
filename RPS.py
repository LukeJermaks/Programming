#Rock Paper Scisors

#  M O D U L E S  #

import random

#  V A R I A B L E S  #
        #N/A#
#  FUNC AND PROC  #


def uChoice():           #Retrieves the user's choice between rock, paper or scissors, then simplifies by making it into a 1 letter value rather than a full word
    cont = True
    global userChoice

    
    while cont == True:
        userChoice = input("Enter your choice:\n> ROCK\n> PAPER\n> SCISSORS\n>>> ")
        userChoice = userChoice.upper()
        
        if userChoice == "ROCK":
            userChoice = "r"
            cont = False

        elif userChoice == "PAPER":
            userChoice = "p"
            cont = False

        elif userChoice == "SCISSORS":
            userChoice = "s"
            cont = False

        else:
            print("Sorry, I didn't quite catch that. Please try again!")           
            

    return userChoice

    

def bChoice():             #Determines what the bot choses between Rock, Paper or Scissors via random number generation

    global botChoice

    botChoice = random.randint(1,3)

    if botChoice == 1:
        botChoice = "r"

    elif botChoice == 2:
        botChoice = "p"

    elif botChoice == 3:
        botChoice = "s"
        

    return botChoice



def winner(botChoice, userChoice):
        
    if botChoice == "r":
        if userChoice == "r":
            print("You drew with the bot. Try again!")

        elif userChoice == "p":
            print("You Win!!!")
            
        elif userChoice == "s":
            print("You Lose!")
        
    elif botChoice == "p":
        if userChoice == "r":
            ("You Lose!")

        elif userChoice == "p":
            print("You drew with the bot. Try again!")
            
        elif userChoice == "s":
            print("You Win!!!")
        
    elif botChoice == "s":
        if userChoice == "r":
            print("You Win!!!")

        elif userChoice == "p":
            ("You Lose!")
            
        elif userChoice == "s":
            print("You drew with the bot. Try again!")

            
    
def loopGame():

    cont = True
    while cont == True:
        
        uChoice()
        print("Your choice is: " , userChoice)

        bChoice()
        print("the bot's choice is: " , botChoice)

        winner(botChoice, userChoice
               )

        loop = input("Press 'enter' on your keyboard to retry or type 'quit' to stop playing.\n>>> ")
        loop = loop.upper()
        
        if loop == "QUIT":
            cont = False

        else:
            cont = True

                  


#   M  A  I  N   #

loopGame()

