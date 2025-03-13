# over under
# two players, three dice
# player one rolls three dice, add them up
# player two makes bet on whether the next roll will be over or under that number
# player two rolls the dice
# if player two is correct, they win the round; ties go to player one
# roles alternate until one player reaches 6 points

import random

def roll():
    return [random.randint(1,6) for i in range(3)]

def score(dice):
    return sum(dice)

def over_under(p1,p2):
    player_one = 0
    player_two = 0
    while player_one < 6 and player_two < 6:
        player_one_roll = score(roll())
        print(f"{p1} rolls {player_one_roll}")
        bet = input(f"{p2}, will the next roll be over or under? (o/u) ")
        player_two_roll = score(roll())
        print(f"{p2} rolls {player_two_roll}")
        if (bet == "o" and player_two_roll > player_one_roll) or (bet == "u" and player_two_roll < player_one_roll):
            player_two += 1
            print(f"{p2} wins the round!")
        else:
            player_one += 1
            print(f"{p1} wins the round!")
    if player_one == 6:
        print(f"{p1} wins the game!")
    else:
        print(f"{p2} wins the game!")

# over_under()
# prob gonna change some stuff to make player one/player two stuff more clear
# and prob also running tally of the score
# but that's a problem for later me
# i think it works tho
# maybe there's a way to add names to make it less confusing

over_under("Shawn", "Gus")
# hmm so the problem is that the person that's doing the first roll is always player one but it needs to switch