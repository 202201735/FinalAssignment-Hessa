import pickle

class Guest:
    def __init__(self, guest_id: int, name: str, address: str, contact_details: str):
        """
        Initialize a new Guest instance.

        Args:
            guest_id (int): Unique identifier for the guest.
            name (str): Name of the guest.
            address (str): Residential address of the guest.
            contact_details (str): Contact details of the guest.
        """
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def __str__(self):
        """
        Return a string representation of the guest.
        """
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Address: {self.address}, Contact: {self.contact_details}"


import tkinter as tk
from tkinter import messagebox, simpledialog
import os


def add_guest():
    guest_id = simpledialog.askinteger("Add Guest", "Enter Guest ID:")
    name = simpledialog.askstring("Add Guest", "Enter Name:")
    address = simpledialog.askstring("Add Guest", "Enter Address:")
    contact_details = simpledialog.askstring("Add Guest", "Enter Contact Details:")

    guest = Guest(guest_id, name, address, contact_details)
    with open(f"guest_{guest_id}.pkl", "wb") as out_file:
        pickle.dump(guest, out_file)
    messagebox.showinfo("Add Guest", "Guest added successfully!")


def display_guest():
    guest_id = simpledialog.askinteger("Display Guest", "Enter Guest ID:")
    try:
        with open(f"guest_{guest_id}.pkl", "rb") as in_file:
            guest = pickle.load(in_file)
        messagebox.showinfo("Display Guest", str(guest))
    except FileNotFoundError:
        messagebox.showerror("Display Guest", "Guest not found!")


def delete_guest():
    guest_id = simpledialog.askinteger("Delete Guest", "Enter Guest ID to Delete:")
    try:
        os.remove(f"guest_{guest_id}.pkl")
        messagebox.showinfo("Delete Guest", "Guest deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Guest", "Guest not found!")


def modify_guest():
    guest_id = simpledialog.askinteger("Modify Guest", "Enter Guest ID:")
    try:
        with open(f"guest_{guest_id}.pkl", "rb") as in_file:
            guest = pickle.load(in_file)

        # Ask for new details
        name = simpledialog.askstring("Modify Guest", "Enter Name:", initialvalue=guest.name)
        address = simpledialog.askstring("Modify Guest", "Enter Address:", initialvalue=guest.address)
        contact_details = simpledialog.askstring("Modify Guest", "Enter Contact Details:",
                                                 initialvalue=guest.contact_details)

        # Update guest details
        guest.name = name
        guest.address = address
        guest.contact_details = contact_details

        with open(f"guest_{guest_id}.pkl", "wb") as out_file:
            pickle.dump(guest, out_file)
        messagebox.showinfo("Modify Guest", "Guest modified successfully!")
    except FileNotFoundError:
        messagebox.showerror("Modify Guest", "Guest not found!")


# Main GUI Setup
root = tk.Tk()
root.title("Guest Manager")

# Buttons
add_button = tk.Button(root, text="Add Guest", command=add_guest)
delete_button = tk.Button(root, text="Delete Guest", command=delete_guest)
modify_button = tk.Button(root, text="Modify Guest", command=modify_guest)
display_button = tk.Button(root, text="Display Guest", command=display_guest)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()
