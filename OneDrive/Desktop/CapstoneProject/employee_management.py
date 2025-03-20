import json
import os

# File to store employee data
EMPLOYEE_FILE = "employees.json"

# Load employee data from file
def load_employees():
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "r") as file:
            return json.load(file)
    return {}

# Save employee data to file
def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(employees, file, indent=4)

# Add a new employee
def add_employee():
    employees = load_employees()
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists!")
        return
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    role = input("Enter Role: ")
    employees[emp_id] = {"name": name, "department": department, "role": role}
    save_employees(employees)
    print("Employee added successfully!")

# View all employees
def view_employees():
    employees = load_employees()
    if not employees:
        print("No employees found!")
        return
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, Role: {details['role']}")

# Update an employee
def update_employee():
    employees = load_employees()
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Employee not found!")
        return
    name = input(f"Enter new Name ({employees[emp_id]['name']}): ") or employees[emp_id]['name']
    department = input(f"Enter new Department ({employees[emp_id]['department']}): ") or employees[emp_id]['department']
    role = input(f"Enter new Role ({employees[emp_id]['role']}): ") or employees[emp_id]['role']
    employees[emp_id] = {"name": name, "department": department, "role": role}
    save_employees(employees)
    print("Employee updated successfully!")

# Delete an employee
def delete_employee():
    employees = load_employees()
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id not in employees:
        print("Employee not found!")
        return
    del employees[emp_id]
    save_employees(employees)
    print("Employee deleted successfully!")

# Main menu
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
    # Track employee performance
def track_performance():
    employees = load_employees()
    emp_id = input("Enter Employee ID to track performance: ")
    if emp_id not in employees:
        print("Employee not found!")
        return
    attendance = input("Enter Attendance (out of 100): ")
    projects_completed = input("Enter Number of Projects Completed: ")
    rating = input("Enter Performance Rating (1-5): ")
    employees[emp_id]["performance"] = {
        "attendance": attendance,
        "projects_completed": projects_completed,
        "rating": rating
    }
    save_employees(employees)
    print("Performance tracked successfully!")

# View performance
def view_performance():
    employees = load_employees()
    emp_id = input("Enter Employee ID to view performance: ")
    if emp_id not in employees or "performance" not in employees[emp_id]:
        print("Performance data not found!")
        return
    performance = employees[emp_id]["performance"]
    print(f"Attendance: {performance['attendance']}%")
    print(f"Projects Completed: {performance['projects_completed']}")
    print(f"Rating: {performance['rating']}/5")

# Update the main menu
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Track Performance")
        print("6. View Performance")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            track_performance()
        elif choice == "6":
            view_performance()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
            # Calculate payroll
def calculate_payroll():
    employees = load_employees()
    emp_id = input("Enter Employee ID to calculate payroll: ")
    if emp_id not in employees:
        print("Employee not found!")
        return
    hourly_rate = float(input("Enter Hourly Rate: "))
    hours_worked = float(input("Enter Hours Worked: "))
    salary = hourly_rate * hours_worked
    print(f"Salary for {employees[emp_id]['name']}: ${salary:.2f}")

# Update the main menu
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Track Performance")
        print("6. View Performance")
        print("7. Calculate Payroll")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            track_performance()
        elif choice == "6":
            view_performance()
        elif choice == "7":
            calculate_payroll()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
def add_employee():
    try:
        employees = load_employees()
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Employee ID already exists!")
            return
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        role = input("Enter Role: ")
        employees[emp_id] = {"name": name, "department": department, "role": role}
        save_employees(employees)
        print("Employee added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")