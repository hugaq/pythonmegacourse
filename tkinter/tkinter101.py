from tkinter import *


def km_to_miles():
    calc = float(e1_value.get())*1.6
    mi = ''.join(['{:.2f}'.format(calc),'\n'])
    t1.insert(END, mi)

window = Tk()

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=10, width=20)
t1.grid(row=0, column=2)

window.mainloop()
#das sieht aber hässlich aus
