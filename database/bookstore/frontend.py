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

class Labels():
    def __init__(self, parent, row, column, Text):
        self = tk.Label(master=parent, text=Text)
        self.grid(row=row, column=column)

class Entries():
    def __init__(self, parent, row, column):#, Text):
        self.text_variable = tk.StringVar()
        #self.text_variable = Text
        self = tk.Entry(master=parent, textvariable=self.text_variable)
        self.grid(row=row, column=column)

class MainApplication():
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        Labels(parent=parent, row=0, column=0, Text='Title')
        e1 = Entries(parent=parent, row=0, column=1)#, Text='placeholder')
        Labels(parent=parent, row=0, column=2, Text='Author')
        e2 = Entries(parent=parent, row=0, column=3)
        Labels(parent=parent, row=1, column=0, Text='Year')
        e3 = Entries(parent=parent, row=1, column=1)
        Labels(parent=parent, row=1, column=2, Text='ISBN')
        e4 = Entries(parent=parent, row=1, column=3)
        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)#.pack(side="top", fill="both", expand=True)

    root.mainloop()
