# Task 2: Class Marks Analyzer
# Topics: Lists (append, len, sum, max, min, sorted) and Loops


def get_valid_mark(student_name):
    # Ask for one student's mark until a number between 0 and 100 is entered.
    while True:
        text = input(f"Enter marks for {student_name} (0-100): ").strip()
        try:
            mark = float(text)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if mark < 0 or mark > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            continue
        return mark


def find_students_with_mark(names, marks, target_mark):
    # Return the names of all students whose mark equals target_mark.
    matched = []
    for index in range(len(marks)):
        if marks[index] == target_mark:
            matched.append(names[index])
    return matched


print("===== CLASS MARKS ANALYZER =====")

# Ask how many students are in the class (must be a whole number above zero)
while True:
    try:
        student_count = int(input("Enter number of students: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue
    if student_count <= 0:
        print("Number of students must be greater than zero.")
        continue
    break

student_names = []
student_marks = []

# Collect names and marks using append()
for number in range(1, student_count + 1):
    print(f"\n--- Student {number} ---")
    while True:
        name = input("Enter student name: ").strip().title()
        if name != "":
            break
        print("Invalid name! Name cannot be empty.")
    mark = get_valid_mark(name)
    student_names.append(name)
    student_marks.append(mark)

# Basic statistics
class_average = sum(student_marks) / len(student_marks)
highest_mark = max(student_marks)
lowest_mark = min(student_marks)
top_students = find_students_with_mark(student_names, student_marks, highest_mark)
bottom_students = find_students_with_mark(student_names, student_marks, lowest_mark)

# Count passing (50 or above) and failing (below 50) students
pass_count = 0
fail_count = 0
for mark in student_marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\n===== CLASS REPORT =====")
print(f"Total Students : {len(student_names)}")
print(f"Class Average  : {class_average:.2f}")
print(f"Highest Marks  : {highest_mark:g} ({', '.join(top_students)})")
print(f"Lowest Marks   : {lowest_mark:g} ({', '.join(bottom_students)})")
print(f"Passing        : {pass_count}")
print(f"Failing        : {fail_count}")

# Students scoring above the class average
print("\n--- Students Above Class Average ---")
above_average_found = False
for index in range(len(student_names)):
    if student_marks[index] > class_average:
        print(f"{student_names[index]} - {student_marks[index]:g}")
        above_average_found = True
if not above_average_found:
    print("No student scored above the class average.")

# Marks sorted from highest to lowest (pairs of mark and name)
print("\n--- Marks (Highest to Lowest) ---")
ranked = sorted(zip(student_marks, student_names), reverse=True)
position = 1
for mark, name in ranked:
    print(f"{position}. {name} - {mark:g}")
    position += 1
