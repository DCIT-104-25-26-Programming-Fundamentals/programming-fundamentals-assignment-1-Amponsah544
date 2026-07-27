# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end="\t")
        print()


def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row_str = input(f"Enter row {i + 1}: ")
            parts = row_str.split()

            if len(parts) != cols:
                print(f"Expected exactly {cols} numbers, but got {len(parts)}. Try again.")
                continue

            row = []
            for p in parts:
                row.append(int(p))
            matrix.append(row)
            break
    return matrix


def part_a_transpose():
    print("--- PART A: Transpose a Matrix ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    matrix = read_matrix(m, n)

    transposed = []
    for col_idx in range(n):
        new_row = []
        for row_idx in range(m):
            new_row.append(matrix[row_idx][col_idx])
        transposed.append(new_row)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transposed)


def part_b_add():
    print("\n--- PART B: Add Two Matrices ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    print("Enter Matrix A:")
    matrix_a = read_matrix(m, n)

    print("Enter Matrix B:")
    matrix_b = read_matrix(m, n)

    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    print("\nMatrix A + Matrix B:")
    print_matrix(result)


def part_c_multiply():
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter number of rows for Matrix A: "))
    n = int(input("Enter number of columns for Matrix A / rows for Matrix B: "))
    p = int(input("Enter number of columns for Matrix B: "))

    print("Enter Matrix A:")
    matrix_a = read_matrix(m, n)

    print("Enter Matrix B:")
    matrix_b = read_matrix(n, p)

    result = []
    for i in range(m):
        row = []
        for j in range(p):
            sum_val = 0
            for k in range(n):
                sum_val += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_val)
        result.append(row)

    print("\nMatrix A x Matrix B:")
    print_matrix(result)


if __name__ == "__main__":
    part_a_transpose()
    part_b_add()
    part_c_multiply()