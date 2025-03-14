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

def roll(numdice):
    return [random.randint(1,6) for i in range(numdice)]

def count_outcomes(dice):
    return {i: dice.count(i) for i in dice}
    # print(count_outcomes)

def multiples_stay(p1,p2):
    dicepool=roll(10)
    playeraturn=True

    while len(dicepool) > 0:
        if playeraturn:
         player_a_roll = count_outcomes(dicepool)
         print(f"{p1} rolls {player_a_roll}")
         keep = int(input(f"{p1}, which outcome would you like to keep? "))
         dicepool=[die for die in dicepool if die != keep]
        #  if len(dicepool) == 0: 
        #     print(f"{p1} wins the game!") 
         if all(count==1 for count in count_outcomes(dicepool).values()):
            print(f"{p1} has no multiples left, {p2} wins the game!")
            
        # this indentation not working is driving me insane WHAT DO YOU MEAN UNEXPECTED MY GUY
        # might need to ask dad over break if i dont talk to hughes today
        # nvm fixed it (finally) (only to not need that bit lol)
         else:      
            playeraturn = not playeraturn
        else:
            player_b_roll = count_outcomes(dicepool)
            print(f"{p2} rolls {player_b_roll}")
            keep = int(input(f"{p2}, which outcome would you like to keep? "))
            dicepool=[die for die in dicepool if die != keep]
        # if len(dicepool) == 0:
        #     print(f"{p2} wins the game!")
            if all(count==1 for count in count_outcomes(dicepool).values()):
             print(f"{p2} has no multiples left, {p1} wins the game!")

             

    #     if player_a_roll.get(keep,0) > player_b_roll(keep,0):
    #         player_a_score += 1
    #         print(f"{p1} wins the round!")
    #     else:
    #         player_b_score += 1
    #         print(f"{p2} wins the round!")

    # if player_a_score == 10:
    #     print(f"{p2} wins the game!")   
    # else:
    #     print(f"{p2} wins the game!")

# time to see if this'll work

multiples_stay("Shawn", "Gus")
# nyokay so almost there
# the kept dice need to be removed from the pool
# see i can understand how this would be enjoyable from a brain teaser aspect but i wish it was like a person instead of ai
# i will take the suggestion of making the dice pool a list thank u copliot
# still i wish i could like do this with my dad 

# def not gonna get done today (thursday) but i'll have like all class friday to work on it

# prob gonna have to do same thing with the turns and for end if it's a players turn when no more mulitples they lose
# but that's gonna be a problem for me tomorrow bc there's three minutes left in class

# thanks copilot for telling me how to do this
# let's see if it'll work 
# nyokay this needs more work
# i think other than the dam indentation it's mostly good
# ok got the indentation let's see if it'll be nice and work
# alright so removing the dice works now to get it so that game ends if there are no multiples
# ok changes made time to test
# gotta figure out the rolls bc each turn it's not rerolling the remaining dice
# and that'll be a problem for me over break, might need to email in order to get 4 for assignment
# and over break i'll be able to bug dad about it