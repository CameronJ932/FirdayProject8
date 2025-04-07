import sqlite3
import tkinter as tk
from tkinter import messagebox

# -------------------- DATABASE SETUP --------------------
conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

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

# -------------------- GUI SETUP --------------------
def window():
    window = tk.Tk()
    window.title("Customer Info System")
    window.geometry("500x500")
    window.configure(bg="#f0f4f8")

    font_style = ("Segoe UI", 10)
    label_color = "#333"
    highlight_color = "#007acc"

    # Title Label
    title_label = tk.Label(window, text="Enter Customer Information", font=("Segoe UI", 14, "bold"), fg=highlight_color, bg="#f0f4f8")
    title_label.pack(pady=10)

    # Form Frame
    form_frame = tk.Frame(window, bg="#f0f4f8")
    form_frame.pack(pady=10)

    # Entry Fields
    tk.Label(form_frame, text="Name", font=font_style, fg=label_color, bg="#f0f4f8").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    name_entry = tk.Entry(form_frame, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Birthday (YYYY-MM-DD)", font=font_style, fg=label_color, bg="#f0f4f8").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    birthday_entry = tk.Entry(form_frame, width=30)
    birthday_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Email", font=font_style, fg=label_color, bg="#f0f4f8").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    email_entry = tk.Entry(form_frame, width=30)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Phone", font=font_style, fg=label_color, bg="#f0f4f8").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    phone_entry = tk.Entry(form_frame, width=30)
    phone_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Address", font=font_style, fg=label_color, bg="#f0f4f8").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    address_entry = tk.Entry(form_frame, width=30)
    address_entry.grid(row=4, column=1, padx=10, pady=5)

    # Contact Method Dropdown
    tk.Label(form_frame, text="Preferred Contact Method", font=font_style, fg=label_color, bg="#f0f4f8").grid(row=5, column=0, sticky="e", padx=10, pady=5)
    contact_method_var = tk.StringVar(value="Email")
    contact_dropdown = tk.OptionMenu(form_frame, contact_method_var, "Email", "Phone", "Mail")
    contact_dropdown.config(width=28)
    contact_dropdown.grid(row=5, column=1, padx=10, pady=5)

    # Submit Function
    def submit_data():
        name = name_entry.get()
        birthday = birthday_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        contact_method = contact_method_var.get()

        # Name required
        if not name:
            messagebox.showerror("Input Error", "Name is required.")
            return

        # Email validation
        if email and ("@" not in email or "." not in email):
            messagebox.showerror("Input Error", "Invalid email format.")
            return

        # Birthday validation
        if birthday:
            parts = birthday.split("-")
            if len(parts) != 3 or not all(part.isdigit() for part in parts):
                messagebox.showerror("Input Error", "Birthday must be in YYYY-MM-DD format.")
                return
            year, month, day = parts
            if len(year) != 4 or len(month) != 2 or len(day) != 2:
                messagebox.showerror("Input Error", "Birthday must be in YYYY-MM-DD format.")
                return

        # Save to database
        cursor.execute('''
            INSERT INTO customers (name, birthday, email, phone, address, contact_method)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, birthday, email, phone, address, contact_method))
        conn.commit()

        messagebox.showinfo("Success", "Customer information saved!")

        # Clear form
        name_entry.delete(0, tk.END)
        birthday_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        contact_method_var.set("Email")

    # Submit Button
    submit_btn = tk.Button(window, text="Submit", command=submit_data, bg=highlight_color, fg="white", font=font_style)
    submit_btn.pack(pady=20)

    window.mainloop()

# -------------------- RUN --------------------
window()
conn.close()
