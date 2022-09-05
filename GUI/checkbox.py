from tkinter import*
from PIL import ImageTk,Image
root = Tk()
root.geometry('400x400')
var= StringVar()
c= Checkbutton(root,text="ckeck thix box",variable=var,offvalue="off",onvalue="on")
c.pack()
def show():
    mylabel=Label(root,text=var.get()).pack()

mybutton=Button(root,text="here me",command=show).pack()
root.mainloop()