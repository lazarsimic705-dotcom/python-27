import tkinter as tk
from src.windows.users import show_users_window
from src.windows.payments import show_payments_window



def switch_navigation_window(event, content):
    listbox = event.widget
    selection = listbox.curselection()
    name = listbox.get(selection)

    for child in content.winfo_children():
        child.destroy()


    if name.lower() == 'uplate':
        show_payments_window(content)
    else:
        show_users_window(content)



def show_navigation(window):
    nav_item = ['Uplate', 'Korisnici', 'Dodavanje uplata']

    navigation = tk.Listbox(window)
    navigation.pack(side='left', fill='y', padx='5')

    for item in nav_item:
        navigation.insert(tk.END, item)



    return navigation