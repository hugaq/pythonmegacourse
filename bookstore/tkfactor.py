import tkinter as tk


def createLabel(parent, Text, row, column):
    asd = tk.Label(master=parent, text=Text)
    asd.grid(row=row, column=column)
