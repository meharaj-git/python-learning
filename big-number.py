numbers = [10, 45, 23, 99, 15, 109]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest =", largest)

numbers_1 = [100, 405, 223, 99, 150, 109]
largest = max(numbers_1)
print("Largest =", largest)
smallest = min(numbers_1)
print("Smallest =", smallest)

