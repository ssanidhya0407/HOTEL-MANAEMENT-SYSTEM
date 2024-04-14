from tkinter import *
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
import sqlite3
import create_db
import math
import smtplib, ssl
import tkinter as tk
import time
import math
import sys


login1 = Tk()
login1.geometry('1600x900+0+0')
login1.title('Login System')
login1.config(bg='lightyellow')
login1.state('zoomed')




global sandy
sandy=StringVar()
# initialising the login variables
var_username = StringVar()
var_password = StringVar()

# Title
logo_title20 = PhotoImage(file='images/Extras/login.png')
title = Label(login1, text=' Login System', image=logo_title20, compound=LEFT,
              font=('courier', 40, 'bold'), bg='orange', fg='white', anchor='c').place(x=0, y=0, relwidth=1,
                                                                                        height=200)


frame2 = Frame(login1, bd=3, relief=RIDGE, bg='lightgreen')
frame2.place(x=720, y=240, width=600, height=550)

canvas = Canvas(login1, width=300, height=400, bg="black")
canvas.place(x=340,y=240,width=360,height=550)

# create background
bg = PhotoImage(file='images/Extras/imagelogin1.png')
canvas.create_image(174, 240, image=bg)


username = LabelFrame(frame2, bd=2, relief=RIDGE, bg="lightgreen", text='Username',
                      font=('courier', 34, 'bold'), fg='black')
username.place(x=10, y=30, width=500, height=130)

usernameEntry = Entry(username, bg="skyblue", textvariable=var_username, font=('courier', 34, 'bold'),
                      fg='black')
usernameEntry.place(x=10, y=4, width=450, height=50)

password = LabelFrame(frame2, bd=2, relief=RIDGE, bg="lightgreen", text='Password',
                      font=('courier', 34, 'bold'), fg='black')
password.place(x=10, y=170, width=500, height=120)

pwdEntry = Entry(password, bg="skyblue", textvariable=var_password, font=('courier', 34, 'bold'), fg='black')
pwdEntry.place(x=10, y=4, width=450, height=50)


def login2():
    global sandy
    con = sqlite3.connect(database=r'rms.db')
    cur = con.cursor()

    def login3():
        login1.destroy()

    try:

        if var_username.get() == "" and var_password.get() == "":
            messagebox.showerror("SQL Database", "Please Enter Login Details", parent=login1)

        elif var_username.get() != "":
            cur.execute('select * from employee where email=?', (var_username.get(),))
            rows = cur.fetchone()

            if rows == None:
                messagebox.showerror("SQL Database", "Invalid Email ID", parent=login1)

            elif rows != None and var_password.get() == "":
                messagebox.showerror("SQL Database", "Please Enter Password", parent=login1)

            elif rows != None and var_password.get() != "":
                cur.execute('select name from employee where pswd=?', (var_password.get(),))
                rows = cur.fetchone()
                sandy=rows


                if rows == None:
                    messagebox.showerror("SQL Database", "Invalid Password", parent=login1)

                elif rows != None:
                    messagebox.showinfo("SQL Database", "Login Successful", parent=login1)
                    login3()

        elif var_username.get() == "":
            messagebox.showerror("SQL Database", "Please Enter Username", parent=login1)

    except Exception as ex:
        messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=login1)


login1Btn = Button(frame2, bd=2, relief=RIDGE, bg="green", text='Login', font=('courier', 30, 'bold'),
                   fg='orange', command=login2)
login1Btn.place(x=140, y=330, width=260, height=80)


def forgotpwd():
    import forgotpswd


forgotpwd = Button(frame2, bd=2, relief=RIDGE, bg="orange", text='Forgot Password',
                   font=('courier', 20, 'bold'), fg='black', command=forgotpwd)
forgotpwd.place(x=120, y=420, width=300, height=70)

login1.mainloop()