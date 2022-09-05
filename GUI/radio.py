from tkinter import*
# from PIL import ImageTk,Image
root= Tk()
root.title('this is my journey')
# r=IntVar()
# r.set("2")
def clicked(value):
    mylabel =Label(root,text= pizza.get())
    mylabel .pack()
MODES=[
    ("it","it"),
    ("this","this"),
    ("what","what") 
]
pizza=StringVar()
pizza.set("it")
for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack()
# Radiobutton(root,text="Option1",variable=r,value=1,command=lambda: clicked(r.get())).pack()
# Radiobutton(root,text="Option2",variable=r,value=2,command=lambda: clicked(r.get())).pack()

mylabel =Label(root,text= pizza.get())
mylabel .pack()
myButton  =Button(root,text="clicked me!",command=lambda:clicked(pizza.get()))
myButton.pack()
root.mainloop()