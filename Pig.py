# each player takes turns rolling die
# if player rolls 1, they lose their turn
# if player rolls 2-6, they can choose to roll again or stop
# if player chooses to hold, they add the sum of their rolls to their score
# first to 100 wins

import random

def rollDie():
    return random.randint(1,6)

def pig():
    score = 0
    while score < 100:
        player = 1
        while player <= 2:
            print(f"Player {player}'s turn")
            turnScore = 0
            roll = rollDie()
            print(f"Roll: {roll}")
            if roll == 1:
                print("You rolled a 1. Your turn is over.")
                player += 1
                continue
            turnScore += roll
            print(f"Turn score: {turnScore}")
            choice = input("Would you like to roll again? (y/n) ")
            while choice == 'y':
                roll = rollDie()
                print(f"Roll: {roll}")
                if roll == 1:
                    print("You rolled a 1. Your turn is over.")
                    turnScore = 0
                    break
                turnScore += roll
                print(f"Turn score: {turnScore}")
                choice = input("Would you like to roll again? (y/n) ")
            score += turnScore
            print(f"Player {player}'s score: {score}")
            player += 1
    if score >= 100:
        return f"Player {player} wins!"
    
pig()

