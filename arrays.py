

times_of_day = ["Breakfast", "Lunch", "Dinner", "Bedtime"]

blood_sugar_levels = []
for time in times_of_day:
    level = input(f"Enter your blood sugar level for {time}: ")
    blood_sugar_levels.append([time, level])

for time in test_times:
    level = int(input(f"Enter your blood sugar level for {time}: "))
    sugars.append([time, level])


total = 0
for sugar in sugars:
    total += sugar[1]

average = round(total / len(sugars))
print("Your average blood sugar level is ", average)


