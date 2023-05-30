# @description: Simulate a game of bingo
# @author: SCHEPPAT, Hunter
# @date: 11.14.22
import random


def createCard(cols_num, rows_num):

    # initialize a card and a used number list
    card = [[0 for i in range(cols_num)] for j in range(rows_num)]
    used = []

    # add the initial nums to the Bingo card
    for row in range(0, rows_num):
        for col in range(0, cols_num):
            index1 = (col * 15) + 1
            index2 = ((col + 1) * 15)

            # make sure nums are unique
            bingo_num = random.randint(index1, index2)
            while bingo_num in used:
                bingo_num = random.randint(index1, index2)
            used.append(bingo_num)

            card[row][col] = bingo_num

    # make the middle space free !
    card[(rows_num // 2)][(cols_num // 2)] = 0

    print("SELECTION LIST: " + str(used))
    print("BINGO CARD: " + str(card))
    printHelper(card)

    return card


# simulate the full Bingo game
def bingoGame(card):
    calls = list(range(1, 76))
    calls_made = []

    # continue to run numbers until Bingo is hit
    while not isItBingo(card):
        call = random.choice(calls)
        calls.remove(call)
        calls_made.append(call)

        # look for Bingo hit
        for row in range(0, len(card)):
            for col in range(0, len(card[0])):

                # if there is a Bingo hit, set to 0
                if card[row][col] == call:
                    card[row][col] = 0
                    isItBingo(card)

    # if loop breaks, Bingo has been made
    print("\nCALL LIST: " + str(calls_made))
    print("BINGO!, final number was " + str(calls_made[len(calls_made) - 1]))
    printHelper(card)


def isItBingo(card):

    # check if rows equal 0
    for row in range(0, len(card)):
        bingo_sum = 0
        for col in range(0, len(card[0])):
            bingo_sum += card[row][col]

        if bingo_sum == 0:
            return True

    # check if cols equal 0
    for row in range(0, len(card)):
        bingo_sum = 0
        for col in range(0, len(card[0])):
            bingo_sum += card[col][row]

        if bingo_sum == 0:
            return True

    # check if first diag equal 0
    bingo_sum = 0
    for row in range(0, len(card)):
        bingo_sum += card[row][row]

    if bingo_sum == 0:
        return True

    # check if second diag equal 0
    bingo_sum = 0
    for row in range(0, len(card)):
        bingo_sum += card[row][abs(row - ((len(card[row])) - 1))]

    if bingo_sum == 0:
        return True

    return False


def printHelper(card):
    print()
    bingo = ['B', 'I', 'N', 'G', 'O']
    for i in range(0, len(bingo)):
        print("\t " + bingo[i], end=" ")
    for row in range(len(card)):
        print("")
        for col in range(len(card[0])):
            print("\t", card[row][col], end= "")

    print("")


def main():
    print("\nThis program simulates the creation of a BINGO card and the subsequent simulation \n"
          "of a one card, one player game of BINGO\n")
    card = createCard(5, 5)
    bingoGame(card)


main()

