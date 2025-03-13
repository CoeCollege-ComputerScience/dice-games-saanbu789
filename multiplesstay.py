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

def multiples_stay():
    player_a = 0
    player_b = 0
    while player_a < 10 and player_b < 10:
        player_a_roll = count_outcomes(roll())
        print(f"Player A rolls {player_a_roll}")
        keep = int(input("Player A, which outcome would you like to keep? "))
        player_b_roll = count_outcomes(roll())
        print(f"Player B rolls {player_b_roll}")
        keep = int(input("Player B, which outcome would you like to keep? "))
        if player_a_roll[keep] > player_b_roll[keep]:
            player_a += 1
            print("Player A wins the round!")
        else:
            player_b += 1
            print("Player B wins the round!")
    if player_a == 10:
        print("Player A wins the game!")   
    else:
        print("Player B wins the game!")