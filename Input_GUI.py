from tkinter import *


root = Tk()

e = Entry(root,width=50)
e.pack()
e.insert(1,"Enter Your Name:")

def myclick():
    mylabel = Label( root,text="Hello "+e.get())
    mylabel.pack()

mylabel1 = Label(root, text="Kahan Sheth")
mybutton=Button(root,text="Enter your name", padx=50,pady=50,command=myclick,fg="red",bg="cyan")

mybutton.pack()

root.mainloop()