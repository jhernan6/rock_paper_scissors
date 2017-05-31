import random

lose = "Too bad, the computer won"
win = "Congratz!! You beat the computer"
lives = 5
score = 0
drew = 0
computer_lives = 7
move_set = ["rock", "paper", "scissors"]

while True:
    print("Testing out loop and vars")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    searchfile = open("accounts.csv","r")

    for lien in searchfile:
        if username and password in line:
            print("Access Granted")
            print("==========================================================")
            print("Rules of the game:")
            print("1. You have a total of ",lives," lives")
            print("2. The computer has ",computer_lives," lives")
            print("3. If you win the round the computer loses a point")
            print("4. If the computer wins the round you lose a point")
            print("5. If the round is a draw no lives are lost")
            print("==========================================================")
            print("Commands you can use:")
            print("rules - list the rules of the game")
            print("exit - leave the game at any point")
            print("==========================================================")
            print("Can you beat the computer?")
            print("Good Luck!")
            print("**********************************************************")
                while True:
                    rps = input("What is your move")
                    c_rps = random.choice(move_set)
