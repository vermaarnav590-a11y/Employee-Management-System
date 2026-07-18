import sqlite3


connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary REAL
)
""")

connection.commit()

while True:

    print("\n" + "=" * 70)
    print("              EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 70)

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\nADD EMPLOYEE")
        print("-" * 40)

        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        department = input("Enter Department: ").strip()
        salary = float(input("Enter Salary: "))

        cursor.execute(
            "INSERT INTO employees(name, age, department, salary) VALUES (?, ?, ?, ?)",
            (name, age, department, salary)
        )

        connection.commit()

        print("\n✅ Employee Added Successfully!")

    elif choice == "2":

        cursor.execute("SELECT * FROM employees")

        employees = cursor.fetchall()

        if not employees:

            print("\nNo employee records found.")

        else:

            print("\n" + "-" * 70)
            print(f"{'ID':<5}{'NAME':<20}{'AGE':<8}{'DEPARTMENT':<20}{'SALARY'}")
            print("-" * 70)

            for employee in employees:

                print(
                    f"{employee[0]:<5}"
                    f"{employee[1]:<20}"
                    f"{employee[2]:<8}"
                    f"{employee[3]:<20}"
                    f"{employee[4]}"
                )

            print("-" * 70)

    elif choice == "3":

        employee_id = input("\nEnter Employee ID: ")

        cursor.execute(
            "SELECT * FROM employees WHERE id=?",
            (employee_id,)
        )

        employee = cursor.fetchone()

        if employee:

            print("\nEmployee Found")
            print("-" * 40)
            print("ID         :", employee[0])
            print("Name       :", employee[1])
            print("Age        :", employee[2])
            print("Department :", employee[3])
            print("Salary     :", employee[4])

        else:

            print("\n❌ Employee not found!")

    elif choice == "4":

        employee_id = input("\nEnter Employee ID to Update: ")

        cursor.execute(
            "SELECT * FROM employees WHERE id=?",
            (employee_id,)
        )

        employee = cursor.fetchone()

        if employee:

            print("\nCurrent Details")
            print("-" * 40)
            print("Name       :", employee[1])
            print("Age        :", employee[2])
            print("Department :", employee[3])
            print("Salary     :", employee[4])

            print("\nEnter New Details")

            name = input("New Name: ").strip()
            age = int(input("New Age: "))
            department = input("New Department: ").strip()
            salary = float(input("New Salary: "))

            cursor.execute(
                """
                UPDATE employees
                SET name=?, age=?, department=?, salary=?
                WHERE id=?
                """,
                (name, age, department, salary, employee_id)
            )

            connection.commit()

            print("\n✅ Employee Updated Successfully!")

        else:

            print("\n❌ Employee not found!")

    elif choice == "5":
        emp_id = input("Enter Employee ID to Delete: ")
        cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
        emp = cursor.fetchone()

        if emp:
            confirm = input(f"Delete {emp[1]}? (Y/N): ").strip().upper()

            if confirm == "Y":
                cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
                connection.commit()
                print("Employee deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Employee not found.")

    elif choice == "6":
        connection.close()
        print("\nThank you for using Employee Management System!")
        break

    else:
        print("Invalid choice.")