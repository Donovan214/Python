"""Counting the number of steps you take each day"""
# the days of the week
day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
# the number steps you take each day
for day in day_of_week:
    step = int(input(f"How many steps did you take on {day}: "))
    steps.append(step)
    print(f"You took {step} steps on {day} ")
# the total of steps you take in a week
total = sum(steps)
print("Total steps: ", total)
# the average steps you take in a week
average = round(total / len(steps))
print("Average steps: ", average)
