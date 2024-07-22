import tkinter as tk
from tkinter import messagebox

# Global list to store employee data (simulating a database)
employees = []

# Function to add an employee
def add_employee(name, position, salary):
    employees.append({
        'name': name,
        'position': position,
        'salary': salary
    })
    messagebox.showinfo("Success", "Employee added successfully!")

# Function to get employee information
def get_employee_info(employee_id):
    try:
        employee_id = int(employee_id)
        employee = employees[employee_id - 1]  # Adjusting for 1-based index
        messagebox.showinfo("Employee Info", f"Name: {employee['name']}\nPosition: {employee['position']}\nSalary: {employee['salary']}")
    except IndexError:
        messagebox.showwarning("Not Found", "Employee not found")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid employee ID")

# GUI setup
def setup_gui(root):
    root.title("HR Management System")
    root.geometry("400x300")  # Set initial window size to 400x300 pixels

    label_name = tk.Label(root, text="Employee Name")
    label_name.pack()

    entry_name = tk.Entry(root)
    entry_name.pack()

    label_position = tk.Label(root, text="Position")
    label_position.pack()

    entry_position = tk.Entry(root)
    entry_position.pack()

    label_salary = tk.Label(root, text="Salary")
    label_salary.pack()

    entry_salary = tk.Entry(root)
    entry_salary.pack()

    add_button = tk.Button(root, text="Add Employee", command=lambda: add_employee(entry_name.get(), entry_position.get(), entry_salary.get()))
    add_button.pack()

    label_employee_id = tk.Label(root, text="Employee ID")
    label_employee_id.pack()

    entry_employee_id = tk.Entry(root)
    entry_employee_id.pack()

    info_button = tk.Button(root, text="Get Employee Info", command=lambda: get_employee_info(entry_employee_id.get()))
    info_button.pack()

# Main function to run the application
def main():
    root = tk.Tk()
    setup_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
