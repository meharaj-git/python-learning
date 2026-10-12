def generate_fibonacci(n):
    # Starting values for the Fibonacci sequence
    sequence = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return sequence
    
    # Loop to calculate the rest of the sequence up to n terms
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        
    return sequence

# Main program execution
try:
    # Ask the user for input and convert it to an integer
    user_input = int(input("Enter the number of Fibonacci terms you want: "))
    
    if user_input <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        result = generate_fibonacci(user_input)
        print(f"The first {user_input} terms of the Fibonacci series are:")
        print(result)

except ValueError:
    print("Invalid input! Please enter a valid whole number.")
