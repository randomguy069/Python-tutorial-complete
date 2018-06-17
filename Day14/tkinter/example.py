from tkinter import *

window = Tk()

def convert_to_everything():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0",END)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    t3.delete("1.0",END)
    t3.insert(END,ounces)

l1 = Label(window,text="kg")
l1.grid(row=0,column=1)
e1_value = StringVar()
e1= Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

b1= Button(window,text="Convert",command=convert_to_everything)
b1.grid(row=0,column=3)

t1= Text(window,height=1,width=10)
t1.grid(row=1,column=1)

t2= Text(window,height=1,width=10)
t2.grid(row=1,column=2)

t3= Text(window,height=1,width=10)
t3.grid(row=1,column=3)

window.mainloop()
