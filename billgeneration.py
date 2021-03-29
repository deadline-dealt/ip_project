import tkinter as tk
from tkinter import *
from tkinter import messagebox 
import random
import mysql.connector
import mysql.connector as sqltor
from PIL import ImageTk,Image




mycon=sqltor.connect(host="localhost ",user="root",password="varunvenkatesh2",database="Hotel")
if mycon.is_connected()==True:
    print("Connected Success!!")

def ok():
    mycursor = mycon.cursor()
    print("Bill is Generating")

    query = "select m.itemname,Quantity,Price,price*quantity 'Total' from Menu m join PlaceOrder p on m.itemname=p.itemname where cust_id="+str(input_cus_ID.get())
    print(query)
    mycursor.execute(query)
    result_set=mycursor.fetchall()
    print(result_set)
    messagebox.showinfo("success", result_set)

    query1 = "select cust_id,sum(total) 'TotalAmount' from (select cust_id,m.itemname,Quantity,Price,price*quantity 'Total' from menu m join placeorder p on m.itemname=p.itemname where cust_id="+str(input_cus_ID.get())+")as t;"
    print(query1)
    mycursor.execute(query1)
    result_set1=mycursor.fetchall()
    for i in result_set1:
        x=i[1]
    res="Your Bill Amount is "+ str(x)   
    messagebox.showinfo("success", res)
    mycon.commit()
    mycon.close()
    root.destroy()

root=tk.Tk()
root.geometry("1199x600+100+50")
photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root=Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)

cus_ID = Frame(root)
cus_ID.place(x=150, y=150, height=340, width=500)
title = Label(cus_ID, text="Enter Your Customer ID").place(x=90,y=30)

input_cus_ID = Entry(cus_ID)
input_cus_ID.place(x=90, y=140, width=300, height=35)

ok_btn=tk.Button(root,text='OK',command=ok)
ok_btn.place(x=250,y=450, width=100, height=35)

root.mainloop()