# multiples stay
# two players, ten dice
# player a begins by rolling all dice
# count number of times each outcome is rolled
# player a chooses one outcome to keep, those dice are removed
# player b rolls remaining dice
# count number of times each outcome is rolled
# player b chooses one outcome to keep, those dice are removed
# repeat until no dice left, you lose when you can't remove any dice

import random

def roll():
    return [random.randint(1,6) for i in range(10)]

def count_outcomes(dice):
    return {i: dice.count(i) for i in dice}
    # print(count_outcomes)

def multiples_stay(p1,p2):
    player_a = 0
    player_b = 0
    while player_a < 10 and player_b < 10:
        player_a_roll = count_outcomes(roll())
        print(f"{p1} rolls {player_a_roll}")
        keep = int(input(f"{p1}, which outcome would you like to keep? "))
        player_b_roll = count_outcomes(roll())
        print(f"{p2} rolls {player_b_roll}")
        keep = int(input(f"{p2}, which outcome would you like to keep? "))
        if player_a_roll[keep] > player_b_roll[keep]:
            player_a += 1
            print(f"{p1} wins the round!")
        else:
            player_b += 1
            print(f"{p2} wins the round!")
    if player_a == 10:
        print(f"{p2} wins the game!")   
    else:
        print(f"{p2} wins the game!")

# time to see if this'll work

multiples_stay("Shawn", "Gus")
# nyokay so almost there
# the kept dice need to be removed from the pool
# see i can understand how this would be enjoyable from a brain teaser aspect but i wish it was like a person instead of ai
# i will take the suggestion of making the dice pool a list thank u copliot
# still i wish i could like do this with my dad 