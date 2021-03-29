import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=tk.Tk()
root.title("Admin Login")
root.geometry("1000x500+200+100")
#==========background_img==================
photo = ImageTk.PhotoImage(Image.open("/home/varun/varun-files/ip project001/images/loginp.jpg"))
root=Label(image=photo)
root.place(x=0,y=0,relwidth=1,relheight=1)
#===========username===============
username=Label(text="username",font=("times new roman",18,"bold","italic"))
username.place(x=75,y=208)
username_input=Entry(font=("times new roman",18))
username_input.place(x=240,y=208)
#===========Password============
Password=Label(text="Password",font=("times new roman",18,"bold","italic"))
Password.place(x=75,y=260)
passwrd_input=Entry(show="*",font=("times new roman",18))
passwrd_input.place(x=240,y=260)


#==========Login-work==============
def Login():
    if (username_input.get()=="nithish" and passwrd_input.get()=="nithish"):
        messagebox.showinfo("","sucessfully logined")
        messagebox.showinfo("good day","welcome back Nithish") 
        import admin_menu.py

    elif  (username_input.get()=="varun" and passwrd_input.get()=="varun"):
        messagebox.showinfo("","sucessfully logined")
        messagebox.showinfo("good day","welcome back Varun") 
        import admin_menu.py

    elif (username_input.get()=="harshavardhan" and passwrd_input.get()=="harshavardhan"):
        messagebox.showinfo("","sucessfully logined")  
        messagebox.showinfo("good day","welcome back Harshavardhan")  
        import admin_menu.py

    else:
        messagebox.showinfo("error","Incorrect username/password")

#========login_button==========0
Login_bt=Button(text="Login",command= Login ,bg="white",fg="red",font=("",13,"bold"))
Login_bt.place(x=260,y=320)

root.mainloop()  