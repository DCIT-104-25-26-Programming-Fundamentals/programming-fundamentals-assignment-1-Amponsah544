# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Function for checking prime numbers.
def is_prime(num):
    # Returns true if prime, otherwise false.
    if num < 2:
        return False
    # Checking for factors of 2 up to num -1 or square of a number for efficiency.
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


# Main execution block
if __name__ == "__main__":
    # Get user input

    User_input = int(input("Enter a number: "))

# Checks if a given number is prime.
if is_prime(User_input):
    print(f"{User_input} is a prime number.")
else:
    print(f"{User_input} is not a prime number.")
