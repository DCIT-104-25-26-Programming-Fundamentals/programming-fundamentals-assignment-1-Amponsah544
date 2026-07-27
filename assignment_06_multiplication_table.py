# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_single_table(digit):
    print(f"Multiplication Table for {digit}:")
    for i in range(1, 13):
        print(f"{digit}  x  {i:<2} =  {digit * i}")


def generate_range_tables(number):

    for num in range(1, number + 1):
        generate_single_table(num)
        if num < number:
            print("-" * 27)


def main():
    print(f"=== PART A: Single Multiplication Table ===")
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Error: Input must be a positive integer.\n")
            return
        generate_single_table(num)

    except ValueError:
        print(f"Error: Invalid input. Please enter a valid integer. ")
        return

    print(f"  + = * 40 +  ")

    print("=== PART B: Tables from 1 to N ===")
    try:
        n = int(input("Enter a number N: "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        generate_range_tables(n)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
