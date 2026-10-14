import tkinter as tk



def switch_navigation_window(event):
    listbox = event.widget
    selection = listbox.curselection()
    name = listbox.get(selection)
    print(name)

def show_navigation(window):
    nav_item = ['Uplate', 'Korisnici', 'Dodavanje uplata']

    navigation = tk.Listbox(window)
    navigation.pack(side='left', fill='y', padx='5')

    for item in nav_item:
        navigation.insert(tk.END, item)



    return navigation