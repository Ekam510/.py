def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample function call
sample_number = 5
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")


import math

# User input
number = float(input("Enter a number: "))

# Calculations
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Display results
print(f"Square root of {number} is: {square_root}")
print(f"Natural logarithm of {number} is: {natural_log}")
print(f"Sine of {number} (in radians) is: {sine_value}")
