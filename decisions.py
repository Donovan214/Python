# Determine if the age is apportiate for the actions

age = int(input("What is your current age?  "))
# Check to see if the user is old enough to drive.
if age < 16:
    print("You are not old enough to drive")
else:
    print("You can drive")
    # Check to see if the user can vote.
if age < 18:
    print("You can not vote")
else:
    print("You can vote")
    # Check to see if the user can legally buy alcohol.
if age < 21:
    print("You can not buy alcohol")
else:
    print("You can buy alcohol")
    # Check to see if the user is eligible for a senior discount(65)
if age < 65:
    print("You do not qualify for the discount")
else:
    print("You qualify for the discount")
