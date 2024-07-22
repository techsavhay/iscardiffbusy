import tkinter as tk
from tkinter import messagebox
import pyodbc

# Database connection setup
def get_database_connection():
    return pyodbc.connect('Driver={SQL Server};'
                          'Server=Your_Server_Name;'
                          'Database=Your_Database_Name;'
                          'Trusted_Connection=yes;')

# Function to add an employee to the database
def add_employee(name, position, salary):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "Employee added successfully!")

# Function to get employee information from the database
def get_employee_info(employee_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
    employee_data = cursor.fetchone()
    connection.close()

    if employee_data:
        messagebox.showinfo("Employee Info", f"Name: {employee_data[1]}\nPosition: {employee_data[2]}\nSalary: {employee_data[3]}")
    else:
        messagebox.showwarning("Not Found", "Employee not found")

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
