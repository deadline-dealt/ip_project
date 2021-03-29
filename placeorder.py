import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
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
    query = "insert into PlaceOrder values("+str(input_CutomerId.get())+","+str("'"+input_ItemName.get()+"'")+","+str(input_Qty.get())+")"
    print(query)
    mycursor.execute(query)
    messagebox.showinfo("success", "Order Placed!!!")
    mycon.commit()
    mycon.close()
    root.destroy()  
    
    
pla_order=Frame(root)
pla_order.place(x=150, y=150, height=340, width=500)
title = Label(pla_order,text="Place Your Order",font=("",20,"bold")).place(x=90,y=30)


CutomerId = Label(pla_order, text="Customer Id:",font=("",20,"bold")).place(x=90, y=70)
input_CutomerId = Entry(pla_order)
input_CutomerId.place(x=325, y=70, width=150, height=35)


ItemName = Label(pla_order, text="Item Name:",font=("",20,"bold")).place(x=90, y=150)
input_ItemName = Entry(pla_order)
input_ItemName.place(x=325, y=150, width=150, height=35)

Qty = Label(pla_order, text="Quantity:",font=("",20,"bold")).place(x=90, y=230)
input_Qty = Entry(pla_order)
input_Qty.place(x=325, y=230, width=150, height=35)

ok_btn=tk.Button(root,text='OK',command=ok)
ok_btn.place(x=250,y=450, width=100, height=35)

can_btn=tk.Button(root,text='CANCEL',command=cancel)
can_btn.place(x=450,y=450, width=100, height=35)

root.mainloop()
