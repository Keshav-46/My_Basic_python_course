from tkinter import*
from PIL import ImageTk, Image
root = Tk()

top = Toplevel()
my_image=ImageTk.PhotoImage(Image.open("1.png"))
Lab1=Label(top,image=my_image).pack()
root.mainloop()