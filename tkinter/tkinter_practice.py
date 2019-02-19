from tkinter import *


def convert():
    calc_gram = float(e1_value.get())*1000.0
    gram = ''.join(['{:.1f}'.format(calc_gram),'g'])
    t1.insert(END, gram)
    calc_pounds = float(e1_value.get())*2.20462
    pounds = ''.join(['{:.4f}'.format(calc_pounds),'lbs'])
    t2.insert(END, pounds)
    calc_ounces = float(e1_value.get())*35.27
    ounces = ''.join(['{:.2f}'.format(calc_ounces),'ounces'])
    t3.insert(END, ounces)

window = Tk()
window.geometry("320x100")

b1 = Button(window, text="convert", command=convert)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l1 = Label(window, text='kg')
l1.grid(row=0, column=0)

t1 = Text(window, height=3, width=10)
t1.grid(row=1, column=0)

t2 = Text(window, height=3, width=10)
t2.grid(row=1, column=1)

t3 = Text(window, height=3, width=10)
t3.grid(row=1, column=2)

window.mainloop()
