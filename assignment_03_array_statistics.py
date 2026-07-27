# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def cal_Sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    total = cal_Sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num


def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
    return min_num


def main():
    digit = int(input("How many numbers? "))

    if digit <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    numbers = []
    for i in range(digit):
        S_num = float(input(f"Enter number {i + 1}: "))
        numbers.append(S_num)

    sum = cal_Sum(numbers)
    avg = calculate_average(numbers)
    max = find_maximum(numbers)
    min = find_minimum(numbers)

    print()

    print(f"===== Results =======")
    print(f"Sum:     {sum}")
    print(f"Average: {avg}")
    print(f"Maximum: {max}")
    print(f"Minimum: {min}")


if __name__ == "__main__":
    main()
