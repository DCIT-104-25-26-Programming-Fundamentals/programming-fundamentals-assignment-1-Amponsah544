# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_menu():
    # Displays the main menu options.
    print(f"""================================
                STUDENT RECORD SYSTEM MENU")
              ==================================
    1. Add student
    2. Display all students
    3. Calculate average score
    4. Quit
    """)


def add_student(students):
    # Prompts the user for student details and adds a new dictionary record to the students list.
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    try:
        num_scores = int(input("How many scores? "))
    except ValueError:
        print("Invalid number of scores. Aborting entry.\n")
        return

    scores = []
    for i in range(1, num_scores + 1):
        try:
            score = float(input(f"Enter score {i}: "))
            # Format integer inputs neatly
            scores.append(int(score) if score.is_integer() else score)
        except ValueError:
            print("Invalid input, defaulting score to 0.")
            scores.append(0)

    # Create dictionary and append to main list
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.\n')


def display_all_students(students):
    # Prints a formatted table of all students and their averages.
    if not students:
        print("No students have been added yet.\n")
        return

    divider = "-" * 50
    print(divider)
    print(f"{'Name':<15} {'ID':<11} {'Scores':<14} {'Average':<8}")
    print(divider)

    for s in students:
        scores_str = ", ".join(str(x) for x in s["scores"])
        avg = sum(s["scores"]) / len(s["scores"]) if s["scores"] else 0.0
        print(f"{s['name']:<15} {s['id']:<11} {scores_str:<14} {avg:.2f}")

    print(divider + "\n")


def calculate_student_average(students):
    # Searches for a student by ID, calculates their average, and prints it.
    search_id = input("Enter student ID: ").strip()

    for s in students:
        if s["id"] == search_id:
            if s["scores"]:
                avg = sum(s["scores"]) / len(s["scores"])
                print(f"{s['name']}'s average score: {avg:.2f}\n")
            else:
                print(f"{s['name']} has no recorded scores.\n")
            return

    print("Error: Student ID not found.\n")


def main():
    # Store all student records in a list of dictionaries
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            calculate_student_average(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.\n")


# Main execution block
if __name__ == "__main__":
    main()
