# Ask how many numbers to enter
count_numbers = int(input("How many numbers do you want to enter? "))

numbers = []

# Get numbers from user
for i in range(count_numbers):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Count even and odd numbers
even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nNumbers entered:", numbers)
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)