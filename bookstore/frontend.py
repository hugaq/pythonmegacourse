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
import backend


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

    def config(self, **kwargs):
        self.configure(**kwargs)

class Labels(tk.Label):
    def __init__(self, parent, row, column, Text):
        tk.Label.__init__(self, master=parent, text=Text)
        self.grid(row=row, column=column)

class Entries(tk.Entry):
    def __init__(self, parent, row, column):
        self.text_variable = tk.StringVar()
        tk.Entry.__init__(self, master=parent, textvariable=self.text_variable)
        self.grid(row=row, column=column)

class Scrollbars(tk.Scrollbar):
    def __init__(self, parent, row, column, **kwargs):
        tk.Scrollbar.__init__(self, master=parent)
        self.grid(row=row, column=column, **kwargs)

    def config(self, **kwargs):
        self.configure(**kwargs)

class Buttons(tk.Button):
    def __init__(self, parent, row, column, text, width, command=None, **kwargs):
        tk.Button.__init__(self, master=parent, text=text, width=width, command=command)
        self.grid(row=row, column=column)

class MainApplication():
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        Labels(parent=parent, row=0, column=0, Text='Title')
        e1 = Entries(parent=parent, row=0, column=1)
        Labels(parent=parent, row=0, column=2, Text='Author')
        e2 = Entries(parent=parent, row=0, column=3)
        Labels(parent=parent, row=1, column=0, Text='Year')
        e3 = Entries(parent=parent, row=1, column=1)
        Labels(parent=parent, row=1, column=2, Text='ISBN')
        e4 = Entries(parent=parent, row=1, column=3)

        l1 = Lists(parent=parent, row=2, column=0, height=10, width=35, rowspan=6, columnspan=2)

        sb1 = Scrollbars(parent=parent, row=2, column=2, rowspan=6)

        l1.config(yscrollcommand=sb1.set)
        sb1.config(command=l1.yview)

        b1 = Buttons(parent=parent, row=2, column=3, text='View all', width=12)
        b2 = Buttons(parent=parent, row=3, column=3, text='Search entry', width=12)
        b3 = Buttons(parent=parent, row=4, column=3, text='Add entry', width=12)
        b4 = Buttons(parent=parent, row=5, column=3, text='Update', width=12)
        b5 = Buttons(parent=parent, row=6, column=3, text='Delete', width=12)
        b6 = Buttons(parent=parent, row=7, column=3, text='Close', width=12)
        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)#.pack(side="top", fill="both", expand=True)

    root.mainloop()