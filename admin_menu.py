import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

root=tk.Tk()
root.title("ADMIN MENU")
root.geometry("1000x500+200+100")

photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root=Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)

def add_item():
    import adding_item

def delete_item():
    import deleting_item

def update_item():
    import updating_item


add_btn=tk.Button(root,text='Add Item',bg = "brown3",command=add_item,font=("",18,"bold"))
add_btn.place(x=50,y=200, width=180, height=60)

del_btn=tk.Button(root,text='Delete Item',bg = "brown3",command=delete_item,font=("",18,"bold"))
del_btn.place(x=50,y=275, width=180, height=60)

upd_btn=tk.Button(root,text='Update Item',bg = "brown3",command=update_item,font=("",18,"bold"))
upd_btn.place(x=50,y=350, width=180, height=60)

root.mainloop()