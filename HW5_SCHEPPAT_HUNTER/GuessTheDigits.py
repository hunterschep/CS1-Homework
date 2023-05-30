# @author: hunter scheppat
# @date: 10/6/2022
# @program: guess a users digits

import random


def getRandom():
    n = 0
    while len(set(list(str(n)))) != 4:
        n = random.randint(1000, 9999)
    return n


def checkNum(userNum):
    temp = str(userNum)

    numString = str(random)

    for i in range(0, 4):
        tempChar = temp[i]
        if numString.find(tempChar) > -1:
            print(tempChar + " is in the number")


random = getRandom()
userInput = int(input("Enter a 4 digit integer: "))

while str(userInput) != str(random):
    checkNum(userInput)
    userInput = int(input("Enter a 4 digit integer: "))

print("You guessed the number in order! ")

