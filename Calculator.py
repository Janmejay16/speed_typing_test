from tkinter import *

root=Tk()
root.title("KDS CALCULATOR")

e=Entry(root,width=40,borderwidth=2)
e.grid(row=0,column=0,columnspan=3,pady=10,padx=10)

def button_add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_addition1():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def button_equals():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))


button1=Button(root,text="1",padx=40,pady=20,command=lambda: button_add(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: button_add(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: button_add(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda: button_add(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: button_add(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda: button_add(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda: button_add(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: button_add(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: button_add(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda: button_add(0))
button_addition=Button(root,text="+",padx=40,pady=20,command=button_addition1)
button_equal=Button(root,text="=",padx=40,pady=20,command=button_equals)
button_clear=Button(root,text="Clear",padx=125,pady=20,command=button_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
button_addition.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_clear.grid(row=5,column=0,columnspan=3)

root.mainloop()