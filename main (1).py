def factorial(n):
    """
    This function calculates the factorial of a number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
