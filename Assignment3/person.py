import pickle

class Person:
    def __init__(self, id: int, name: str, address: str, contact_details: str):
        """
        Initialize a new Person instance.

        Args:
        id (int): The unique identifier for the person.
        name (str): The name of the person.
        address (str): The address of the person.
        contact_details (str): Contact details of the person.

        Examples:
        >>> p = Person(1, "John Doe", "123 Elm St", "555-1234")
        >>> p.name
        'John Doe'
        """
        self.id = id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def __str__(self):
        """
        Return a string representation of the person.

        Examples:
        >>> p = Person(1, "John Doe", "123 Elm St", "555-1234")
        >>> str(p)
        'ID: 1, Name: John Doe, Address: 123 Elm St, Contact: 555-1234'
        """
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}, Contact: {self.contact_details}"
import tkinter as tk
from tkinter import messagebox, simpledialog

def add_person():
    id = simpledialog.askinteger("Add Person", "Enter ID:")
    name = simpledialog.askstring("Add Person", "Enter Name:")
    address = simpledialog.askstring("Add Person", "Enter Address:")
    contact = simpledialog.askstring("Add Person", "Enter Contact Details:")
    person = Person(id, name, address, contact)
    with open(f"{id}.pkl", "wb") as out_file:
        pickle.dump(person, out_file)
    messagebox.showinfo("Add Person", "Person added successfully!")

def delete_person():
    id = simpledialog.askinteger("Delete Person", "Enter ID to Delete:")
    try:
        os.remove(f"{id}.pkl")
        messagebox.showinfo("Delete Person", "Person deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Person", "Person not found!")

def modify_person():
    # Similar to add_person but loads an existing person and modifies them
    pass

def display_person():
    id = simpledialog.askinteger("Display Person", "Enter ID:")
    try:
        with open(f"{id}.pkl", "rb") as in_file:
            person = pickle.load(in_file)
        messagebox.showinfo("Display Person", str(person))
    except FileNotFoundError:
        messagebox.showerror("Display Person", "Person not found!")

# Main GUI Setup
root = tk.Tk()
root.title("Person Manager")

# Buttons
add_button = tk.Button(root, text="Add Person", command=add_person)
delete_button = tk.Button(root, text="Delete Person", command=delete_person)
modify_button = tk.Button(root, text="Modify Person", command=modify_person)
display_button = tk.Button(root, text="Display Person", command=display_person)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()

