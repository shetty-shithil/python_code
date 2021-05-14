import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title('Simple Calculator')

e=tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_clicked(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0, END)
def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math=='addition':
     e.insert(0, f_num +int(second_number))
    elif math=='subtraction':
     e.insert(0, f_num -int(second_number))
    elif math=='multiplication':
     e.insert(0, f_num *int(second_number))
    elif math=='division':
     e.insert(0, f_num/int(second_number)) 
def button_add():
    first_number=e.get()
    global f_num
    global math 
    math ='addition'
    f_num=int(first_number)
    e.delete(0, END)
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math='subtraction'
    f_num=int(first_number)
    e.delete(0, END)
def button_mul():
    first_number=e.get()
    global f_num
    global math
    math='multiplication'
    f_num=int(first_number)
    e.delete(0, END)
def button_div():
    first_number=e.get()
    global f_num
    global math
    math='division'
    f_num=int(first_number)
    e.delete(0, END)
    
button_1=tk.Button(root, text='1', padx=40, pady=20, command=lambda:button_clicked(1))
button_2=tk.Button(root, text='2', padx=40, pady=20, command=lambda:button_clicked(2))
button_3=tk.Button(root, text='3', padx=40, pady=20, command=lambda:button_clicked(3))
button_4=tk.Button(root, text='4', padx=40, pady=20, command=lambda:button_clicked(4))
button_5=tk.Button(root, text='5', padx=40, pady=20, command=lambda:button_clicked(5))
button_6=tk.Button(root, text='6', padx=40, pady=20, command=lambda:button_clicked(6))
button_7=tk.Button(root, text='7', padx=40, pady=20, command=lambda:button_clicked(7))
button_8=tk.Button(root, text='8', padx=40, pady=20, command=lambda:button_clicked(8))
button_9=tk.Button(root, text='9', padx=40, pady=20, command=lambda:button_clicked(9))
button_0=tk.Button(root, text='0', padx=40, pady=20, command=lambda:button_clicked(0))
button_11=tk.Button(root, text='+', padx=40, pady=20, command=button_add)
button_12=tk.Button(root, text='=', padx=39, pady=20, command=button_equal)
button_13=tk.Button(root, text='Clear', padx=125, pady=20, command=button_clear)
button_14=tk.Button(root, text='-', padx=39, pady=20, command=button_sub)
button_15=tk.Button(root, text='*', padx=39, pady=20, command=button_mul)
button_16=tk.Button(root, text='/', padx=39, pady=20, command=button_div)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=1)

button_11.grid(row=4,column=0)
button_12.grid(row=4,column=2)
button_13.grid(row=5,column=0, columnspan=3)
button_14.grid(row=6,column=0)
button_15.grid(row=6,column=1)
button_16.grid(row=6,column=2)

root.mainloop()
