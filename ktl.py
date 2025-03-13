# keep the lowest
# start by rolling five dice
# keep the lowest number
# continue rerolling the other dice until no more left to roll
# turn scored by adding values
# alternate players, first to 20 loses

import random

def roll():
    return [random.randint(1,6) for i in range(5)]

def keep_lowest(dice):
    return min(dice)

def reroll(dice):
    return [random.randint(1,6) for i in range(len(dice)-1)]   

def score(dice):
    return sum(dice)

def keep_the_lowest():
    player_one = 0
    player_two = 0
    while player_one < 20 and player_two < 20:
        player_one_roll = keep_lowest(roll())
        print(f"Player one keeps {player_one_roll}")
        player_one_roll = score(roll())
        print(f"Player one rolls {player_one_roll}")
        player_two_roll = keep_lowest(roll())
        print(f"Player two keeps {player_two_roll}")
        player_two_roll = score(roll())
        print(f"Player two rolls {player_two_roll}")
        if player_one_roll < player_two_roll:
            player_two += 1
            print("Player two wins the round!")
        else:
            player_one += 1
            print("Player one wins the round!")
    if player_one == 20:
        print("Player one wins the game!")
    else:
        print("Player two wins the game!")

#nyeh gonna try smth else that's easier
# same problems/ideas of adding names and keeping like running tally of the score
