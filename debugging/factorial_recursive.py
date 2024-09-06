#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. For example:
    5! = 5 * 4 * 3 * 2 * 1 = 120

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number.

    Raises:
    RecursionError: If the input is too large, causing excessive recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)

try:
    # Convert the command-line argument to an integer
    number = int(sys.argv[1])
    
    # Calculate the factorial
    result = factorial(number)
    
    # Print the result
    print(result)
except ValueError:
    print("Error: Please provide a valid integer as an argument.")
except RecursionError:
    print("Error: Input is too large, causing excessive recursion.")
    
