import pickle
from datetime import date

class Person:
    def __init__(self, name: str, address: str, contact_details: str):
        """
        Initialize a new Person instance.

        Args:
            name (str): The name of the person.
            address (str): The address of the person.
            contact_details (str): Contact details of the person.
        """
        self.name = name
        self.address = address
        self.contact_details = contact_details

class Employee(Person):
    def __init__(self, name: str, address: str, contact_details: str,
                 employee_id: int, department: str, job_title: str,
                 basic_salary: float, age: int, date_of_birth: date,
                 passport_details: str):
        """
        Initialize a new Employee instance.

        Args:
            name (str): The name of the person.
            address (str): The address of the person.
            contact_details (str): Contact details of the person.
            employee_id (int): Unique identifier for the employee.
            department (str): Department where the employee works.
            job_title (str): Job title of the employee.
            basic_salary (float): Basic salary of the employee.
            age (int): Age of the employee.
            date_of_birth (date): Date of birth of the employee.
            passport_details (str): Passport details of the employee.

        Examples:
        >>> e = Employee("hessa", "use", "555-9876", 101, "HR", "Manager", 50000, 30, date(2004, 7, 30), "AB1234567")
        >>> e.name
        'hessa'
        """
        super().__init__(name, address, contact_details)
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    def __str__(self):
        """
        Return a string representation of the employee.

        Examples:
        >>> e = Employee("hessa", "uae", "555-9876", 101, "HR", "Manager", 50000, 30, date(2004, 7, 30), "AB1234567")
        >>> str(e)
        'Employee ID: 101, Name: hessa, Department: HR, Job Title: Manager, Salary: $50000'
        """
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Job Title: {self.job_title}, Salary: ${self.basic_salary}"

import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle
from datetime import datetime

# Assuming the Employee class is defined as previously described

def add_employee():
    name = simpledialog.askstring("Add Employee", "Enter Name:")
    address = simpledialog.askstring("Add Employee", "Enter Address:")
    contact_details = simpledialog.askstring("Add Employee", "Enter Contact Details:")
    employee_id = simpledialog.askinteger("Add Employee", "Enter Employee ID:")
    department = simpledialog.askstring("Add Employee", "Enter Department:")
    job_title = simpledialog.askstring("Add Employee", "Enter Job Title:")
    basic_salary = simpledialog.askfloat("Add Employee", "Enter Basic Salary:")
    age = simpledialog.askinteger("Add Employee", "Enter Age:")
    date_of_birth = simpledialog.askstring("Add Employee", "Enter Date of Birth (YYYY-MM-DD):")
    passport_details = simpledialog.askstring("Add Employee", "Enter Passport Details:")
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()  # Convert string to date

    employee = Employee(name, address, contact_details, employee_id, department, job_title,
                        basic_salary, age, date_of_birth, passport_details)
    with open(f"employee_{employee_id}.pkl", "wb") as out_file:
        pickle.dump(employee, out_file)
    messagebox.showinfo("Add Employee", "Employee added successfully!")

def delete_employee():
    employee_id = simpledialog.askinteger("Delete Employee", "Enter Employee ID to Delete:")
    try:
        os.remove(f"employee_{employee_id}.pkl")
        messagebox.showinfo("Delete Employee", "Employee deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Employee", "Employee not found!")

def modify_employee():
    # This function should ideally fetch, modify, and re-save an Employee
    # The functionality is similar to add_employee but includes a load step
    pass

def display_employee():
    employee_id = simpledialog.askinteger("Display Employee", "Enter Employee ID:")
    try:
        with open(f"employee_{employee_id}.pkl", "rb") as in_file:
            employee = pickle.load(in_file)
        messagebox.showinfo("Display Employee", str(employee))
    except FileNotFoundError:
        messagebox.showerror("Display Employee", "Employee not found!")

# Main GUI Setup
root = tk.Tk()
root.title("Employee Manager")

# Buttons
add_button = tk.Button(root, text="Add Employee", command=add_employee)
delete_button = tk.Button(root, text="Delete Employee", command=delete_employee)
modify_button = tk.Button(root, text="Modify Employee", command=modify_employee)
display_button = tk.Button(root, text="Display Employee", command=display_employee)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()
