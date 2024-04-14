from tkinter import *

import cur as cur
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
from random import randint
import sqlite3
import create_db
import smtplib, ssl




forgotpswd = Toplevel()
forgotpswd.geometry('500x450+725+280')
forgotpswd.title('Forget Password')
forgotpswd.config(bg='lightyellow')
forgotpswd.focus_force()

var_checkEmpNo = StringVar()
var_otp = StringVar()
var_newPassword = StringVar()

logo_title1 = PhotoImage(file='images/Extras/forgotpswd.png')
title = Label(forgotpswd, text='Forgot Password', image=logo_title1, compound=LEFT,
              font=('courier', 20, 'bold'), bg='orange', fg='white', anchor='c').place(x=0, y=0, relwidth=1,
                                                                                        height=140)

forgotpswdLbl=LabelFrame(forgotpswd, text="Enter Employee Number", font=('courier', 20,'bold'), fg='red', bg='lightyellow', bd=3, relief=RIDGE)
forgotpswdLbl.place(x=10, y=148, width=450, height=80)

forgotpswdEntry=Entry(forgotpswdLbl, textvar=var_checkEmpNo, font=('courier', 20,'bold'), fg='red', bg='lightgreen', bd=3, relief=RIDGE)
forgotpswdEntry.place(x=5, y=0, width=420, height=40)

#generateOTP
generateOTP=randint(1000, 3000)
strgenerateOTP=str(generateOTP)

def sendEmail():
    def read_creds():
        user = password = ""
        with open("credentials.txt", "r") as f:
            file = f.readlines()
            user = file[0].strip()
            password = file[1].strip()

        return user, password

    port = 465

    sender, password = read_creds()

    con = sqlite3.connect(database=r'rms.db')
    cur = con.cursor()
    cur.execute('Select email from employee where empID=?', (var_checkEmpNo.get(),))
    con.commit()
    row = cur.fetchone()
    if row != None:
        recieve = row
    elif row == None:
        messagebox.showerror("SQL Database", "The entered Employee ID does not exist.", parent=forgotpswd)

    message = """\
    OTP For Regaining Access\n
Your OTP is """ + strgenerateOTP

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    print('Email Sent')
    messagebox.showinfo("SQL Database","An email with the OTP has been\nsent to your Registered Email Address", parent=forgotpswd)


Send=Button(forgotpswd, text="Send OTP", font=('times new roman', 15,'bold'), fg='red', bg='orange', bd=3, relief=RIDGE, command=sendEmail)
Send.place(x=10, y=250, width=120, height=65)

otpLbl=LabelFrame(forgotpswd, text="Enter OTP", font=('courier', 15,'bold'), fg='red', bg='lightyellow', bd=3, relief=RIDGE)
otpLbl.place(x=240, y=240, width=160, height=75)


otpEntry=Entry(otpLbl, textvar=var_otp, font=('courier', 20,'bold'), fg='red', bg='lightgreen', bd=3, relief=RIDGE)
otpEntry.place(x=5, y=0, width=140, height=40)


newPSWDLbl=LabelFrame(forgotpswd, text="Enter New Password", font=('courier', 20,'bold'), fg='red', bg='lightyellow', bd=3, relief=RIDGE)
newPSWDLbl.place(x=10, y=350, width=450, height=80)

newpswdEntry=Entry(newPSWDLbl, textvar=var_newPassword, font=('courier', 20,'bold'), fg='red', bg='lightgreen', bd=3, relief=RIDGE, state='disabled')
newpswdEntry.place(x=0, y=0, width=380, height=40)


def otpBtnfunc():
    if var_otp.get()==strgenerateOTP:
        messagebox.showinfo("Forgot Password", "OTP Validated \nYou May Proceed To Enter Your New Password", parent=forgotpswd)
        newpswdEntry.config(state='normal')
    if var_otp.get()!= strgenerateOTP:
        messagebox.showerror("Forgot Password", "You Have Entered Incorrect OTP\n Please Retry", parent=forgotpswd)
        newpswdEntry.config(state='disabled')


otpPhoto=PhotoImage(file='images/Extras/tick.png')
otpBtn=Button(forgotpswd, image=otpPhoto, font=('courier', 15,'bold'), fg='red', bg='lightyellow', bd=3, relief=RIDGE, command=otpBtnfunc)
otpBtn.place(x=410, y=260, width=50, height=50)

def newPswdset():
    con = sqlite3.connect(database=r'rms.db')
    cur = con.cursor()
    try:
        cur.execute('Select pswd from employee where empID=?', (var_checkEmpNo.get(),))
        con.commit()
        row = cur.fetchone()
        rowtuplesplit = row[0]
        if var_newPassword.get() == rowtuplesplit:
            messagebox.showerror("SQL Database", "Please enter a new password", parent=forgotpswd)
        elif var_newPassword.get() != rowtuplesplit:
            cur.execute('update employee set pswd=? where empID=?', (var_newPassword.get(), var_checkEmpNo.get()))
            con.commit()

            messagebox.showinfo('SQL Database', 'New Password Set Successfully', parent=forgotpswd)
            forgotpswd.destroy()

    except Exception as ex:
        messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=forgotpswd)

newpswdBtn=Button(newPSWDLbl, text='Set', font=('courier', 20,'bold'), fg='red', bg='lightgreen', bd=3, relief=RIDGE, command=newPswdset)
newpswdBtn.place(x=380, y=0, width=60, height=40)

