from tkinter import*
root =Tk()
root.title('its me keshav')
root.geometry("400x400")
click= StringVar()

drop= OptionMenu(root,click, "sun","mon","tue")
drop.pack()


root.mainloop()