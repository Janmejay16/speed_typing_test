from tkinter import *

root = Tk()

def myclick():
    mylabel = Label( root,text="Hello World" )
    mylabel.pack()

mylabel1 = Label(root, text="Kahan Sheth")
mybutton=Button(root,text="Enter", padx=50,pady=50,command=myclick,fg="red",bg="cyan")

mybutton.pack()

root.mainloop()