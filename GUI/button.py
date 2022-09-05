from tkinter import*
root= Tk()
root =Tk()
e=Entry(root,width=50,bg="blue",fg="white")
e.pack()
def myclick():
    mylabel1=Label(root,text="hello"+ e.get())
    mylabel1.pack()

Mybutton= Button(root,text="click me!",command=myclick,bg="#000000",fg="green")
Mybutton.pack()
root.mainloop()