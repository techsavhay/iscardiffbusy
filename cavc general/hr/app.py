import tkinter as tk
from tkinter import ttk, messagebox
from employee import Employee
from database import Database

class HRApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HR Management System")
        self.database = Database()
        self.initialize_ui()

    def initialize_ui(self):
        self.label_name = tk.Label(self.root, text="Employee Name")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()

        self.label_position = tk.Label(self.root, text="Position")
        self.label_position.pack()

        self.entry_position = tk.Entry(self.root)
        self.entry_position.pack()

        self.label_salary = tk.Label(self.root, text="Salary")
        self.label_salary.pack()

        self.entry_salary = tk.Entry(self.root)
        self.entry_salary.pack()

        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.info_button = tk.Button(self.root, text="Get Employee Info", command=self.get_employee_info)
        self.info_button.pack()

    def add_employee(self):
        name = self.entry_name.get()
        position = self.entry_position.get()
        salary = self.entry_salary.get()
        if name and position and salary:
            try:
                salary = float(salary)
                new_employee = Employee(name, position, salary)
                self.database.add_employee(new_employee)
                messagebox.showinfo("Success", "Employee added successfully!")
                self.entry_name.delete(0, tk.END)
                self.entry_position.delete(0, tk.END)
                self.entry_salary.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter a valid salary")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def get_employee_info(self):
        employee_id = self.entry_name.get()
        if employee_id:
            try:
                employee_id = int(employee_id)
                employee = self.database.get_employee_info(employee_id)
                if employee:
                    messagebox.showinfo("Employee Info", f"Name: {employee.name}\nPosition: {employee.position}\nSalary: {employee.salary}")
                else:
                    messagebox.showwarning("Not Found", "Employee not found")
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter a valid employee ID")
        else:
            messagebox.showwarning("Input Error", "Please enter an employee ID")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HRApp()
    app.run()
