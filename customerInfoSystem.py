import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

#Chat GPT creatred 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        contact_method TEXT
    );
''')

conn.commit()

def window():
    window = tk.Tk()
    window.title("Info System")
    window.geometry("500x500")

#Chat GPT written 
    fields = {
        'Name': None,
        'Birthday (YYYY-MM-DD)': None,
        'Email': None,
        'Phone': None,
        'Address': None
    }

    row = 0
    for label_text in fields:
        label = tk.Label(window, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")

        entry = tk.Entry(window, width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)

        fields[label_text] = entry
        row += 1

    # Dropdown menu for preferred contact method
    tk.Label(window, text="Preferred Contact Method").grid(row=row, column=0, padx=10, pady=5, sticky="e")
    contact_method_var = tk.StringVar(value="Email")
    contact_dropdown = tk.OptionMenu(window, contact_method_var, "Email", "Phone", "Mail")
    contact_dropdown.grid(row=row, column=1, padx=10, pady=5)
    row += 1

    # Submit button function
    def submit_data():
        name = fields['Name'].get()
        birthday = fields['Birthday (YYYY-MM-DD)'].get()
        email = fields['Email'].get()
        phone = fields['Phone'].get()
        address = fields['Address'].get()
        contact_method = contact_method_var.get()

        if not name:
            messagebox.showerror("Input Error", "Name is required.")
            return
        
        cursor.execute('''
            INSERT INTO customers (name, birthday, email, phone, address, contact_method)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, birthday, email, phone, address, contact_method))
        conn.commit()

        messagebox.showinfo("Success", "Customer information saved!")

        for entry in fields.values():
            entry.delete(0, tk.END)
        contact_method_var.set("Email")

    # Add the submit button
    submit_btn = tk.Button(window, text="Submit", command=submit_data)
    submit_btn.grid(row=row, column=0, columnspan=2, pady=20)

    window.mainloop()


window()

conn.close()