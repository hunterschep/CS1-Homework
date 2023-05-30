# description: Calculate a BMI given someone's weight and height
# author: SCHEPPAT, Hunter
# date: 9.15.22

def main():
    # print program description
    print("This program computes and evaluates Body Mass Index (BMI)")
    print("")
    print("Enter Height in Feet and Inches")

    # get height and weight from user
    height = float(input("Enter feet: ")) * 12
    height += float(input("Enter inches: "))
    weight = float(input("Enter weight in pounds: "))

    print("Height is " + str(height) + " inches")

    # call the compute BMI & category functions
    BMI = compute_BMI(weight, height)
    category = compute_Category(BMI)

    print("Your Body Mass Index is " + str(BMI))
    print(category)


# compute and round BMI
def compute_BMI(init_Weight, init_Height):
    init_Height = (init_Height / 39.37)
    init_Height = init_Height ** 2
    init_Weight = init_Weight / 2.205

    init_BMI = round((init_Weight / init_Height), 1)

    return init_BMI


# compute BMI category based on BMI number
def compute_Category(init_BMI):
    if init_BMI > 25.0:
        init_category = 'Overweight'
    elif init_BMI >= 18.5:
        init_category = 'Normal Weight'
    else:
        init_category = 'Underweight'

    return init_category


main()
