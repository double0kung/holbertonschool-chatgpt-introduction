#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Add this line to decrement n
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    f = factorial(n)
    print(f)
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
