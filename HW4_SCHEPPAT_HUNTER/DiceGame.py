# description: Program which simulates a game of craps
# author: SCHEPPAT, HUNTER
# date: September.30.2022

import random


# function to roll the dice and return their value
def rollDice():
    # roll dice one and two
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    # print their first roll
    first_round = roll_one + roll_two
    print("Player rolled " + str(roll_one) + " + " + str(roll_two) + " = " + str(first_round))

    # return the roll
    return first_round


# function which takes game status and runs game until won or lost
def thePoint(game_Status, original_roll):

    while game_Status == 'CONTINUE':
        # set the point and roll the dice
        point = original_roll
        new_roll = rollDice()
        if new_roll == point:
            # declare winner if point is hit
            game_Status = "WON"
            break
        elif new_roll == 7:
            # declare loser if 7 is hit
            game_Status = "LOST"
            break

    # if there is already game status print won or lost
    if game_Status == "WON":
        print("Player wins")
        return
    else:
        print("Player loses")
        return


# explain program & roll the dice
print("This program simulates the game of dice called craps")
roll = int(rollDice())

# set game status based on roll
if roll in [7, 11]:
    gameStatus = "WON"
elif roll in [2, 3, 12]:
    gameStatus = "LOST"
else:
    gameStatus = "CONTINUE"
    print("Point is " + str(roll))

# call thePoint() function
thePoint(gameStatus, roll)
