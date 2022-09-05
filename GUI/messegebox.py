from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("my traget is so dangerous")
def popup():
    messagebox.showwarning("This is my Popup","Hello world!")
Button(root,text="Pupup",command=popup).pack()

root.mainloop()