import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

while True:

    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter name: ")
        age = int(input("Enter age: "))

        cursor.execute(
            "INSERT INTO students(name, age) VALUES (?, ?)",
            (name, age)
        )

        conn.commit()

    elif choice == "2":

        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()

        for row in rows:

            print(row)

    elif choice == "3":

        break

    else:

        print("Invalid choice")

conn.close()