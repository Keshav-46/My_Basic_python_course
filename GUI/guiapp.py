from tkinter import*
import sqlite3
root=Tk()
root.title('this is my gui app')
root.geometry("400x400")
#text box
def update():
   conn=sqlite3.connect('address_book.db')
   c=conn.cursor()
   c.execute("""UPDATE addresses
   set fname = 'Alfred Schmidt', lname= 'Frankfurt',address='ghante',state='bagmati'
   WHERE oid= """+ update.get())
   conn.commit()
   conn.close()
def Delete():
   conn=sqlite3.connect('address_book.db')
   c=conn.cursor()
   c.execute("DELETE FROM addresses where oid=" + update.get())
   conn.commit()
   conn.close()

def query():
   conn= sqlite3.connect('address_book.db')
   c=conn.cursor()
  #query the databases
   c.execute("SELECT * ,oid FROM addresses")
   records=c.fetchall()
   print(records)

   conn.commit()
   conn.close()
   
   print_records=''
   for record in records:
      print_records += str(record[0])+" "+str(record[1]+" "+str(record[2])+" "+str(record[3]))+ "\n"

   query_label=Label(root,text=print_records)
   query_label.grid(row=13,column=0,columnspan=2)
def submit():
   conn= sqlite3.connect('address_book.db')
   c=conn.cursor()
   c.execute("INSERT INTO addresses VALUES(:fname,:lname,:address,:state)",
   {
      
      'fname':fname.get(),
      'lname':lname.get(),
      'address':address.get(),
      'state':state.get()
   })
   conn.commit()
   conn.close()
fname= Entry(root,width=40)
fname.grid(row=0,column=1,padx=40)

lname= Entry(root,width=40)
lname.grid(row=1,column=1,padx=40)

address= Entry(root,width=40)
address.grid(row=2,column=1,padx=40)

state= Entry(root,width=40)
state.grid(row=3,column=1,padx=40)

update= Entry(root,width=40)
update.grid(row=9,column=1,padx=40)

fname_label=Label(root,text='First Name')
fname_label.grid(row=0,column=0,padx=10)

lname_label=Label(root,text='Last name')
lname_label.grid(row=1,column=0,padx=10)

address_label=Label(root,text='Address')
address_label.grid(row=2,column=0,padx=10)

State_label=Label(root,text='State')
State_label.grid(row=3,column=0,padx=10)

State_label=Label(root,text='select ID')
State_label.grid(row=9,column=0,padx=10)

mybutton=Button(root,text="add to database",command=submit)
mybutton.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

query_but=Button(root,text="show record",command=query)
query_but.grid(row=7,column=0,columnspan=100)

delete_but=Button(root,text="Delete all",command=Delete)
delete_but.grid(row=11,column=0,columnspan=146,padx=10,pady=10,ipadx=148)

#create a update button
update_but=Button(root,text="update datas",command=update)
update_but.grid(row=12,column=0,columnspan=100,padx=10,pady=10,ipadx=145)

root.mainloop()