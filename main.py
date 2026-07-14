import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        cursor.execute(
            "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )
        conn.commit()
        print("Student Added Successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if students:
            for student in students:
                print(student)
        else:
            print("No Students Found!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

conn.close()
# menu
print("\n===== Student Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")
 #search students 
elif choice == "3":
    name = input("Enter student name: ")
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    student = cursor.fetchall()

    if student:
        for s in student:
            print(s)
    else:
        print("Student not found!")
#update student 
elif choice == "4":
    student_id = input("Enter Student ID: ")
    new_name = input("Enter New Name: ")
    new_age = input("Enter New Age: ")
    new_course = input("Enter New Course: ")

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (new_name, new_age, new_course, student_id)
    )
    conn.commit()
    print("Student Updated Successfully!")
# del stu
elif choice == "5":
    student_id = input("Enter Student ID: ")

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    print("Student Deleted Successfully!")
#breck
elif choice == "6":
    print("Thank You!")
    break
