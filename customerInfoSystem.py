import sqlite3
import tkinter as tk

conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

#Chat GPT creatred 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers(
    name TEXT NOT NULL,
    birthday TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    contect_method TEXT,
    )
''')
conn.commit()

def window():
    window = tk.Tk()
    window.title("Info System")
    window.geometry("500x500")

    window.mainloop()


window()