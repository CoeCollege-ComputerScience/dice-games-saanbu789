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

def keep_the_lowest(p1,p2):
    player_one_score = 0
    player_two_score = 0
    while player_one_score < 20 and player_two_score < 20:
        player_one_roll = keep_lowest(roll())
        print(f"{p1} keeps {player_one_roll}")
        player_one_roll = score(roll())
        print(f"{p1} rolls {player_one_roll}")
        player_two_roll = keep_lowest(roll())
        print(f"{p2} keeps {player_two_roll}")
        player_two_roll = score(roll())
        print(f"{p2} rolls {player_two_roll}")
        if player_one_roll < player_two_roll:
            player_two_score += 1
            print(f"{p2} wins the round!")
        else:
            player_one_score += 1
            print(f"{p1} wins the round!")
    if player_one_score == 20:
        print(f"{p1} wins the game!")
    else:
        print(f"{p2} wins the game!")

#nyeh gonna try smth else that's easier
# same problems/ideas of adding names and keeping like running tally of the score

keep_the_lowest("Shawn", "Gus")
# let's see if this works
# ok so got it to do the thing automatically so basically the computer's playing against itself
# gonna see if i can do the name thing for the others then work on making it like playable by a person 
# if nothing else this class is increasing my respect for my dad who does this for work
# is this what it's like trying to get a toddler/young child to understand things
# maybe that's why dad's so good at explaining things like board game rules

# on second thought i think this one is probably fine bc it's just chance and the computer will probably always do the same thing as a person
# like there's no strategy it's just luck
# so i'm gonna leave it