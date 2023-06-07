#!/usr/bin/env python

__author__ = "Alex Mirnyy"

from tkinter import *
from math import sqrt

def solver(a,b,c):
    if a==0:
        x=-c/b
        text = "Линейное уравнение: x = %s \n" % x 
    D = b*b - 4*a*c
    if D >= 0 and a != 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант: %s \n X1 = %s \n X2 = %s \n" % (D, x1, x2)        
    elif a != 0:
        text = "Дискриминант: %s \n Нет корней" % D 
    return text

def inserter(value):
    output.delete("0.0","end")
    output.insert("0.0",value)    

def clear(event):
    caller = event.widget
    caller.delete("0", "end")

def handler():
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Введите 3 числа")

root = Tk()
root.title("Решение уравнений")
root.minsize(325,235)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a = Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="x^2+").grid(row=1,column=2)

b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1, column=4)

c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

but = Button(frame, text="РЕШИТЬ", command=handler).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="gray", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()
