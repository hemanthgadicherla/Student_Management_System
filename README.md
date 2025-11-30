# Student Management System (Python)

A simple console-based Student Management System built using Python. This program helps manage student records by allowing users to add, view, search, update, and delete student details during runtime.

---

## Features

- Add new students  
- View all students  
- Search students by name  
- Update student details (Name, Age, Course, Marks)  
- Delete students by ID  
- Save and exit program  

---

## Student Data Structure

Each student record contains:

- ID  
- Name  
- Age  
- Course  
- Marks  

Data is stored in memory using a list of lists:

```python
[
    [id, name, age, course, marks],
    ...
]
```

---

## Menu Options

```text
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save & Exit
```

---

## How To Run

### Step 1: Install Python
Ensure Python 3 is installed:
```bash
python --version
```

---

### Step 2: Run the Program

Save the file as:
```text
student_management_system.py
```

Run in terminal or VS Code:
```bash
python student_management_system.py
```

---

## Usage

### Add Student
Enter student details:
- ID
- Name
- Age
- Course
- Marks

---

### View Students
Displays all student records in tabular form.

---

### Search Student
Search by student name to display matching results.

---

### Update Student
Choose which field to update:
- name
- age
- course
- marks

Provide the student ID and the updated value.

---

### Delete Student
Delete a student record using the student ID.

---

### Save & Exit
Safely exits the program.

---

## Example Input

```text
Enter your choice: 1
Enter Student ID: 101
Enter Student Name: Alex
Enter Student Age: 20
Enter Student Course: Python
Enter Student Marks: 85
Student added successfully!
```

---

## Limitations

- Data is stored only during runtime (no file storage).
- No validation of numeric inputs.
- Duplicate student IDs are allowed.

---

## Future Enhancements

- Add file-based storage (CSV/JSON)
- Validate inputs
- Prevent duplicate IDs
- Add record sorting
- Build a GUI interface

---

## Author

Created as a beginner-friendly Python learning project to practice:
- Loops
- Lists
- Conditions
- Menu-driven programs
