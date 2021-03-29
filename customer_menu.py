from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk,Image

root=tk.Tk()
root.geometry("1199x600+100+50")

photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root=Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)



def gen_id():
    x=random.randint(1,1000)
    msg="Your Customer ID is "+str(x)
    messagebox.showinfo("ID", msg)
    
def view_menu():
   print("viewing menu")
   import view_menu
def pla_ord():
   print("Order placed")
   import placeorder

def bill_gen():
   import billgeneration

cus_id=tk.Button(root,text='Generate CustomerID',command=gen_id,font=("",18,"bold"))
cus_id.place(x=50,y=250, width=300, height=60)

view_menu=tk.Button(root,text='View menu',command=view_menu,font=("",18,"bold"))
view_menu.place(x=50,y=320, width=190, height=60)

pla_ord=tk.Button(root,text='Place Order',command=pla_ord,font=("",18,"bold"))
pla_ord.place(x=50,y=390, width=180, height=60)

bill_gen=tk.Button(root,text='Bill',command=bill_gen,font=("",18,"bold"))
bill_gen.place(x=50,y=460, width=180, height=60)

root.mainloop()