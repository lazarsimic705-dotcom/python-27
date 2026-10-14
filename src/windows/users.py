
import tkinter as tk


def show_users_window(window):

    users = ['Toma', 'Laki', 'Joca']

    user_list = tk.Listbox(window)
    user_list.pack(side='left', fill='both')

    for user in users:
        user_list.insert(tk.END, user)