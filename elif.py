
# Determine the grade you will get

percentage = int(input("What was the percentage of your grade?  "))
# each percentage with coresponding letter grade
if percentage < 60:
    grade = "F"
elif percentage < 69:
    grade = "D"
elif percentage < 79:
    grade = "C"
elif percentage < 89:
    grade = "B"
else:
    percentage > 90
    grade = "A"
# final grade
print("The letter grade is: ", str(grade))
