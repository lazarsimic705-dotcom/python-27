import tkinter as tk
from src.core.database import connect_to_db


def show_payments_window(window):

    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM payments")

    Listbox = tk.Listbox(window)
    Listbox.pack(side='left')

    for payment in cursor.fetchall():
        id, user_id, amount, created_at = payment
        Listbox.insert(tk.END, f"{id}, {user_id}, {amount}, {created_at}")