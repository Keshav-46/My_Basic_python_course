from tkinter import*
from PIL import ImageTk, Image
root = Tk()
root.geometry('400x400')

HORIZONTAL= Scale(root,from_=0,to=200,orient=HORIZONTAL)
HORIZONTAL.pack()

VERTICAL= Scale(root,from_=0,to=200,orient=VERTICAL)
VERTICAL.pack()
my_label=Label(root,text=HORIZONTAL.get()).pack()

def slide():
    my_label = Label(root,text=HORIZONTAL.get()).pack() 

my_but=Button(root,text="click me!",command=slide).pack()
def slide():
    my_label = Label(root,text=VERTICAL.get()).pack() 

my_but=Button(root,text="click me!",command=slide).pack()
root.mainloop()