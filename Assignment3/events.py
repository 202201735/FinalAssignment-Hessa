import pickle
from datetime import datetime
from typing import List

class Event:
    def __init__(self, event_id: int, event_type: str, theme: str, date: datetime,
                 time: str, duration: float, venue_address: str, client_id: int,
                 guest_list: List[str], catering_company: str, cleaning_company: str,
                 decorations_company: str, entertainment_company: str,
                 furniture_supply_company: str, invoice: str):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice

    def __str__(self):
        return f"Event ID: {self.event_id}, Type: {self.event_type}, Theme: {self.theme}, Date: {self.date.strftime('%Y-%m-%d')}, Time: {self.time}, Duration: {self.duration} hours, Venue: {self.venue_address}, Client ID: {self.client_id}, Guests: {len(self.guest_list)}"

    def save(self):
        with open(f"event_{self.event_id}.pkl", "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load(event_id):
        try:
            with open(f"event_{self.event_id}.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None

import tkinter as tk
from tkinter import messagebox, simpledialog, simpledialog, Toplevel, Label, Entry, Button
import os

def add_event():
    # This dialog would collect all necessary information from the user
    # For simplicity, let's assume all inputs are valid and provided
    event_id = simpledialog.askinteger("Add Event", "Enter Event ID:")
    if event_id is None:
        return
    event_type = simpledialog.askstring("Add Event", "Enter Event Type:")
    theme = simpledialog.askstring("Add Event", "Enter Theme:")
    date = simpledialog.askstring("Add Event", "Enter Date (YYYY-MM-DD):")
    time = simpledialog.askstring("Add Event", "Enter Time (HH:MM):")
    duration = simpledialog.askfloat("Add Event", "Enter Duration in hours:")
    venue_address = simpledialog.askstring("Add Event", "Enter Venue Address:")
    client_id = simpledialog.askinteger("Add Event", "Enter Client ID:")
    # Simplifications are made here for guest list and company details
    guest_list = simpledialog.askstring("Add Event", "Enter Guest Names (comma-separated):").split(',')
    catering_company = simpledialog.askstring("Add Event", "Enter Catering Company:")
    cleaning_company = simpledialog.askstring("Add Event", "Enter Cleaning Company:")
    decorations_company = simpledialog.askstring("Add Event", "Enter Decorations Company:")
    entertainment_company = simpledialog.askstring("Add Event", "Enter Entertainment Company:")
    furniture_supply_company = simpledialog.askstring("Add Event", "Enter Furniture Supply Company:")
    invoice = simpledialog.askstring("Add Event", "Enter Invoice Details:")

    # Parse the date and time
    date = datetime.strptime(date, "%Y-%m-%d")

    event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id,
                  guest_list, catering_company, cleaning_company, decorations_company,
                  entertainment_company, furniture_supply_company, invoice)
    event.save()
    messagebox.showinfo("Add Event", "Event added successfully!")

def display_event():
    event_id = simpledialog.askinteger("Display Event", "Enter Event ID:")
    event = Event.load(event_id)
    if event:
        messagebox.showinfo("Display Event", str(event))
    else:
        messagebox.showerror("Display Event", "Event not found!")

def delete_event():
    event_id = simpledialog.askinteger("Delete Event", "Enter Event ID:")
    if event_id is None:
        return
    try:
        os.remove(f"event_{event_id}.pkl")
        messagebox.showinfo("Delete Event", "Event deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Event", "Event not found!")

def modify_event():
    event_id = simpledialog.askinteger("Modify Event", "Enter Event ID:")
    event = Event.load(event_id)
    if not event:
        messagebox.showerror("Modify Event", "Event not found!")
        return

    # Assume that we only allow modifying the theme for simplicity
    new_theme = simpledialog.askstring("Modify Event", "Enter new theme:", initialvalue=event.theme)
    if new_theme:
        event.theme = new_theme
        event.save()
        messagebox.showinfo("Modify Event", "Event modified successfully!")

# Main GUI Setup
root = tk.Tk()
root.title("Event Manager")

# Buttons
add_button = tk.Button(root, text="Add Event", command=add_event)
delete_button = tk.Button(root, text="Delete Event", command=delete_event)
modify_button = tk.Button(root, text="Modify Event", command=modify_event)
display_button = tk.Button(root, text="Display Event", command=display_event)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()
