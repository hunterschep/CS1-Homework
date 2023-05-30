# description: Program which forecasts two companies sales
# author: SCHEPPAT, HUNTER
# date: September.30.2022

# forecast function which takes initial sales, growth, and time period
def forecast(start, end, UW_sales, WI_sales, UW_inc, WI_inc):
    print("Year", "\t", "UW", "\t", "    WI")

    # initialize variables
    var1 = None
    var2 = None
    year = None
    j = 0

    # calculate each companies sales forecast
    for i in range(start, end + 1):
        UW_Current = round(UW_sales * (UW_inc ** (i - start)), 1)
        WI_Current = round((WI_sales * (WI_inc ** (i - start))), 1)

        # find which company is initially bigger
        if WI_sales > UW_sales:
            var1 = UW_Current
            var2 = WI_Current
        else:
            var1 = WI_Current
            var2 = UW_Current

        # if they switch, save that year in year variable
        if var1 >= var2:
            j += 1
            year = i - j + 1

        print(str(i), "\t", str(UW_Current), "\t", str(WI_Current))

    # print out the year they crossed
    if year is not None:
        print("The sales crossed in " + str(year))


# get the initial input and make sure it is an int
while True:
    UW_Sales = input("Please enter initial sales for UW: ")
    try:
        UW_Sales = int(UW_Sales)
    except ValueError:
        print("Please enter initial sales as an integer!")
        continue
    break


# get the initial input and make sure it is an int
while True:
    WI_Sales = input("Please enter initial sales for WI: ")
    try:
        WI_Sales = int(WI_Sales)
    except ValueError:
        print("Please enter initial sales as an integer!")
        continue
    break


# get the initial increase and make sure it is a float
while True:
    UW_Increase = input("Please enter annual % increase for UW: ")
    try:
        UW_Increase = float(UW_Increase)
        UW_Increase = (UW_Increase / 100) + 1
    except ValueError:
        print("Please enter percent increase!")
        continue
    break


# get the initial increase and make sure it is a float
while True:
    WI_Increase = input("Please enter annual % increase for WI: ")
    try:
        WI_Increase = float(WI_Increase)
        WI_Increase = (WI_Increase / 100) + 1
    except ValueError:
        print("Please enter percent increase!")
        continue
    break


# get the start and end years
year_Start = int(input("Please enter the year to start the forecast: "))
year_End = int(input("Please enter the year to end the forecast: "))

# call the forecast function
forecast(year_Start, year_End, UW_Sales, WI_Sales, UW_Increase, WI_Increase)
