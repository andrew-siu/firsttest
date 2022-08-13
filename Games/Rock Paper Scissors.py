from random import randint

listChoice = ["Rock", "Paper", "Scissors"]

while 1:

    me = int(input(f"Choose one: 1: Rock, 2: Paper, 3: Scissors, 0: Quit\n"))

    if (me == 0):
        print(f"Goodbye!")
        break

    opponent = randint(1,3)

    outcome = opponent - me

    print(f"You: {listChoice[me-1]}, Opponent: {listChoice[opponent-1]}")
    if (outcome == 0):
        print(f"Draw!")
    elif (outcome == 1 )*( outcome == -2):
        print(f"You win!")
    else:
        print(f"You lose!") 
