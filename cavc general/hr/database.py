import pyodbc
from employee import Employee

class Database:
    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQL Server};'
                                         'Server=Your_Server_Name;'
                                         'Database=Your_Database_Name;'
                                         'Trusted_Connection=yes;')

    def add_employee(self, employee):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
                       (employee.name, employee.position, employee.salary))
        self.connection.commit()

    def get_employee_info(self, employee_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
        employee_data = cursor.fetchone()
        if employee_data:
            return Employee(employee_data[1], employee_data[2], employee_data[3])

    # Other database operations
