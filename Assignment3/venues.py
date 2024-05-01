import pickle

class Venue:
    def __init__(self, venue_id: int, name: str, address: str, contact: str, min_guests: int, max_guests: int):
        """
        Initialize a new Venue instance.
        Args:
            venue_id (int): Unique identifier for the venue.
            name (str): Name of the venue.
            address (str): Address of the venue.
            contact (str): Contact details for the venue.
            min_guests (int): Minimum number of guests the venue can accommodate.
            max_guests (int): Maximum number of guests the venue can accommodate.
        """
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    def __str__(self):
        """
        Return a string representation of the venue.
        """
        return (f"Venue ID: {self.venue_id}, Name: {self.name}, Address: {self.address}, "
                f"Contact: {self.contact}, Min Guests: {self.min_guests}, Max Guests: {self.max_guests}")

    def save(self):
        with open(f"venue_{self.venue_id}.pkl", "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load(venue_id):
        try:
            with open(f"venue_{venue_id}.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

def add_venue():
    venue_id = simpledialog.askinteger("Add Venue", "Enter Venue ID:")
    if venue_id is None:
        return
    name = simpledialog.askstring("Add Venue", "Enter Name:")
    if name is None:
        return
    address = simpledialog.askstring("Add Venue", "Enter Address:")
    if address is None:
        return
    contact = simpledialog.askstring("Add Venue", "Enter Contact:")
    if contact is None:
        return
    min_guests = simpledialog.askinteger("Add Venue", "Enter Minimum Number of Guests:")
    if min_guests is None:
        return
    max_guests = simpledialog.askinteger("Add Venue", "Enter Maximum Number of Guests:")
    if max_guests is None:
        return

    venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
    venue.save()
    messagebox.showinfo("Add Venue", "Venue added successfully!")

def display_venue():
    venue_id = simpledialog.askinteger("Display Venue", "Enter Venue ID:")
    venue = Venue.load(venue_id)
    if venue:
        messagebox.showinfo("Display Venue", str(venue))
    else:
        messagebox.showerror("Display Venue", "Venue not found!")

def delete_venue():
    venue_id = simpledialog.askinteger("Delete Venue", "Enter Venue ID:")
    if venue_id is None:
        return
    try:
        os.remove(f"venue_{venue_id}.pkl")
        messagebox.showinfo("Delete Venue", "Venue deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Venue", "Venue not found!")

def modify_venue():
    venue_id = simpledialog.askinteger("Modify Venue", "Enter Venue ID:")
    venue = Venue.load(venue_id)
    if not venue:
        messagebox.showerror("Modify Venue", "Venue not found!")
        return

    name = simpledialog.askstring("Modify Venue", "Enter new name:", initialvalue=venue.name)
    if name is None:
        return
    address = simpledialog.askstring("Modify Venue", "Enter new address:", initialvalue=venue.address)
    if address is None:
        return
    contact = simpledialog.askstring("Modify Venue", "Enter new contact:", initialvalue=venue.contact)
    if contact is None:
        return
    min_guests = simpledialog.askinteger("Modify Venue", "Enter new minimum number of guests:", initialvalue=venue.min_guests)
    if min_guests is None:
        return
    max_guests = simpledialog.askinteger("Modify Venue", "Enter new maximum number of guests:", initialvalue=venue.max_guests)
    if max_guests is None:
        return

    venue.name = name
    venue.address = address
    venue.contact = contact
    venue.min_guests = min_guests
    venue.max_guests = max_guests
    venue.save()
    messagebox.showinfo("Modify Venue", "Venue modified successfully!")

# Main GUI Setup
root = tk.Tk()
root.title("Venue Manager")

# Buttons
add_button = tk.Button(root, text="Add Venue", command=add_venue)
delete_button = tk.Button(root, text="Delete Venue", command=delete_venue)
modify_button = tk.Button(root, text="Modify Venue", command=modify_venue)
display_button = tk.Button(root, text="Display Venue", command=display_venue)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()
