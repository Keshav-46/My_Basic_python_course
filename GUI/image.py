from tkinter import*
from PIL import ImageTk,Image
root= Tk()
root.title('this is my journey')

myimage=ImageTk.PhotoImage(Image.open("1.png"))
root.iconbitmap('E:\My_pyhton_programs\GUI\1.png')

my_label=Label(image=myimage)
my_label

# Button_quit=Button(root,text='exit program',command=root.quit)
# Button_quit.pack()

root.mainloop()