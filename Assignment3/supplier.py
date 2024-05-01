import pickle

class Supplier:
    def __init__(self, supplier_id: int, name: str, address: str, contact_details: str):
        """
        Initialize a new Supplier instance.

        Args:
            supplier_id (int): The unique identifier for the supplier.
            name (str): The name of the supplier.
            address (str): The address of the supplier.
            contact_details (str): Contact details of the supplier.

        Examples:
        >>> s = Supplier(1, "ABC Corp", "456 Oak St", "555-6789")
        >>> s.name
        'ABC Corp'
        """
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def __str__(self):
        """
        Return a string representation of the supplier.

        Examples:
        >>> s = Supplier(1, "ABC Corp", "456 Oak St", "555-6789")
        >>> str(s)
        'Supplier ID: 1, Name: ABC Corp, Address: 456 Oak St, Contact: 555-6789'
        """
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Address: {self.address}, Contact: {self.contact_details}"


import tkinter as tk
from tkinter import messagebox, simpledialog


def add_supplier():
    supplier_id = simpledialog.askinteger("Add Supplier", "Enter Supplier ID:")
    name = simpledialog.askstring("Add Supplier", "Enter Name:")
    address = simpledialog.askstring("Add Supplier", "Enter Address:")
    contact_details = simpledialog.askstring("Add Supplier", "Enter Contact Details:")

    supplier = Supplier(supplier_id, name, address, contact_details)
    with open(f"supplier_{supplier_id}.pkl", "wb") as out_file:
        pickle.dump(supplier, out_file)
    messagebox.showinfo("Add Supplier", "Supplier added successfully!")


def delete_supplier():
    supplier_id = simpledialog.askinteger("Delete Supplier", "Enter Supplier ID to Delete:")
    try:
        os.remove(f"supplier_{supplier_id}.pkl")
        messagebox.showinfo("Delete Supplier", "Supplier deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Supplier", "Supplier not found!")


def modify_supplier():
    # This function should ideally fetch, modify, and re-save a Supplier
    # Similar to modify_employee but for Supplier
    pass


def display_supplier():
    supplier_id = simpledialog.askinteger("Display Supplier", "Enter Supplier ID:")
    try:
        with open(f"supplier_{supplier_id}.pkl", "rb") as in_file:
            supplier = pickle.load(in_file)
        messagebox.showinfo("Display Supplier", str(supplier))
    except FileNotFoundError:
        messagebox.showerror("Display Supplier", "Supplier not found!")


# Main GUI Setup
root = tk.Tk()
root.title("Supplier Manager")

# Buttons
add_button = tk.Button(root, text="Add Supplier", command=add_supplier)
delete_button = tk.Button(root, text="Delete Supplier", command=delete_supplier)
modify_button = tk.Button(root, text="Modify Supplier", command=modify_supplier)
display_button = tk.Button(root, text="Display Supplier", command=display_supplier)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()
