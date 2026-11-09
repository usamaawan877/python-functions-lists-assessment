# 📘 Python Functions, Strings & Lists Assessment

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-green)
![Topics](https://img.shields.io/badge/Topics-Functions%20%7C%20Strings%20%7C%20Lists-orange)

## 📌 Project Overview

This repository contains two separate console-based Python programs built for the **Functions, Strings and Lists** assessment.

| # | Program | File | Main Topics |
|---|---------|------|-------------|
| 1 | Student Result Card Generator | `result_card_generator.py` | Functions, string methods, f-strings |
| 2 | Class Marks Analyzer | `class_marks_analyzer.py` | Lists, loops, custom functions |

## 📁 Project Structure

```
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

---

## 🧾 Task 1: Student Result Card Generator

### Description
Takes a student's name, roll number and marks in five subjects, then prints a formatted result card with total, percentage, grade and Pass/Fail status.

### Functions

| Function | Purpose |
|----------|---------|
| `get_valid_marks(subject)` | Asks for marks until a number between 0 and 100 is entered |
| `calculate_percentage(total, max_total)` | Returns the percentage |
| `get_grade(percentage)` | Returns the letter grade |
| `format_name(name)` | Cleans the name with `.strip()` and `.title()` |
| `get_valid_name()` | Asks again if the name is empty |
| `get_valid_roll_number()` | Asks again until the roll number is digits only (`.isdigit()`) |

### Grading Table

| Percentage | Grade |
|------------|-------|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| Below 50 | Fail |

> ⚠️ If **any subject is below 40**, the final result is **Fail** whatever the overall percentage is.

### Concepts Used
`def`, parameters, `return`, `while True` validation, `try / except`, `.strip()`, `.title()`, `.isdigit()`, `if / elif / else`, lists, `sum()`, `min()`, f-strings with alignment (`:<12`) and decimals (`:.2f`)

### ▶️ How to Run
```bash
python result_card_generator.py
```

### 🖥️ Sample Execution

**✅ Pass (messy name is cleaned)**
```
===== STUDENT RESULT CARD GENERATOR =====
Enter student name:   ali raza khan  
Enter roll number: 1023
Enter marks for Subject 1 (0-100): 95
Enter marks for Subject 2 (0-100): 88
Enter marks for Subject 3 (0-100): 92
Enter marks for Subject 4 (0-100): 90
Enter marks for Subject 5 (0-100): 85

==============================================
               RESULT CARD
==============================================
Student Name : Ali Raza Khan
Roll Number  : 1023
----------------------------------------------
Subject 1    : 95 / 100
Subject 2    : 88 / 100
Subject 3    : 92 / 100
Subject 4    : 90 / 100
Subject 5    : 85 / 100
----------------------------------------------
Total Marks  : 450 / 500
Percentage   : 90.00%
Grade        : A+
Final Status : Pass
==============================================
```

**❌ Fail because one subject is below 40 (percentage is 78%)**
```
Enter student name: sara ahmed
Enter roll number: abc
Invalid roll number! Use digits only.
Enter roll number: 2045
Enter marks for Subject 1 (0-100): 85
Enter marks for Subject 2 (0-100): 120
Invalid marks! Marks must be between 0 and 100.
Enter marks for Subject 2 (0-100): xyz
Invalid input! Please enter a number.
Enter marks for Subject 2 (0-100): 90
Enter marks for Subject 3 (0-100): 35
Enter marks for Subject 4 (0-100): 88
Enter marks for Subject 5 (0-100): 92

Student Name : Sara Ahmed
Roll Number  : 2045
Total Marks  : 390 / 500
Percentage   : 78.00%
Grade        : Fail
Final Status : Fail
Note         : Marks below 40 in at least one subject.
```

**❌ Fail because percentage is below 50**
```
Student Name : Usman
Roll Number  : 7
Total Marks  : 238 / 500
Percentage   : 47.60%
Grade        : Fail
Final Status : Fail
```

---

## 📊 Task 2: Class Marks Analyzer

### Description
Collects names and marks of all students in a class using two lists, then prints a full class report.

### Features
- Two lists: `student_names` and `student_marks`, filled with `.append()`
- Every mark is validated (0–100) and asked again if invalid
- Class average, highest and lowest marks with **all** students who got them (ties handled)
- Passing (50 or above) and failing (below 50) count
- Students scoring above the class average
- Marks sorted from highest to lowest

### Custom Functions

| Function | Purpose |
|----------|---------|
| `get_valid_mark(student_name)` | Asks for one mark until it is a number between 0 and 100 |
| `find_students_with_mark(names, marks, target_mark)` | Returns all student names that have a given mark |

### Concepts Used
Lists, `.append()`, `len()`, `sum()`, `max()`, `min()`, `sorted()`, `zip()`, `for` loop with `range()`, `while True` validation, `try / except`, counters, custom functions with parameters and `return`

### ▶️ How to Run
```bash
python class_marks_analyzer.py
```

### 🖥️ Sample Execution

**✅ Normal run with invalid inputs and ties**
```
===== CLASS MARKS ANALYZER =====
Enter number of students: 0
Number of students must be greater than zero.
Enter number of students: abc
Invalid input! Please enter a whole number.
Enter number of students: 5

--- Student 1 ---
Enter student name: ali
Enter marks for Ali (0-100): 80

--- Student 2 ---
Enter student name: sara
Enter marks for Sara (0-100): 150
Invalid marks! Marks must be between 0 and 100.
Enter marks for Sara (0-100): 90

--- Student 3 ---
Enter student name: usman
Enter marks for Usman (0-100): xx
Invalid input! Please enter a number.
Enter marks for Usman (0-100): 90

--- Student 4 ---
Enter student name: hina
Enter marks for Hina (0-100): 40

--- Student 5 ---
Enter student name: bilal
Enter marks for Bilal (0-100): 40

===== CLASS REPORT =====
Total Students : 5
Class Average  : 68.00
Highest Marks  : 90 (Sara, Usman)
Lowest Marks   : 40 (Hina, Bilal)
Passing        : 3
Failing        : 2

--- Students Above Class Average ---
Ali - 80
Sara - 90
Usman - 90

--- Marks (Highest to Lowest) ---
1. Usman - 90
2. Sara - 90
3. Ali - 80
4. Hina - 40
5. Bilal - 40
```

**✅ All students have the same marks**
```
Total Students : 2
Class Average  : 70.00
Highest Marks  : 70 (Ali, Sara)
Lowest Marks   : 70 (Ali, Sara)
Passing        : 2
Failing        : 0

--- Students Above Class Average ---
No student scored above the class average.
```

---

## 🧪 Testing Summary

| Program | Scenario Tested | Result |
|---------|-----------------|--------|
| Result Card | Normal pass with messy name spacing and case | ✅ |
| Result Card | Roll number with letters | ✅ |
| Result Card | Marks above 100 and non-numeric marks | ✅ |
| Result Card | One subject below 40 with high percentage | ✅ |
| Result Card | Percentage below 50 | ✅ |
| Analyzer | Zero and non-numeric student count | ✅ |
| Analyzer | Invalid marks asked again | ✅ |
| Analyzer | Tie for highest and lowest marks | ✅ |
| Analyzer | Nobody above the average | ✅ |

## 🛠️ Requirements

- Python 3.x
- Any terminal and a code editor (VS Code, PyCharm, etc.)
- No external libraries needed

## 👤 Author

**Usama Malik** — Python Functions, Strings & Lists Assessment
