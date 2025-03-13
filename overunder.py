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
    player_one_score = 0
    player_two_score = 0
    playeroneturn=True

    while player_one_score < 6 and player_two_score < 6:
        if playeroneturn:
            player_one_roll = score(roll())
            print(f"{p1} rolls {player_one_roll}")
            bet = input(f"{p2}, will the next roll be over or under? (o/u) ")
            player_two_roll = score(roll())
            print(f"{p2} rolls {player_two_roll}")
        else:
            player_two_roll = score(roll())
            print(f"{p2} rolls {player_two_roll}")
            bet = input(f"{p1}, will the next roll be over or under? (o/u) ")
            player_one_roll = score(roll())
            print(f"{p1} rolls {player_one_roll}")
        
        if (bet == "o" and player_two_roll > player_one_roll) or (bet == "u" and player_two_roll < player_one_roll):
            if playeroneturn: 
                player_two_score += 1
                print(f"{p2} wins the round!")
            else:
                player_one_score += 1
                print(f"{p1} wins the round!")
        else:
            if playeroneturn:
                player_one_score += 1
                print(f"{p1} wins the round!")
            else:
                player_two_score += 1
                print(f"{p2} wins the round!")
        print(f"Score: {p1}: {player_one_score}, {p2}: {player_two_score}")
        playeroneturn = not playeroneturn

    if player_one_score == 6:
        print(f"{p1} wins the game!")
    else:
        print(f"{p2} wins the game!")

# over_under()
# prob gonna change some stuff to make player one/player two stuff more clear
# and prob also running tally of the score
# but that's a problem for later me
# i think it works tho
# maybe there's a way to add names to make it less confusing

# over_under("Shawn", "Gus")
# hmm so the problem is that the person that's doing the first roll is always player one but it needs to switch
# ig let's ask copliot
# actually not yet

# so per round there are two rolls
# roll one starts with player 1 but switched to player 2 and back again each round
# roll two is not always player 2 mx copliot it's whoever didnt do the first roll
# thanks copliot for the help with turns, let's review/fix indents/see if it works

over_under("Shawn", "Gus")
# it works yippee
# thanks copilot, literally could not have done it without you