"""Daily Heart rate Tracker"""

# The time of day you take your heart rate
times_of_day = ("Morning", "Midday", "Afternoon", "Evening")
heart_rate = []
# your input of your heart rate
for time in times_of_day:
    level = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
    heart_rate.append([time, level])
# Total of your heart rates
total = 0
for heart in heart_rate:
    total += heart[1]
# the average of your heart rate
average = round(total / len(heart_rate))
print("Average heart rate today: ", average)
