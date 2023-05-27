# This is a python program that sums up all even numbers in a given list of numbers.
# The code demonstrates the use of functions, conditional statements, loops, and comparison operators.

def sum_even(numbers):
    # Initialize a variable to store the sum of even numbers
    sum_all = 0
    
    # Iterate through each element in the list
    for num in numbers:
        # Check if the current number is even
        if num % 2 == 0:
            # If the number is even, add it to the sum
            sum_all += num
    
    # Return the sum of even numbers
    return sum_all

# Prompt the user to enter a list of numbers
input_numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = [int(num) for num in input_numbers.split()]

# Calculate the sum of even numbers
sum_all = sum_even(numbers)

# Print the sum of even numbers
print('Sum of even numbers:', sum_all)
