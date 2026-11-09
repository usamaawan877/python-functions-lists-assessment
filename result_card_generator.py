# Task 1: Student Result Card Generator
# Topics: Functions (def, parameters, return) and String Manipulation

SUBJECT_COUNT = 5
MAX_MARKS_PER_SUBJECT = 100
MIN_PASS_MARKS_PER_SUBJECT = 40


def get_valid_marks(subject):
    # Ask for marks of one subject until a number between 0 and 100 is entered.
    while True:
        text = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            marks = float(text)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if marks < 0 or marks > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            continue
        return marks


def calculate_percentage(total, max_total):
    # Return the percentage obtained from total marks and maximum marks.
    return (total / max_total) * 100


def get_grade(percentage):
    # Return the letter grade for a given percentage.
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def format_name(name):
    # Clean extra spaces and capitalize each word of the name.
    return name.strip().title()


def get_valid_name():
    # Ask for the student name until a non-empty name is entered.
    while True:
        name = format_name(input("Enter student name: "))
        if name != "":
            return name
        print("Invalid name! Name cannot be empty.")


def get_valid_roll_number():
    # Ask for the roll number until it contains digits only.
    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            return roll_number
        print("Invalid roll number! Use digits only.")


print("===== STUDENT RESULT CARD GENERATOR =====")

student_name = get_valid_name()
roll_number = get_valid_roll_number()

subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
marks_list = []
for subject in subjects:
    marks_list.append(get_valid_marks(subject))

total_obtained = sum(marks_list)
max_total = SUBJECT_COUNT * MAX_MARKS_PER_SUBJECT
percentage = calculate_percentage(total_obtained, max_total)
grade = get_grade(percentage)

# Any subject below 40 means the final result is Fail, whatever the percentage
failed_subject = min(marks_list) < MIN_PASS_MARKS_PER_SUBJECT
if failed_subject:
    grade = "Fail"

status = "Fail" if grade == "Fail" else "Pass"

print("\n==============================================")
print("               RESULT CARD")
print("==============================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("----------------------------------------------")
for index in range(SUBJECT_COUNT):
    print(f"{subjects[index]:<12} : {marks_list[index]:g} / 100")
print("----------------------------------------------")
print(f"Total Marks  : {total_obtained:g} / {max_total}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print(f"Final Status : {status}")
if failed_subject:
    print("Note         : Marks below 40 in at least one subject.")
print("==============================================")
