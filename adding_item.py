import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import random
import mysql.connector
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost ",user="root",password="varunvenkatesh2",database="Hotel")
if mycon.is_connected()==True:
    print("Connected Success!!")


root=tk.Tk()
root.geometry("1199x600+100+50")

photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root = Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)

def cancel():
    root.destroy()
def ok():
    mycursor = mycon.cursor()
    print("started to Add item")
    query = "insert into Menu values(" +str(random.randint(1,1000))+","+str("'"+input_ItemName.get()+"'")+","+str(input_Price.get())+")"
    print(query)
    mycursor.execute(query)
    messagebox.showinfo("success", "Item Added Successfully")
    mycon.commit()
    mycon.close()
    root.destroy()
    
Add_item = Frame(root)
Add_item.place(x=150, y=150, height=340, width=500)
title = Label(Add_item, text="Add New Item",font=("",20,"bold")).place(x=90,y=30)
ItemName = Label(Add_item, text="Item Name:",font=("",20,"bold")).place(x=90, y=110)

input_ItemName = Entry(Add_item)
input_ItemName.place(x=150, y=160, width=300, height=35)

Price = Label(Add_item, text="Price:",font=("",20,"bold")).place(x=90, y=200)
input_Price = Entry(Add_item)
input_Price.place(x=150, y=250, width=300, height=35)

ok_btn=tk.Button(root,text='OK',command=ok)
ok_btn.place(x=250,y=450, width=100, height=35)

can_btn=tk.Button(root,text='CANCEL',command=cancel)
can_btn.place(x=450,y=450, width=100, height=35)

root.mainloop()