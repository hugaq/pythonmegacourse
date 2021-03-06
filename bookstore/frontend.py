"""
A program that stores book information:
Title, Author, Year, ISBN

User can:
    View all records (Scrollbar)
    Search an entry
    Add an entry
    Update an entry
    Delete an entry

    Close the application
"""
# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from backend import *
import tkfactor as tkfac


class Lists(tk.Listbox):
    def __init__(self, parent, row, column, **kwargs):
        list_properties = {}
        grid_properties = {}
        for key, value in kwargs.items():
            if key in ('height', 'width'):
                list_properties[key] = value
            elif key in ('rowspan', 'columnspan'):
                grid_properties[key] = value
            else:
                pass
        tk.Listbox.__init__(self, master=parent, **list_properties)
        self.grid(row=row, column=column, **grid_properties)

    def view_command(self, lst):
        self.delete(0, tk.END)
        for row in lst:
            self.insert(tk.END, row)

    def get_selected_row(self):
        index = self.curselection()[0]
        return str(self.get(index)[0])


class Entries(tk.Entry):
    def __init__(self, parent, row, column):
        self.text_variable = tk.StringVar()
        tk.Entry.__init__(self, master=parent, textvariable=self.text_variable)
        self.grid(row=row, column=column)

    def out(self):
        return self.text_variable.get()

class Scrollbars(tk.Scrollbar):
    def __init__(self, parent, row, column, **kwargs):
        tk.Scrollbar.__init__(self, master=parent)
        self.grid(row=row, column=column, **kwargs)

class Buttons(tk.Button):
    def __init__(self, parent, row, column, text, width, command=None, **kwargs):
        tk.Button.__init__(self, master=parent, text=text, width=width, command=command)
        self.grid(row=row, column=column)

class MainApplication():
    def __init__(self, parent, *args, **kwargs):
        tkfac.createLabel(parent=parent, row=0, column=0, Text='Title')
        e1 = Entries(parent=parent, row=0, column=1)
        tkfac.createLabel(parent=parent, row=0, column=2, Text='Author')
        e2 = Entries(parent=parent, row=0, column=3)
        tkfac.createLabel(parent=parent, row=1, column=0, Text='Year')
        e3 = Entries(parent=parent, row=1, column=1)
        tkfac.createLabel(parent=parent, row=1, column=2, Text='ISBN')
        e4 = Entries(parent=parent, row=1, column=3)

        l1 = Lists(parent=parent, row=2, column=0, height=10, width=35, rowspan=6, columnspan=2)

        sb1 = Scrollbars(parent=parent, row=2, column=2, rowspan=6)

        l1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=l1.yview)

        self.state = ""

        b1 = Buttons(parent=parent, row=2, column=3, text='View all', width=12, command=lambda: self.view_command(l1, b1))
        b2 = Buttons(parent=parent, row=3, column=3, text='Search entry', width=12, command=lambda: self.search_command(l1, e1, e2, e3, e4, b2))
        b3 = Buttons(parent=parent, row=4, column=3, text='Add entry', width=12, command=lambda: self.insert_command(l1, e1, e2, e3, e4, b3))
        b4 = Buttons(parent=parent, row=5, column=3, text='Update', width=12, command=lambda: self.update_command(l1, e1, e2, e3, e4, b4))
        b5 = Buttons(parent=parent, row=6, column=3, text='Delete', width=12, command=lambda: self.delete_command(l1, b5))
        b6 = Buttons(parent=parent, row=7, column=3, text='Close', width=12, command=parent.destroy)

    def look(button):
        if self.state == button:
            return False
        else:
            self.state = button
            return True

    def view_command(self, l1, button):
        if look(button):
            l1.view_command(db.view())

    def search_command(self, l1, e1, e2, e3, e4, button):
        if look(button):
            result = db.search(title=e1.out(), author=e2.out(), year=e3.out(), isbn=e4.out())
            l1.view_command(result)

    def insert_command(self, l1, e1, e2, e3, e4, button):
        if look(button):
            db.insert(title=e1.out(), author=e2.out(), year=e3.out(), isbn=e4.out())
            l1.view_command(['insert successful'])

    def delete_command(self, l1, button):
        if look(button):
            db.delete(l1.get_selected_row(), button)
            l1.view_command(['entry successfully deleted'])

    def update_command(self, l1, e1, e2, e3, e4, button):
        if look(button):
            db.update(id=l1.get_selected_row(), title=e1.out(), author=e2.out(), year=e3.out(), isbn=e4.out())
            l1.view_command(['entry updated'])

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Book Store")
    MainApplication(root)#.pack(side="top", fill="both", expand=True)

    root.mainloop()
