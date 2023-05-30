# description: Calculate a BMI given someone's weight and height
# author: SCHEPPAT, Hunter
# date: 10.24.22


# sort a list by selection sort
import random


def sortem(list):
    for i in range(0, len(list)):
        min = list[i]
        for j in range(i + 1, len(list)):
            if list[j] < list[i]:
                min = list[j]
                list[j] = list[i]
                list[i] = min

        list[i] = min
    return list


# calculate the mean
def mean(list):
    total = 0
    for i in range(0, len(list)):
        total += list[i]

    mean = (total / len(list))

    return round(mean, 2)


# calculate the median
def median(list):
    list = sortem(list)
    length = len(list)

    if length % 2 == 0:
        median = list[length // 2]
    else:
        median = (list[(length // 2)] + list[(length // 2) + 1]) / 2

    return round(median, 2)


# calculate the mode, works for one or two modes
def mode(list):
    list = sortem(list)
    uniqueVals = []

    for element in list:
        if element not in uniqueVals:
            uniqueVals.append(element)

    occur = [0] * len(uniqueVals)

    for i in range(0, len(uniqueVals)):
        element = uniqueVals[i]
        for j in range(0, len(list)):
            if element == list[j]:
                occur[i] += 1

    maximum = occur[0]
    index = 0
    index2 = 0
    for i in range(1, len(occur)):
        if occur[i] > maximum:
            maximum = occur[i]
            index = i
        elif occur[i] == maximum:
            index2 = i

    if occur[index] == occur[index2]:

        if uniqueVals[index] != uniqueVals[index2]:
            modes = [uniqueVals[index], uniqueVals[index2]]
        else:
            modes = [uniqueVals[index]]
    else:
        modes = [uniqueVals[index]]
    return modes


# calculate the standard deviation
def std_dev(list):
    sum = 0
    the_mean = mean(list)
    for element in list:
        sum += (element - the_mean)**2

    deviation = (sum/(len(list) - 1))**0.5

    return round(deviation, 2)


# main section
def main():
    print("This program produces the following descriptive statistics for a sample of widget scores: The mean, "
          "median, mode, and, standard deviation \n")
    number = random.randint(20,30)
    print("Input " + str(number) + " widget scores")
    input_string = input("Input widget scores separated by commas: ")
    initial_list = input_string.split(",")

    for i in range(0, len(initial_list)):

        initial_list[i] = int(initial_list[i])

    print("The mean for " + str(number) + " values is " + str(mean(initial_list)))
    print("The median for " + str(number) + " values is " + str(median(initial_list)))

    modes = mode(initial_list)
    if len(modes) < 2:
        print("the mode(s) for " + str(number) + " values is " + str(modes[0]))
    else:
        print("the mode(s) for " + str(number) + " values is " + str(modes[0]) + " " + str(modes[1]))

    print("the standard deviation for " + str(number) + " values is " + str(std_dev(initial_list)))


main()

