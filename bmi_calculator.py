"""
    
    Create a BMI calculator that takes a user's weight and height, 
    calculates their BMI, and then categorizes their BMI into underweight, 
    normal weight, overweight, or obese.

"""
# the global varibles
global POUNDS
POUNDS = 1 * .453592
global INCHES
INCHES = 1 * .0254

# def get_height(height):
#     height_total = height * .0254
#     return height_total

# def get_weight(weight):
#     weight_total = weight * .453592
#     return weight_total

# def total_bmi(bmi):
#     bmi = weight / (height * height)

# under = bmi < 18.5
# normal = 18.5 < bmi < 24.9
# over = 25 < bmi < 29.9
# obese = bmi > 30


def main():
    # user inputs their information
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    
    INCHES = height * .0254
    POUNDS = weight * .453592
    # coverts the information in BMI
    bmi = POUNDS / (INCHES * INCHES)
  
    if bmi < 18.5:
        bmi_total = "under"
    elif 18.5 < bmi < 24.9:
        bmi_total = "normal"
    elif 25 < bmi < 29.9:
        bmi_total = "over"
    elif bmi > 30:
        bmi_total = "obese"

    # shows your BMI rating
    print(f"Your BMI is: {(bmi):,.2f}")
    # shows your category
    print(f"You are in the {bmi_total} weight category.")

main()