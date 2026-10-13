numbers = [1,2,3,4,5,6,7,8,11,3,10,2,99]
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
print("Count of even numbers:", count)
count = 0
for n in numbers:
    if n % 2 != 0:
        count += 1
print("Count of odd numbers:", count)

