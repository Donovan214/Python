# while loops

count = 0
while count < 5:
    print("Loop iteration", count)
    count += 1  # Increment count
    print("Count is now", count)

# for loops with range

for i in range(1, 10, 2):
    print(i)

for i in range(5, 8):
    print(i)

for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1, 10 + 1):
    if i % 2 == 0:
        continue
    print(i)

# loops with break or continue

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        break
    print(number)

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        continue
    print(number)

# loops with else clause

# for item in iterable:
    # Code to execute for each item
   # if some_condition:
    #    break
# else:
    # Code to execute if the loop did not encounter a 'break'

for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without break")
