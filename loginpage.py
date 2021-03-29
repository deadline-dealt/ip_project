import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

root=tk.Tk()
root.geometry("1199x600+100+50")

photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root=Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)

def admin():
    import admin_login
    
def customer():
    import customer_menu
    
    
admn_btn=tk.Button(root,text='ADMIN',command=admin,font=("",20,"bold"))
admn_btn.place(x=150,y=250, width=120, height=60)

cus_btn=tk.Button(root,text='CUSTOMER',command=customer,font=("",20,"bold"))
cus_btn.place(x=150,y=350, width=180, height=60)

root.mainloop()