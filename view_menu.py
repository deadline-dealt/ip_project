from tkinter import messagebox
import random
import mysql.connector
import mysql.connector as sqltor

mycon=sqltor.connect(host="localhost ",user="root",password="varunvenkatesh2",database="Hotel")
if mycon.is_connected()==True:
    print("Connected Success!!")

mycursor = mycon.cursor()
query ="select Itemname,price from Menu"
print(query)
mycursor.execute(query)
result=mycursor.fetchall()
    
messagebox.showinfo("Menu", result)
mycon.commit()
mycon.close()