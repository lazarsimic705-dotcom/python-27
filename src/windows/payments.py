import tkinter as tk



def show_payments_window(window):
    payments = ["Toma, 500, 25.10.2026", "Laki, 1000, 14.10.2026", "Joca, 200, 22.11.2016"]


    listbox = tk.Listbox(window)
    listbox.pack(side='left')

    for payment in payments:
        listbox.insert(tk.END, payment)