from tkinter import*
import sqlite3
root =Tk()
root.title('its me keshav')
conn=sqlite3.connect('address_book.db')


c=conn.cursor()
c.execute("""CREATE TABLE addresses(
    fname text,
    lname text,
    address text,
    state text)      
""")
conn.commit()
conn.close()
root.mainloop()