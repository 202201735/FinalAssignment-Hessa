import pickle

class Client:
    def __init__(self, client_id: int, name: str, address: str, contact_details: str, budget: float):
        """
        Initialize a new Client instance.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Name of the client.
            address (str): Residential address of the client.
            contact_details (str): Contact details of the client.
            budget (float): Financial budget of the client.
        """
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def __str__(self):
        """
        Return a string representation of the client.
        """
        return f"Client ID: {self.client_id}, Name: {self.name}, Address: {self.address}, Contact: {self.contact_details}, Budget: ${self.budget:.2f}"


import tkinter as tk
from tkinter import messagebox, simpledialog
import os


def add_client():
    client_id = simpledialog.askinteger("Add Client", "Enter Client ID:")
    name = simpledialog.askstring("Add Client", "Enter Name:")
    address = simpledialog.askstring("Add Client", "Enter Address:")
    contact_details = simpledialog.askstring("Add Client", "Enter Contact Details:")
    budget = simpledialog.askfloat("Add Client", "Enter Budget:")

    client = Client(client_id, name, address, contact_details, budget)
    with open(f"client_{client_id}.pkl", "wb") as out_file:
        pickle.dump(client, out_file)
    messagebox.showinfo("Add Client", "Client added successfully!")


def display_client():
    client_id = simpledialog.askinteger("Display Client", "Enter Client ID:")
    try:
        with open(f"client_{client_id}.pkl", "rb") as in_file:
            client = pickle.load(in_file)
        messagebox.showinfo("Display Client", str(client))
    except FileNotFoundError:
        messagebox.showerror("Display Client", "Client not found!")


def delete_client():
    client_id = simpledialog.askinteger("Delete Client", "Enter Client ID to Delete:")
    try:
        os.remove(f"client_{client_id}.pkl")
        messagebox.showinfo("Delete Client", "Client deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Delete Client", "Client not found!")


def modify_client():
    client_id = simpledialog.askinteger("Modify Client", "Enter Client ID:")
    try:
        with open(f"client_{client_id}.pkl", "rb") as in_file:
            client = pickle.load(in_file)

        # Ask for new details
        name = simpledialog.askstring("Modify Client", "Enter Name:", initialvalue=client.name)
        address = simpledialog.askstring("Modify Client", "Enter Address:", initialvalue=client.address)
        contact_details = simpledialog.askstring("Modify Client", "Enter Contact Details:",
                                                 initialvalue=client.contact_details)
        budget = simpledialog.askfloat("Modify Client", "Enter Budget:", initialvalue=client.budget)

        # Update client details
        client.name = name
        client.address = address
        client.contact_details = contact_details
        client.budget = budget

        with open(f"client_{client_id}.pkl", "wb") as out_file:
            pickle.dump(client, out_file)
        messagebox.showinfo("Modify Client", "Client modified successfully!")
    except FileNotFoundError:
        messagebox.showerror("Modify Client", "Client not found!")


# Main GUI Setup
root = tk.Tk()
root.title("Client Manager")

# Buttons
add_button = tk.Button(root, text="Add Client", command=add_client)
delete_button = tk.Button(root, text="Delete Client", command=delete_client)
modify_button = tk.Button(root, text="Modify Client", command=modify_client)
display_button = tk.Button(root, text="Display Client", command=display_client)

add_button.pack(pady=5)
delete_button.pack(pady=5)
modify_button.pack(pady=5)
display_button.pack(pady=5)

root.mainloop()

