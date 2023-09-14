def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: factorial of a number is n multiplied by factorial of n-1
    return n * factorial(n - 1)

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result) 