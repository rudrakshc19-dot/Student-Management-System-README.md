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