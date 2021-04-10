from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.iconbitmap('D:/Blurred.jpg')

button_quit=Button(root,text="EXIT",command=root.quit)
button_quit.pack()

img=ImageTk.PhotoImage(Image.open('D:/Blurred.jpg'))
label=Label(image=img)
label.pack()

root.mainloop()

