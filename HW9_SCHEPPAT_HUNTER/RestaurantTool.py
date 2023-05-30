# @author: hunter scheppat
# @date: 12/1/2022
# @program: sort through a file of restaurants

# open & read the file
file = open('restaurants.txt', 'r')
read = file.readlines()

# create the 2d list
restaurant_2d = [[s.strip() for s in line.split(",")] for line in read]


# find the highest rating
def highestRating(restaurants):
    # initialize the highest rating to the first restaurant
    highRating = restaurants[0][4]
    index = 0

    # if another restaurant is higher, set the index and rating to that
    for row in range(1, len(restaurants)):
        if float(restaurants[row][4]) > float(highRating):
            highRating = restaurants[row][4]
            index = row

    # print the highest rated restaurant
    print("The restaurant with the highest rating was: " + str(restaurants[index][0]) +
          ", with a rating of: " + str(restaurants[index][4]))


# find the lowest rated restaurant in Boston
def lowestBoston(restaurants):
    boston = []

    # new 2d list of only boston restaurants
    for restaurant in restaurants:
        if restaurant[1] == 'Boston':
            boston.append(restaurant)

    # initialize the lowest rating to the first restaurant
    lowRating = boston[0][4]
    index = 0

    # if another restaurant is lower, set the index and rating to that
    for row in range(1, len(boston)):
        if float(boston[row][4]) < float(lowRating):
            lowRating = boston[row][4]
            index = row

    # print the lowest rated restaurant
    print("The restaurant with the lowest rating in Boston was: " + str(boston[index][0]) +
          ", with a rating of: " + str(boston[index][4]))


# find the highest rated average cuisine
def cuisineAverage(restaurants):
    cuisines = []

    # create a list of unique cuisines
    for restaurant in restaurants:
        if restaurant[2] not in cuisines:
            cuisines.append(restaurant[2])

    my_dict = {}

    # use cuisines as a key, and their average rating as the value
    for cuisineType in cuisines:
        occurrences = 0
        rating = 0

        # calculate and add the average rating for each cuisine type
        for restaurant in restaurants:
            if restaurant[2] == cuisineType:
                rating += float(restaurant[4])
                occurrences += 1

        rating = rating / occurrences
        my_dict[cuisineType] = rating

    # get the max and min cuisines from the dictionary
    highestRated = max(my_dict, key=my_dict.get)
    print("Highest rated cuisine was: " + highestRated + ", with a rating of: " + str(my_dict[highestRated]))
    print("")
    lowestRated = min(my_dict, key=my_dict.get)
    print("Lowest rated cuisine was: " + lowestRated + ", with a rating of: " + str(round((my_dict[lowestRated]), 2)))


# find the most expensive restaurant(s)
def mostExpensive(restaurants):
    maxDollars = 0
    hold = ""

    # search for restaurants with most $
    for restaurant in restaurants:
        if len(restaurant[3]) > maxDollars:
            maxDollars = len(restaurant[3])
            hold = restaurant[3]

    expensive = []

    # add restaurants with most $ to new list
    for restaurant in restaurants:
        if len(restaurant[3]) == maxDollars:
            expensive.append(restaurant[0])

    # print the new list of expensive restaurants
    print("The most expensive restaurants were: ")
    for j in range(0, len(expensive)):
        print(expensive[j], end=", ")
    print("\nWith a price of: " + str(hold))


# function calls
highestRating(restaurant_2d)
print("")
lowestBoston(restaurant_2d)
print("")
cuisineAverage(restaurant_2d)
print("")
mostExpensive(restaurant_2d)
