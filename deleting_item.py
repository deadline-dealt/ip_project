import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import mysql.connector
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost ",user="root",password="varunvenkatesh2",database="Hotel")
if mycon.is_connected()==True:
    print("Connected Success!!")
    
root=tk.Tk()
root.geometry("1199x600+100+50")
photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root=Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)

def cancel():
    root.destroy()
def ok():
    mycursor = mycon.cursor()
    print("started to Delete Item")
    query = "Delete from Menu where itemname="+str("'"+input_ItemName.get()+"'")
    print(query)
    mycursor.execute(query)
    messagebox.showinfo("success", "Item Deleted Successfully")
    mycon.commit()
    mycon.close()
    root.destroy()

Delete_item = Frame(root)
Delete_item.place(x=150, y=150, height=340, width=500)
title = Label(Delete_item, text="Delete Item",font=("",20,"bold")).place(x=90,y=30)

ItemName = Label(Delete_item, text="Item Name:",font=("",20,"bold")).place(x=90, y=110)
input_ItemName = Entry(Delete_item)
input_ItemName.place(x=150, y=159, width=300, height=35)

ok_btn=tk.Button(root,text='OK',command=ok)
ok_btn.place(x=290,y=400, width=100, height=35)

can_btn=tk.Button(root,text='CANCEL',command=cancel)
can_btn.place(x=450,y=400, width=100, height=35)

root.mainloop()