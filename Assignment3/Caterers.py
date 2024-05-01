import pickle

class Caterer:
    def __init__(self, caterer_id: int, name: str, address: str, contact_details: str, menu: str, min_guests: int, max_guests: int):
        """
        Initialize a new Caterer instance.

        Args:
            caterer_id (int): Unique identifier for the caterer.
            name (str): Name of the caterer.
            address (str): Address of the caterer.
            contact_details (str): Contact details of the caterer.
            menu (str): Description of the menu offered.
            min_guests (int): Minimum number of guests required for service.
            max_guests (int): Maximum number of guests that can be catered for.
        """
        self.caterer_id = caterer_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    def __str__(self):
        """
        Return a string representation of the caterer.
        """
        return (f"Caterer ID: {self.caterer_id}, Name: {self.name}, Address: {self.address}, "
                f"Contact: {self.contact_details}, Menu: {self.menu}, "
                f"Min Guests: {self.min_guests}, Max Guests: {self.max_guests}")


import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle
import os


class Caterer:
    def __init__(self, caterer_id: int, name: str, address: str, contact_details: str, menu: str, min_guests: int,
                 max_guests: int):
        self.caterer_id = caterer_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    def __str__(self):
        return (f"Caterer ID: {self.caterer_id}, Name: {self.name}, Address: {self.address}, "
                f"Contact: {self.contact_details}, Menu: {self.menu}, "
                f"Min Guests: {self.min_guests}, Max Guests: {self.max_guests}")


def add_caterer():
    try:
        caterer_id = simpledialog.askinteger("Add Caterer", "Enter Caterer ID:")
        if caterer_id is None: return
        name = simpledialog.askstring("Add Caterer", "Enter Name:")
        if name is None: return
        address = simpledialog.askstring("Add Caterer", "Enter Address:")
        if address is None: return
        contact_details = simpledialog.askstring("Add Caterer", "Enter Contact Details:")
        if contact_details is None: return
        menu = simpledialog.askstring("Add Caterer", "Enter Menu Description:")
        if menu is None: return
        min_guests = simpledialog.askinteger("Add Caterer", "Enter Minimum Number of Guests:")
        if min_guests is None: return
        max_guests = simpledialog.askinteger("Add Caterer", "Enter Maximum Number of Guests:")
        if max_guests is None: return

        caterer = Caterer(caterer_id, name, address, contact_details, menu, min_guests, max_guests)
        with open(f"caterer_{caterer_id}.pkl", "wb") as out_file:
            pickle.dump(caterer, out_file)
        messagebox.showinfo("Add Caterer", "Caterer added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def display_caterer():
    try:
        caterer_id = simpledialog.askinteger("Display Caterer", "Enter Caterer ID:")
        if caterer_id is None: return
        with open(f"caterer_{caterer_id}.pkl", "rb") as in_file:
            caterer = pickle.load(in_file)
        messagebox.showinfo("Display Caterer", str(caterer))
    except FileNotFoundError:
        messagebox.showerror("Display Caterer", "Caterer not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_caterer():
    try:
        caterer_id = simpledialog.askinteger("Delete Caterer", "Enter Caterer ID to Delete:")
        if caterer_id is None: return
        os.remove(f"caterer_{caterer_id}.pkl")
        messagebox.showinfo("Delete Caterer", "Caterer deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Caterer", "Caterer not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def modify_caterer():
    try:
        caterer_id = simpledialog.askinteger("Modify Caterer", "Enter Caterer ID:")
        if caterer_id is None: return
        with open(f"caterer_{caterer_id}.pkl", "rb") as in_file:
            caterer = pickle.load(in_file)

        name = simpledialog.askstring("Modify Caterer", "Enter Name:", initialvalue=caterer.name)
        if name is None: return
        address = simpledialog.askstring("Modify Caterer", "Enter Address:", initialvalue=caterer.address)
        if address is None: return
        contact_details = simpledialog.askstring("Modify Caterer", "Enter Contact Details:",
                                                 initialvalue=caterer.contact_details)
        if contact_details is None: return
        menu = simpledialog.askstring("Modify Caterer", "Enter Menu Description:", initialvalue=caterer.menu)
        if menu is None: return
        min_guests = simpledialog.askinteger("Modify Caterer", "Enter Minimum Number of Guests:",
                                             initialvalue=caterer.min_guests)
        if min_guests is None: return
        max_guests = simpledialog.askinteger("Modify Caterer", "Enter Maximum Number of Guests:",
                                             initialvalue=caterer.max_guests)
        if max_guests is None: return

        caterer.name = name
        caterer.address = address
        caterer.contact_details = contact_details
        caterer.menu = menu
        caterer.min_guests = min_guests
        caterer.max_guests = max_guests

        with open(f"caterer_{caterer_id}.pkl", "wb") as out_file:
            pickle.dump(caterer, out_file)
        messagebox.showinfo("Modify Caterer", "Caterer modified successfully!")
    except FileNotFoundError:
        messagebox.showerror("Modify Caterer", "Caterer not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main GUI Setup
root = tk.Tk()
root.title("Caterer Manager")

# Buttons
add_button = tk.Button(root, text="Add Caterer", command=add_caterer)
delete_button = tk.Button(root, text="Delete Caterer", command=delete_caterer)
modify_button = tk.Button(root, text="Modify Caterer", command=modify_caterer)
display_button = tk.Button(root, text="Display Caterer", command=display_caterer)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()



