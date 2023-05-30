# description: Calculate a BMI given someone's weight and height
# author: SCHEPPAT, Hunter
# date: 10.30.22
import random


# create a userList of n unique numbers between 0-1000
def create_userList(length):
    length = int(length)
    solution = []

    # continue until userList is inputted length
    while len(solution) < length:
        num = random.randint(0, 1000)

        # add num to userList if it is unique
        if num not in solution:
            solution.append(num)

    return solution


# sort the userList by insertion sort
def sort_userList(userList):
    for i in range(1, len(userList)):
        val = userList[i]

        j = i - 1

        # switch places if val less than element at j
        while j >= 0 and val < userList[j]:
            userList[j + 1] = userList[j]
            j -= 1

        userList[j + 1] = val

    return userList


# generate and find targets
def find_target(userList, type):
    # keep track of searches and set initial target
    searches = 0
    vals = list(range(0, 1001))

    # do iterative binary search
    if type == 'I':
        # choose a random num from vals then remove it
        target = random.choice(vals)
        vals.remove(target)
        searches = 1

        # if target not found, call function with a new target
        while binary_search_iterative(target, userList) is not True:
            print("Target = " + str(target))
            target = random.choice(vals)
            vals.remove(target)
            binary_search_iterative(target, userList)
            # increment num of searches done
            searches += 1

    # do recursive binary search
    if type == 'R':
        target = random.choice(vals)
        vals.remove(target)
        searches = 1

        # if target not found, call function with a new target
        while binary_search_recursive(target, userList) is not True:
            print("Target = " + str(target))
            target = random.choice(vals)
            vals.remove(target)
            binary_search_recursive(target, userList)

            # increment num of searches done
            searches += 1

    print("\nIt took " + str(searches) + " attempts to find the number selected")


# binary search iterative
def binary_search_iterative(target, userList):
    start = 0
    end = len(userList) - 1

    # keep shortening search until there is 1 element
    while start <= end:
        middle = ((end + start) // 2)
        val = userList[middle]

        if val < target:
            start = middle + 1

        elif val > target:
            end = middle - 1

        # return 1 if found
        elif val == target:
            return True

    # if never found return False
    return False


# binary search recursive
def binary_search_recursive(target, userList):
    # if userList is length of one, check the one element
    if len(userList) == 1:
        return target == userList[0]

    # keep shortening search until there is 1 element
    if len(userList) > 1:
        middle = (len(userList)) // 2
        val = userList[middle]

        if val == target:
            return True

        # cut userList in half and call function again
        elif val > target:
            userList = userList[:middle]
            return binary_search_recursive(target, userList)

        # cut userList in half and call function again
        else:
            userList = userList[middle + 1:]
            return binary_search_recursive(target, userList)

    # if never found return -1
    else:
        return False


def main():
    # outline program details
    print("\nThis program creates a list of random integers and then sorts them \n"
          "It then picks random integers in the same interval until it gets a hit \n"
          "using the binary search algorithm\n")

    # get user userList size and create, display, and sort the userList
    size = input("Enter the desired list size: ")
    original_userList = create_userList(size)
    print("\nOriginal list: ", end="")
    print(original_userList)
    sorted_userList = sort_userList(original_userList)
    print("\nSorted list: ", end="")
    print(sorted_userList)

    # get the search algorithm type
    type = input("\nChoose the algorithm: 'I' for Iterative, 'R' for Recursive: ")
    print("")
    find_target(sorted_userList, type)


# execute main section
main()
