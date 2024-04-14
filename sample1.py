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
import time
from login import sandy
from cefpython3 import cefpython as cef
import sys
import os
import random
import razorpay
import json
from selenium import webdriver
import getpass
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
from fpdf import FPDF
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import StringVar
import time

from flask import Flask, render_template, request


#After Login
root = Tk()
root.geometry('1600x900+0+0')
root.title('Restaurant Management System')
root.config(bg='gray')
root.state('zoomed')


# Initialising Variables
var_Promo = StringVar()
var_Receipt=StringVar()
##STARTERS

# SANDWICH
sandwichTotal = StringVar()
pizzaPrice = IntVar()
tandooriPrice = IntVar()
mexicanCount1Price = IntVar()
clubCountPrice = IntVar()
pizzaCount = IntVar()
tandooriCount = IntVar()
mexicanCount1 = IntVar()
clubCount = IntVar()
pizzaCount = tandooriCount = mexicanCount1 = clubCount = 0
pizzaPrice = tandooriPrice = mexicanCount1Price = clubCountPrice = 0

# FRANKIE
frankieTotal = StringVar()
schezwanpaneerPrice = IntVar()
mixvegPrice = IntVar()
chillipaneerCount1Price = IntVar()
cheeseCount1Price = IntVar()
cheeseCount1 = IntVar()
schezwanpaneerCount = IntVar()
mixvegCount = IntVar()
chillipaneerCount1 = IntVar()
cheeseCount1 = mixvegCount = chillipaneerCount1 = schezwanpaneerCount = 0
cheeseCount1Price = mixvegPrice = chillipaneerCount1Price = schezwanpaneerPrice = 0

# SUBWAY
subwayTotal = StringVar()
mexicanCount2Price = IntVar()
harabharaPrice = IntVar()
paneerFilletPrice = IntVar()
paneertikkaPrice = IntVar()
paneertikkaCount = IntVar()
paneerFilletCount = IntVar()
harabharaCount = IntVar()
mexicanCount2 = IntVar()
mexicanCount2 = harabharaCount = paneertikkaCount = paneerFilletCount = 0
mexicanCount2Price = harabharaPrice = paneertikkaPrice = paneerFilletPrice = 0

# BURGER
burgerTotal = StringVar()
cheeseCount2Price = IntVar()
cheeseCount2 = IntVar()
regularPrice = IntVar()
regularCount = IntVar()
maharajaCount = IntVar()
maharajaPrice = IntVar()
paneerCount2Price = IntVar()
paneerCount2 = IntVar()
cheeseCount2 = regularCount = maharajaCount = paneerCount2 = 0
cheeseCount2Price = regularPrice = maharajaPrice = paneerCount2Price = 0

# PIZZA
pizzaTotal = StringVar()
basilpaneerPrice = IntVar()
mushroomPrice = IntVar()
margheritaPrice = IntVar()
onioncheesePrice = IntVar()
basilpaneerCount = IntVar()
mushroomCount = IntVar()
margheritaCount = IntVar()
onioncheeseCount = IntVar()
basilpaneerCount = onioncheeseCount = mushroomCount = margheritaCount = 0
basilpaneerPrice = onioncheesePrice = mushroomPrice = margheritaPrice = 0

# PASTA
pastaTotal = StringVar()
paneerpastaPrice = IntVar()
whitesaucePrice = IntVar()
garlicPrice = IntVar()
spinachPrice = IntVar()
spinachCount = IntVar()
garlicCount = IntVar()
whitesauceCount = IntVar()
paneerpastaCount = IntVar()
paneerpastaCount = whitesauceCount = spinachCount = garlicCount = 0
paneerpastaPrice = whitesaucePrice = spinachPrice = garlicPrice = 0

##MAINCOURSE

# SOUTHINDIAN
southindianTotal = StringVar()
dosaPrice = IntVar()
idliPrice = IntVar()
vadaPrice = IntVar()
puliyogrePrice = IntVar()
avalakkibhaatPrice = IntVar()
kharabhaatPrice = IntVar()
dosaCount = IntVar()
idliCount = IntVar()
vadaCount = IntVar()
puliyogreCount = IntVar()
avalakkibhaatCount = IntVar()
kharabhaatCount = IntVar()
dosaCount = idliCount = puliyogreCount = kharabhaatCount = avalakkibhaatCount = vadaCount = 0
dosaPrice = idliPrice = puliyogrePrice = kharabhaatPrice = avalakkibhaatPrice = vadaPrice = 0

# CURRIES
curriesTotal = StringVar()
rajmaPrice = IntVar()
dalPrice = IntVar()
kolhapuriPrice = IntVar()
cholePrice = IntVar()
rajmaCount = IntVar()
dalCount = IntVar()
kolhapuriCount = IntVar()
choleCount = IntVar()
rajmaCount = dalCount = kolhapuriCount = choleCount = 0
rajmaPrice = dalPrice = kolhapuriPrice = cholePrice = 0

# ROTI
rotiTotal = StringVar()
naanPrice = IntVar()
missiPrice = IntVar()
parathaPrice = IntVar()
tandoorirotiPrice = IntVar()
naanCount = IntVar()
missiCount = IntVar()
parathaCount = IntVar()
tandoorirotiCount = IntVar()
tandoorirotiCount = missiCount = parathaCount = naanCount = 0
tandoorirotiPrice = missiPrice = parathaPrice = naanPrice = 0

# NORTHINDIAN
northindianTotal = StringVar()
rajmaparathaPrice = IntVar()
paneerparathaPrice = IntVar()
mushroomparathaPrice = IntVar()
dalparathaPrice = IntVar()
rajmaparathaCount = IntVar()
paneerparathaCount = IntVar()
mushroomparathaCount = IntVar()
dalparathaCount = IntVar()
rajmaparathaCount = dalparathaCount = mushroomparathaCount = paneerparathaCount = 0
rajmaparathaPrice = dalparathaPrice = mushroomparathaPrice = paneerparathaPrice = 0

# THALI
thaliTotal = StringVar()
specialthaliPrice = IntVar()
executivethaliPrice = IntVar()
familythaliPrice = IntVar()
regularthaliPrice = IntVar()
specialthaliCount = IntVar()
executivethaliCount = IntVar()
familythaliCount = IntVar()
regularthaliCount = IntVar()
specialthaliCount = executivethaliCount = familythaliCount = regularthaliCount = 0
specialthaliPrice = executivethaliPrice = familythaliPrice = regularthaliPrice = 0

# CONTINENTAL
continentalTotal = StringVar()
pancakesPrice = IntVar()
capresesandwichPrice = IntVar()
wafflePrice = IntVar()
parfaitPrice = IntVar()
pancakesCount = IntVar()
capresesandwichCount = IntVar()
waffleCount = IntVar()
parfaitCount = IntVar()
pancakesCount = capresesandwichCount = waffleCount = parfaitCount = 0
pancakesPrice = capresesandwichPrice = wafflePrice = parfaitPrice = 0

##BEVERAGES

# COFFEE
coffeeTotal = StringVar()
americanoPrice = IntVar()
cappuccinoPrice = IntVar()
machiatoPrice = IntVar()
espressoPrice = IntVar()
lattePrice = IntVar()
mochaPrice = IntVar()
americanoCount = IntVar()
cappuccinoCount = IntVar()
machiatoCount = IntVar()
espressoCount = IntVar()
latteCount = IntVar()
mochaCount = IntVar()
mochaCount = latteCount = espressoCount = machiatoCount = cappuccinoCount = americanoCount = 0
mochaPrice = lattePrice = espressoPrice = machiatoPrice = cappuccinoPrice = americanoPrice = 0

# TEA
teaTotal = StringVar()
chamomilePrice = IntVar()
whiteTeaPrice = IntVar()
greenTeaPrice = IntVar()
gingerTeaPrice = IntVar()
hibiscusTeaPrice = IntVar()
lavenderTeaPrice = IntVar()
oolongTeaPrice = IntVar()
lemonTeaPrice = IntVar()
chamomileCount = IntVar()
whiteTeaCount = IntVar()
greenTeaCount = IntVar()
gingerTeaCount = IntVar()
hibiscusTeaCount = IntVar()
lavenderTeaCount = IntVar()
oolongTeaCount = IntVar()
lemonTeaCount = IntVar()
chamomileCount = lavenderTeaCount = hibiscusTeaCount = oolongTeaCount = lemonTeaCount = gingerTeaCount = greenTeaCount = whiteTeaCount = 0
chamomilePrice = lavenderTeaPrice = hibiscusTeaPrice = oolongTeaPrice = lemonTeaPrice = gingerTeaPrice = greenTeaPrice = whiteTeaPrice = 0

# COKE
cokeTotal = StringVar()
zeroPrice = IntVar()
cokePrice = IntVar()
pepsiPrice = IntVar()
sevenupPrice = IntVar()
zeroCount = IntVar()
cokeCount = IntVar()
pepsiCount = IntVar()
sevenupCount = IntVar()
zeroCount = sevenupCount = pepsiCount = cokeCount = 0
zeroPrice = sevenupPrice = pepsiPrice = cokePrice = 0

# JUICE
juiceTotal = StringVar()
lemonjuicePrice = IntVar()
orangejuicePrice = IntVar()
watermelonPrice = IntVar()
carrotjuicePrice = IntVar()
lemonjuiceCount = IntVar()
orangejuiceCount = IntVar()
watermelonCount = IntVar()
carrotjuiceCount = IntVar()
lemonjuiceCount = watermelonCount = carrotjuiceCount = orangejuiceCount = 0
lemonjuicePrice = watermelonPrice = carrotjuicePrice = orangejuicePrice = 0

# FRAPPE
frappeTotal = StringVar()
caramelFrappePrice = IntVar()
berryFrappePrice = IntVar()
chocoFrappePrice = IntVar()
orangeFrappePrice = IntVar()
caramelFrappeCount = IntVar()
berryFrappeCount = IntVar()
chocoFrappeCount = IntVar()
orangeFrappeCount = IntVar()
caramelFrappeCount = berryFrappeCount = chocoFrappeCount = orangeFrappeCount = 0
caramelFrappePrice = berryFrappePrice = chocoFrappePrice = orangeFrappePrice = 0

# ICECREAM
icecreamTotal = StringVar()
vanillaPrice = IntVar()
butterscotchPrice = IntVar()
mangoPrice = IntVar()
blackcurrantPrice = IntVar()
vanillaCount = IntVar()
butterscotchCount = IntVar()
mangoCount = IntVar()
blackcurrantCount = IntVar()
vanillaCount = blackcurrantCount = mangoCount = butterscotchCount = 0
vanillaPrice = blackcurrantPrice = mangoPrice = butterscotchPrice = 0

##DESSERT
dessertTotal = StringVar()
rasgullaPrice = IntVar()
gulabjamunPrice = IntVar()
browniePrice = IntVar()
rasmalaiPrice = IntVar()
rasmalaiCount = IntVar()
rasgullaCount = IntVar()
gulabjamunCount = IntVar()
brownieCount = IntVar()
rasgullaCount = gulabjamunCount = brownieCount = rasmalaiCount = 0
rasgullaPrice = gulabjamunPrice = browniePrice = rasmalaiPrice = 0

# Creating final calculators
var_starterTotal = IntVar()
var_mainCourseTotal = IntVar()
var_beveragesTotal = IntVar()
var_tax = IntVar()
var_bill = IntVar()
var_netBill = IntVar()
var_dessertTotal = IntVar()
var_discountTotal = IntVar()
var_starterTotal = var_discountTotal = var_dessertTotal = var_beveragesTotal = var_tax = var_mainCourseTotal = var_netBill = var_bill = 0


##Creating the menu1 tabs for each menu

##STARTERS

# SANDWICH
def sandwichBtn():
    sandwich = Toplevel()
    sandwich.title('Sandwich')
    sandwich.config(bg='light yellow')
    sandwich.geometry('450x330+300+370')
    sandwich.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, pizza1, tandoori, mexican, club
    global pizzaCount, tandooriCount, mexicanCount1, clubCount

    # defining the functions to increase each count by 1
    def pizzaCLick():
        global pizzaCount
        pizzaCount += 1

    def tandooriCLick():
        global tandooriCount
        tandooriCount += 1

    def mexicanClick():
        global mexicanCount1
        mexicanCount1 += 1

    def clubClick():
        global clubCount
        clubCount += 1

    # initialising the close button whenever OKToGO Button is clicked
    def close():
        sandwich.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(sandwich, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda g: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Sandwich', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()], font=('times new roman', 30),
                        bg='lightyellow', fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def pizzaClick1():
        global pizzaCount, pizzaPrice
        pizzaPrice = pizzaCount * 170
        MochaLabel = Label(second_frame1, text=f"{str(pizzaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=258, width=20, height=20)

    pizza1 = PhotoImage(file="images/Sandwiches/pizzaround.png")
    pizza_Btn = Button(second_frame1, image=pizza1, command=lambda: [pizzaCLick(), pizzaClick1(), ],
                       font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    pizza_Btn.grid(row=1, column=0, pady=10, padx=25)

    def tandooriClick1():
        global tandooriCount, tandooriPrice
        tandooriPrice = tandooriCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(tandooriCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=258, width=20, height=20)

    tandoori = PhotoImage(file="images/Sandwiches/tandooriround.png")
    tandoori_Btn = Button(second_frame1, image=tandoori, command=lambda: [tandooriCLick(), tandooriClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    tandoori_Btn.grid(row=1, column=1)

    def mexicanClick1():
        global mexicanCount1, mexicanCount1Price
        mexicanCount1Price = mexicanCount1 * 150
        MochaLabel = Label(second_frame1, text=f"{str(mexicanCount1)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=495, width=20, height=20)

    mexican = PhotoImage(file="images/Sandwiches/mexicanround.png")
    mexican_Btn = Button(second_frame1, image=mexican, command=lambda: [mexicanClick(), mexicanClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                         bd=4)
    mexican_Btn.grid(row=2, column=0, pady=48)

    def clubClick1():
        global clubCount, clubCountPrice
        clubCountPrice = clubCount * 100
        MochaLabel = Label(second_frame1, text=f"{str(clubCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=495, width=20, height=20)

    club = PhotoImage(file="images/Sandwiches/clubround.png")
    club_Btn = Button(second_frame1, image=club, command=lambda: [clubClick(), clubClick1()],
                      font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    club_Btn.grid(row=2, column=1)


# FRANKIE
def frankieBtn():
    frankie = Toplevel()
    frankie.title('Frankie')
    frankie.config(bg='light yellow')
    frankie.geometry('450x330+705+370')
    frankie.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, mixveg, paneer, cheese, schezwanpaneer, addImage, subtractImage

    # defining the functions to increase each count by 1
    def mixvegCLick():
        global mixvegCount
        mixvegCount += 1

    def cheeseCLick():
        global cheeseCount1
        cheeseCount1 += 1

    def chillipaneerClick():
        global chillipaneerCount1
        chillipaneerCount1 += 1

    def schezwanpaneerClick():
        global schezwanpaneerCount
        schezwanpaneerCount += 1

    # initialising the close button whenever OKToGO Button is clicked
    def close():
        frankie.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(frankie, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Frankie', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow', fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def mixvegClick1():
        global mixvegCount, mixvegPrice, frankieTotal
        mixvegPrice = mixvegCount * 130

        MochaLabel = Label(second_frame1, text=f"{str(mixvegCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=104, y=253, width=20, height=20)

        def updatePrice():
            global mixvegCount, mixvegPrice, frankieTotal
            frankieTotal = str(mixvegPrice + chillipaneerCount1Price + cheeseCount1Price + schezwanpaneerPrice)
            print(frankieTotal)
            if frankieTotal == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='Frankie', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=10, y=4, height =75, width=200)
            elif frankieTotal != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='Frankie Total', font=('times new roman', 13, 'bold')
                                   , relief = RIDGE, bd = 2, bg='lightyellow',fg='red')
                priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal, relief=RIDGE, font=('times new roman', 30, 'bold'),
                                   bg='lightblue',fg='black')
                priceShow_Lbl.place(x=10, y=0, width=160, height=50)
        updatePrice()


    mixveg = PhotoImage(file="images/Frankie/mixveg.png")
    mixveg_Label = Label(second_frame1, image=mixveg,
                     font=('times new roman', 30), anchor='c')
    mixveg_Label.grid(row=1, column=0, pady=10, padx=20, ipadx=1, ipady=1)


    def add():
        global mixvegCount
        mixvegCount+=1

    def subtract():
        global mixvegCount
        if mixvegCount > 0:
            mixvegCount-=1
        elif mixvegCount <= 0:
            mixvegCount=0

    addImage = PhotoImage(file = "images/Extras/addition.png")
    AddButton = Button(second_frame1, image = addImage, font=('times new roman', 15),bg='lightyellow'
                       , anchor='c', cursor='hand2', bd=2, command = lambda: [add(),mixvegClick1()])
    AddButton.place(x=125, y=253, width=20, height=20)

    subtractImage = PhotoImage(file = "images/Extras/subtraction.png")
    SubtractButton = Button(second_frame1, image = subtractImage, font=('times new roman', 15),bg='lightyellow'
                            , anchor='c', cursor='hand2', bd=2, command = lambda: [subtract(),mixvegClick1()])
    SubtractButton.place(x=83, y=253, width=20, height=20)

    def chillipaneerClick1():
        global chillipaneerCount1, chillipaneerCount1Price
        chillipaneerCount1Price = chillipaneerCount1 * 150
        MochaLabel = Label(second_frame1, text=f"{str(chillipaneerCount1)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=253, width=20, height=20)

        def updatePrice():
            global chillipaneerCount1, chillipaneerCount1Price, frankieTotalchilli
            frankieTotalchilli = str(mixvegPrice + chillipaneerCount1Price + cheeseCount1Price + schezwanpaneerPrice)
            print(frankieTotalchilli)
            if frankieTotalchilli == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='Frankie', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=10, y=4, height=75, width=200)
            elif frankieTotalchilli != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='Frankie Total',
                                                font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotalchilli, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=160, height=50)

        updatePrice()

    chillipaneer = PhotoImage(file="images/Frankie/chillipaneer.png")
    chillipaneer_Label = Label(second_frame1, image=chillipaneer,
                             font=('times new roman', 30), anchor='c')
    chillipaneer_Label.image=chillipaneer
    chillipaneer_Label.grid(row=1, column=1, pady=10, padx=20, ipadx=1, ipady=1)

    def addchilli():
        global chillipaneerCount1
        chillipaneerCount1 += 1

    def subtractchilli():
        global chillipaneerCount1
        if chillipaneerCount1 > 0:
            chillipaneerCount1 -= 1
        elif chillipaneerCount1 <= 0:
            chillipaneerCount1 = 0

    AddButtonchilli = Button(second_frame1, image=addImage, font=('times new roman', 15), bg='lightyellow'
                       , anchor='c', cursor='hand2', bd=2, command=lambda: [addchilli(), chillipaneerClick1()])
    AddButtonchilli.place(x=334, y=253, width=20, height=20)

    SubtractButtonchilli = Button(second_frame1, image=subtractImage, font=('times new roman', 15), bg='lightyellow'
                            , anchor='c', cursor='hand2', bd=2, command=lambda: [subtractchilli(), chillipaneerClick1()])
    SubtractButtonchilli.place(x=292, y=253, width=20, height=20)


    def vegFingerClick1():
        global cheeseCount1, cheeseCount1Price
        cheeseCount1Price = cheeseCount1 * 160
        MochaLabel = Label(second_frame1, text=f"{str(cheeseCount1)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=500, width=20, height=20)

    vegFinger = PhotoImage(file="images/Frankie/vegfinger.png")
    vegFinger_Btn = Button(second_frame1, image=vegFinger, command=lambda: [cheeseCLick(), cheeseClick1()],
                        font=('times new roman', 30),
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    vegFinger_Btn.image=vegFinger
    vegFinger_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def schezwanpaneerClick1():
        global schezwanpaneerCount, schezwanpaneerPrice
        schezwanpaneerPrice = schezwanpaneerCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(schezwanpaneerCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=500, width=20, height=20)

    schezwanpaneer = PhotoImage(file="images/Frankie/schezwanpaneer.png")
    schezwanpaneer_Btn = Button(second_frame1, image=schezwanpaneer, command=lambda: [schezwanpaneerClick(), schezwanpaneerClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    schezwanpaneer_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# SUBWAY
def SubwayBtn():
    subway = Toplevel(root)
    subway.title('Subway')
    subway.config(bg='light yellow')
    subway.geometry('470x330+1097+370')
    subway.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, harabhara, paneertikka, paneerfillet, mexican3

    # defining the functions to increase each count by 1
    def harabharaCLick():
        global harabharaCount
        harabharaCount += 1

    def paneerFilletCLick():
        global paneerFilletCount
        paneerFilletCount += 1

    def paneertikkaClick():
        global paneertikkaCount
        paneertikkaCount += 1

    def mexicanClick():
        global mexicanCount2
        mexicanCount2 += 1

    # initialising the close button whenever OKToGO Button is clicked
    def close():
        subway.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(subway, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Subway', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def harabharaClick1():
        global harabharaCount,harabharaPrice
        harabharaPrice=harabharaCount*150
        MochaLabel = Label(second_frame1, text=f"{str(harabharaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=254, width=20, height=20)

    harabhara = PhotoImage(file="images/Subway/harabhararound.png")
    harabhara_Btn = Button(second_frame1, image=harabhara, command=lambda: [harabharaCLick(), harabharaClick1()],
                           font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                           bd=4)
    harabhara_Btn.grid(row=1, column=0, pady=10, padx=24, ipadx=5, ipady=5)

    def paneerfilletClick1():
        global paneerFilletCount, paneerFilletPrice
        paneerFilletPrice=paneerFilletCount*175
        MochaLabel = Label(second_frame1, text=f"{str(paneerFilletCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=325, y=254, width=20, height=20)

    paneerfillet = PhotoImage(file="images/Subway/paneerfilletround.png")
    paneerfillet_Btn = Button(second_frame1, image=paneerfillet,
                              command=lambda: [paneerFilletCLick(), paneerfilletClick1()],
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2',
                              bd=4)
    paneerfillet_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def mexicanClick1():
        global mexicanCount2,mexicanCount2Price
        mexicanCount2Price=mexicanCount2*190
        MochaLabel = Label(second_frame1, text=f"{str(mexicanCount2)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=501, width=20, height=20)

    mexican3 = PhotoImage(file="images/Subway/mexicansubwayround.png")
    mexican_Btn = Button(second_frame1, image=mexican3, command=lambda: [mexicanClick(), mexicanClick1()],
                         font=('times new roman', 30),
                         bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    mexican_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def paneertikkaClick1():
        global paneertikkaCount,paneertikkaPrice
        paneertikkaPrice=paneertikkaCount*185
        MochaLabel = Label(second_frame1, text=f"{str(paneertikkaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=325, y=501, width=20, height=20)

    paneertikka = PhotoImage(file="images/Subway/paneertikkaround.png")
    paneertikka_Btn = Button(second_frame1, image=paneertikka,
                             command=lambda: [paneertikkaClick(), paneertikkaClick1()],
                             font=('times new roman', 30),
                             bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    paneertikka_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# BURGER
def BurgerBtn():
    burger = Toplevel()
    burger.title('Burger')
    burger.config(bg='light yellow')
    burger.geometry('420x330+300+370')
    burger.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, maharaja, paneer, regular, cheese

    # defining the functions to increase each count by 1
    def cheeseCLick():
        global cheeseCount2
        cheeseCount2 += 1

    def regularCLick():
        global regularCount
        regularCount += 1

    def paneerClick():
        global paneerCount2
        paneerCount2 += 1

    def maharajaClick():
        global maharajaCount
        maharajaCount += 1

    # initialising the close button whenever OKToGO Button is clicked
    def close():
        burger.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(burger, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Burger', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def cheeseClick1():
        global cheeseCount2, cheeseCount2Price
        cheeseCount2Price = cheeseCount2 * 165
        MochaLabel = Label(second_frame1, text=f"{str(cheeseCount2)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=91, y=235, width=20, height=20)

    cheese = PhotoImage(file="images/Burger/paneer-cheesesupreme.png")
    cheese_Btn = Button(second_frame1, image=cheese, command=lambda: [cheeseCLick(), cheeseClick1()],
                        font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                        bd=4)
    cheese_Btn.grid(row=1, column=0, pady=10, padx=25, ipadx=5, ipady=5)

    def regularClick1():
        global regularCount, regularPrice
        regularPrice = regularCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(regularCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=280, y=235, width=20, height=20)

    regular = PhotoImage(file="images/Burger/regularburger.png")
    regular_Btn = Button(second_frame1, image=regular, command=lambda: [regularCLick(), regularClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                         bd=4)
    regular_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def paneerClick1():
        global paneerCount2, paneerCount2Price
        paneerCount2Price = paneerCount2 * 160
        MochaLabel = Label(second_frame1, text=f"{str(paneerCount2)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=91, y=445, width=20, height=20)

    paneer = PhotoImage(file="images/Burger/paneerburger.png")
    paneer_Btn = Button(second_frame1, image=paneer, command=lambda: [paneerClick(), paneerClick1()],
                        font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                        bd=4)
    paneer_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def maharajaClick1():
        global maharajaCount, maharajaPrice
        maharajaPrice = maharajaCount * 180
        MochaLabel = Label(second_frame1, text=f"{str(maharajaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=280, y=445, width=20, height=20)

    maharaja = PhotoImage(file="images/Burger/maharajaburger.png")
    maharaja_Btn = Button(second_frame1, image=maharaja, command=lambda: [maharajaClick(), maharajaClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    maharaja_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# PIZZA
def PizzaBtn():
    pizza = Toplevel()
    pizza.title('Pizza')
    pizza.config(bg='light yellow')
    pizza.geometry('450x330+705+370')
    pizza.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, margherita, basilpaneer, onioncheese, mushroom

    # defining the functions to increase each count by 1
    def margheritaCLick():
        global margheritaCount
        margheritaCount += 1

    def basilpaneerCLick():
        global basilpaneerCount
        basilpaneerCount += 1

    def onioncheeseClick():
        global onioncheeseCount
        onioncheeseCount += 1

    def mushroomClick():
        global mushroomCount
        mushroomCount += 1

    def close():
        pizza.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(pizza, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Pizza', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def margheritaClick1():
        global margheritaCount, margheritaPrice
        margheritaPrice = margheritaCount * 190
        MochaLabel = Label(second_frame1, text=f"{str(margheritaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=107, y=268, width=20, height=20)

    margherita = PhotoImage(file="images/Pizza/margheritaround.png")
    margherita_Btn = Button(second_frame1, image=margherita,
                            command=lambda: [margheritaCLick(), margheritaClick1()],
                            font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                            bd=4)
    margherita_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=5, ipady=5)

    def basilpaneerClick1():
        global basilpaneerCount, basilpaneerPrice
        basilpaneerPrice = basilpaneerCount * 250
        MochaLabel = Label(second_frame1, text=f"{str(basilpaneerCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=319, y=268, width=20, height=20)

    basilpaneer = PhotoImage(file="images/Pizza/basilpaneerround.png")
    basilpaneer_Btn = Button(second_frame1, image=basilpaneer,
                             command=lambda: [basilpaneerCLick(), basilpaneerClick1()],
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                             cursor='hand2', bd=4)
    basilpaneer_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def mushroomClick1():
        global mushroomCount, mushroomPrice
        mushroomPrice = mushroomCount * 210
        MochaLabel = Label(second_frame1, text=f"{str(mushroomCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=107, y=517, width=20, height=20)

    mushroom = PhotoImage(file="images/Pizza/mushroomround.png")
    mushroom_Btn = Button(second_frame1, image=mushroom, command=lambda: [mushroomClick(), mushroomClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    mushroom_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def onioncheeseClick1():
        global onioncheeseCount, onioncheesePrice
        onioncheesePrice = onioncheeseCount * 230
        MochaLabel = Label(second_frame1, text=f"{str(onioncheeseCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=319, y=517, width=20, height=20)

    onioncheese = PhotoImage(file="images/Pizza/onioncheeseround.png")
    onioncheese_Btn = Button(second_frame1, image=onioncheese,
                             command=lambda: [onioncheeseClick(), onioncheeseClick1()],
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                             cursor='hand2', bd=4)
    onioncheese_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# PASTA
def pastaBtn():
    pasta = Toplevel()
    pasta.title('Pasta')
    pasta.config(bg='light yellow')
    pasta.geometry('450x330+1110+370')
    pasta.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, garlic, spinach, paneerpasta, whitesauce

    # defining the functions to increase each count by 1
    def garlicCLick():
        global garlicCount
        garlicCount += 1

    def spinachCLick():
        global spinachCount
        spinachCount += 1

    def paneerpastaClick():
        global paneerpastaCount
        paneerpastaCount += 1

    def whitesauceClick():
        global whitesauceCount
        whitesauceCount += 1

    def close():
        pasta.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(pasta, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Pasta', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def garlicClick1():
        global garlicCount, garlicPrice
        garlicPrice = garlicCount * 135
        MochaLabel = Label(second_frame1, text=f"{str(garlicCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=273, width=20, height=20)

    garlic = PhotoImage(file="images/Pasta/garlicround.png")
    garlic_Btn = Button(second_frame1, image=garlic, command=lambda: [garlicCLick(), garlicClick1()],
                        font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                        bd=4)
    garlic_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=5, ipady=5)

    def whitesauceClick1():
        global whitesauceCount, whitesaucePrice
        whitesaucePrice = whitesauceCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(whitesauceCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=310, y=273, width=20, height=20)

    whitesauce = PhotoImage(file="images/Pasta/whitesauceround.png")
    whitesauce_Btn = Button(second_frame1, image=whitesauce,
                            command=lambda: [whitesauceClick(), whitesauceClick1()],
                            font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                            cursor='hand2', bd=4)
    whitesauce_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def spinachClick1():
        global spinachCount, spinachPrice
        spinachPrice = spinachCount * 130
        MochaLabel = Label(second_frame1, text=f"{str(spinachCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=102, y=525, width=20, height=20)

    spinach = PhotoImage(file="images/Pasta/spinachround.png")
    spinach_Btn = Button(second_frame1, image=spinach, command=lambda: [spinachCLick(), spinachClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                         cursor='hand2', bd=4)
    spinach_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def paneerpastaClick1():
        global paneerpastaCount, paneerpastaPrice
        paneerpastaPrice = paneerpastaCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(paneerpastaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=314, y=525, width=20, height=20)

    paneerpasta = PhotoImage(file="images/Pasta/paneerpastaround.png")
    paneerpasta_Btn = Button(second_frame1, image=paneerpasta,
                             command=lambda: [paneerpastaClick(), paneerpastaClick1()],
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                             bd=4)
    paneerpasta_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


##MAINCOURSE

# SOUTHINDIAN
def southIndianBtn():
    southindian = Toplevel()
    southindian.title('South Indian')
    southindian.config(bg='light yellow')
    southindian.geometry('450x330+300+300')
    southindian.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, idli, vada, dosa, puliyogre, avalakkibhaat, kharabhaat

    # defining the functions to increase each count by 1
    def idliCLick():
        global idliCount
        idliCount += 1

    def vadaCLick():
        global vadaCount
        vadaCount += 1

    def dosaClick():
        global dosaCount
        dosaCount += 1

    def puliyogreClick():
        global puliyogreCount
        puliyogreCount += 1

    def avalakkibhaatClick():
        global avalakkibhaatCount
        avalakkibhaatCount += 1

    def kharabhaatClick():
        global kharabhaatCount
        kharabhaatCount += 1

    def close():
        southindian.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(southindian, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='South Indian', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def idliClick1():
        global idliCount, idliPrice
        idliPrice = idliCount * 110
        MochaLabel = Label(second_frame1, text=f"{str(idliCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=268, width=20, height=20)

    idli = PhotoImage(file="images/SouthIndian/idliround.png")
    idli_Btn = Button(second_frame1, image=idli, command=lambda: [idliCLick(), idliClick1()],
                      font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                      bd=4)
    idli_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=5, ipady=5)

    def vadaClick1():
        global vadaCount, vadaPrice
        vadaPrice = vadaCount * 90
        MochaLabel = Label(second_frame1, text=f"{str(vadaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=315, y=268, width=20, height=20)

    vada = PhotoImage(file="images/SouthIndian/vadaround.png")
    vada_Btn = Button(second_frame1, image=vada, command=lambda: [vadaCLick(), vadaClick1()],
                      font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                      bd=4)
    vada_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def dosaClick1():
        global dosaCount, dosaPrice
        dosaPrice = dosaCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(dosaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=517, width=20, height=20)

    dosa = PhotoImage(file="images/SouthIndian/dosaround.png")
    dosa_Btn = Button(second_frame1, image=dosa, command=lambda: [dosaClick(), dosaClick1()],
                      font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                      bd=4)
    dosa_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def avalakkibhaatClick1():
        global avalakkibhaatCount, avalakkibhaatPrice
        avalakkibhaatPrice = avalakkibhaatCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(avalakkibhaatCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=315, y=517, width=20, height=20)

    avalakkibhaat = PhotoImage(file="images/SouthIndian/avalakkibhaatround.png")
    avalakkibhaat_Btn = Button(second_frame1, image=avalakkibhaat,
                               command=lambda: [avalakkibhaatClick(), avalakkibhaatClick1()],
                               font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                               cursor='hand2',
                               bd=4)
    avalakkibhaat_Btn.grid(row=2, column=1, ipadx=5, ipady=5)

    def kharabhaatClick1():
        global kharabhaatCount, kharabhaatPrice
        kharabhaatPrice = kharabhaatCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(kharabhaatCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=755, width=20, height=20)

    kharabhaat = PhotoImage(file="images/SouthIndian/kharabhaatround.png")
    kharabhaat_Btn = Button(second_frame1, image=kharabhaat,
                            command=lambda: [kharabhaatClick(), kharabhaatClick1()],
                            font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                            bd=4)
    kharabhaat_Btn.grid(row=3, column=0, ipadx=5, ipady=5)

    def puliyogreClick1():
        global puliyogreCount, puliyogrePrice
        puliyogrePrice = puliyogreCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(puliyogreCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=315, y=755, width=20, height=20)

    puliyogre = PhotoImage(file="images/SouthIndian/puliyogreround.png")
    puliyogre_Btn = Button(second_frame1, image=puliyogre, command=lambda: [puliyogreClick(), puliyogreClick1()],
                           font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                           bd=4)
    puliyogre_Btn.grid(row=3, column=1, ipadx=5, ipady=5)


# VEGCURRY
def curryBtn():
    curry = Toplevel()
    curry.title('Veg Curry')
    curry.config(bg='light yellow')
    curry.geometry('450x330+795+370')
    curry.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, chole, kolhapuri, dal, rajma

    # defining the functions to increase each count by 1
    def choleCLick():
        global choleCount
        choleCount += 1

    def kolhapuriCLick():
        global kolhapuriCount
        kolhapuriCount += 1

    def dalClick():
        global dalCount
        dalCount += 1

    def rajmaClick():
        global rajmaCount
        rajmaCount += 1

    def close():
        curry.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(curry, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Veg Curry', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def rajmaClick1():
        global rajmaCount, rajmaPrice
        rajmaPrice = rajmaCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(rajmaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=273, width=20, height=20)

    rajma = PhotoImage(file="images/Curries/rajmaround.png")
    rajma_Btn = Button(second_frame1, image=rajma, command=lambda: [rajmaClick(), rajmaClick1()],
                       font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                       bd=4)
    rajma_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=5, ipady=5)

    def dalClick1():
        global dalCount, dalPrice
        dalPrice = dalCount * 100
        MochaLabel = Label(second_frame1, text=f"{str(dalCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=310, y=273, width=20, height=20)

    dal = PhotoImage(file="images/Curries/dalround.png")
    dal_Btn = Button(second_frame1, image=dal, command=lambda: [dalClick(), dalClick1()],
                     font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                     cursor='hand2', bd=4)
    dal_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def kolhapuriClick1():
        global kolhapuriCount, kolhapuriPrice
        kolhapuriPrice = kolhapuriCount * 130
        MochaLabel = Label(second_frame1, text=f"{str(kolhapuriCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=102, y=525, width=20, height=20)

    kolhapuri = PhotoImage(file="images/Curries/kolhapuriround.png")
    kolhapuri_Btn = Button(second_frame1, image=kolhapuri, command=lambda: [kolhapuriCLick(), kolhapuriClick1()],
                           font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                           cursor='hand2', bd=4)
    kolhapuri_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def choleClick1():
        global choleCount, cholePrice
        cholePrice = choleCount * 130
        MochaLabel = Label(second_frame1, text=f"{str(choleCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=314, y=525, width=20, height=20)

    chole = PhotoImage(file="images/Curries/choleround.png")
    chole_Btn = Button(second_frame1, image=chole, command=lambda: [choleCLick(), choleClick1()],
                       font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    chole_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# ROTI
def rotiBtn():
    roti = Toplevel()
    roti.title('Indian Breads')
    roti.config(bg='light yellow')
    roti.geometry('450x330+1110+370')
    roti.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, tandooriroti, naan, paratha, missi

    # defining the functions to increase each count by 1
    def naanCLick():
        global naanCount
        naanCount += 1

    def tandoorirotiCLick():
        global tandoorirotiCount
        tandoorirotiCount += 1

    def parathaClick():
        global parathaCount
        parathaCount += 1

    def missiClick():
        global missiCount
        missiCount += 1

    def close():
        roti.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(roti, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Breads', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def naanClick1():
        global naanCount, naanPrice
        naanPrice = naanCount * 80
        MochaLabel = Label(second_frame1, text=f"{str(naanCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=277, width=20, height=20)

    naan = PhotoImage(file="images/Roti/naanround.png")
    naan_Btn = Button(second_frame1, image=naan, command=lambda: [naanCLick(), naanClick1()],
                      font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                      bd=4)
    naan_Btn.grid(row=1, column=0, pady=10, padx=8, ipadx=5, ipady=5)

    def missiClick1():
        global missiCount, missiPrice
        missiPrice = missiCount * 65
        MochaLabel = Label(second_frame1, text=f"{str(missiCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=310, y=277, width=20, height=20)

    missi = PhotoImage(file="images/Roti/missiround.png")
    missi_Btn = Button(second_frame1, image=missi, command=lambda: [missiClick(), missiClick1()],
                       font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                       cursor='hand2', bd=4)
    missi_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def parathaClick1():
        global parathaCount, parathaPrice
        parathaPrice = parathaCount * 40
        MochaLabel = Label(second_frame1, text=f"{str(parathaCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=102, y=535, width=20, height=20)

    paratha = PhotoImage(file="images/Roti/paratharound.png")
    paratha_Btn = Button(second_frame1, image=paratha, command=lambda: [parathaClick(), parathaClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                         cursor='hand2', bd=4)
    paratha_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def tandoorirotiClick1():
        global tandoorirotiCount, tandoorirotiPrice
        tandoorirotiPrice = tandoorirotiCount * 46
        MochaLabel = Label(second_frame1, text=f"{str(tandoorirotiCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=314, y=535, width=20, height=20)

    tandooriroti = PhotoImage(file="images/Roti/tandoorirotiround.png")
    tandooriroti_Btn = Button(second_frame1, image=tandooriroti,
                              command=lambda: [tandoorirotiCLick(), tandoorirotiClick1()],
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2',
                              bd=4)
    tandooriroti_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# NORTH INDIAN
def northindianBtn():
    northindian = Toplevel()
    northindian.title('North Indian')
    northindian.config(bg='light yellow')
    northindian.geometry('450x330+300+440')
    northindian.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, rajmaparatha, mushroomparatha, paneerparatha, dalparatha

    # defining the functions to increase each count by 1
    def dalparathaCLick():
        global dalparathaCount
        dalparathaCount += 1

    def paneerparathaCLick():
        global paneerparathaCount
        paneerparathaCount += 1

    def rajmaparathaClick():
        global rajmaparathaCount
        rajmaparathaCount += 1

    def mushroomparathaClick():
        global mushroomparathaCount
        mushroomparathaCount += 1

    def close():
        northindian.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(northindian, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='North Indian', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def rajmaparathaClick1():
        global rajmaparathaCount, rajmaparathaPrice
        rajmaparathaPrice = rajmaparathaCount * 200
        MochaLabel = Label(second_frame1, text=f"{str(rajmaparathaCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=112, y=253, width=20, height=20)

        def updatePrice():
            global rajmaparathaCount, rajmaparathaPrice, frankieTotal1
            frankieTotal1 = str(rajmaparathaPrice + dalparathaPrice + mushroomparathaPrice + paneerparathaPrice)
            print(frankieTotal1)
            if frankieTotal1 == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='North Indian', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=2, y=4, height=75, width=220)
            elif frankieTotal1 != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='N.Indian Total',
                                                font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=2, y=4, height=75, width=220)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal1, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=180, height=50)

        updatePrice()

    rajmaparatha = PhotoImage(file="images/NorthIndian/rajmaparatharound.png")
    rajmaparatha_Btn = Label(second_frame1, image=rajmaparatha,
                             font=('times new roman', 30), anchor='c')
    rajmaparatha_Btn.image = rajmaparatha
    rajmaparatha_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=1, ipady=1)

    def add1():
        global rajmaparathaCount
        rajmaparathaCount += 1

    def subtract1():
        global rajmaparathaCount
        if rajmaparathaCount > 0:
            rajmaparathaCount -= 1
        elif rajmaparathaCount <= 0:
            rajmaparathaCount = 0

    addImage1 = PhotoImage(file="images/Extras/addition - Copy.png")
    AddButton1 = Button(second_frame1, image=addImage1, font=('times new roman', 15), bg='lightyellow'
                        , anchor='c', cursor='hand2', bd=2, command=lambda: [add1(), rajmaparathaClick1()])
    AddButton1.image = addImage1
    AddButton1.place(x=133, y=253, width=20, height=20)

    subtractImage1 = PhotoImage(file="images/Extras/subtraction - Copy.png")
    SubtractButton1 = Button(second_frame1, image=subtractImage1, font=('times new roman', 15), bg='lightyellow'
                             , anchor='c', cursor='hand2', bd=2, command=lambda: [subtract1(), rajmaparathaClick1()])
    SubtractButton1.image = subtractImage1
    SubtractButton1.place(x=91, y=253, width=20, height=20)


    def dalparathaClick1():
        global dalparathaCount, dalparathaPrice
        dalparathaPrice = dalparathaCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(dalparathaCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=330, y=253, width=20, height=20)

        def updatePrice():
            global dalparathaCount, dalparathaPrice, frankieTotal2
            frankieTotal2 = str(rajmaparathaPrice + dalparathaPrice + mushroomparathaPrice + paneerparathaPrice)
            print(frankieTotal2)
            if frankieTotal2 == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='North Indian', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=2, y=4, height=75, width=220)
            elif frankieTotal2 != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='N.Indian Total',
                                                font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=2, y=4, height=75, width=220)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal2, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=180, height=50)

        updatePrice()

    dalparatha = PhotoImage(file="images/NorthIndian/dalparatharound.png")
    dalparatha_Btn = Label(second_frame1, image=dalparatha,
                           font=('times new roman', 30), anchor='c')
    dalparatha_Btn.image = dalparatha
    dalparatha_Btn.grid(row=1, column=1, pady=10, padx=20, ipadx=1, ipady=1)

    def add2():
        global dalparathaCount
        dalparathaCount += 1

    def subtract2():
        global dalparathaCount
        if dalparathaCount > 0:
            dalparathaCount -= 1
        elif dalparathaCount <= 0:
            dalparathaCount = 0

    AddButton2 = Button(second_frame1, image=addImage1, font=('times new roman', 15), bg='lightyellow'
                        , anchor='c', cursor='hand2', bd=2, command=lambda: [add2(), dalparathaClick1()])
    AddButton2.place(x=351, y=253, width=20, height=20)

    SubtractButton2 = Button(second_frame1, image=subtractImage1, font=('times new roman', 15), bg='lightyellow'
                             , anchor='c', cursor='hand2', bd=2, command=lambda: [subtract2(), dalparathaClick1()])
    SubtractButton2.place(x=309, y=253, width=20, height=20)

    def paneerparathaClick1():
        global paneerparathaCount, paneerparathaPrice
        paneerparathaPrice = paneerparathaCount * 230
        MochaLabel = Label(second_frame1, text=f"{str(paneerparathaCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=102, y=516, width=20, height=20)

    paneerparatha = PhotoImage(file="images/NorthIndian/paneerparatharound.png")
    paneerparatha_Btn = Button(second_frame1, image=paneerparatha,
                               command=lambda: [paneerparathaCLick(), paneerparathaClick1()],
                               font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                               cursor='hand2', bd=4)
    paneerparatha_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def mushroomparathaClick1():
        global mushroomparathaCount, mushroomparathaPrice
        mushroomparathaPrice = mushroomparathaCount * 220
        MochaLabel = Label(second_frame1, text=f"{str(mushroomparathaCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=314, y=516, width=20, height=20)

    mushroomparatha = PhotoImage(file="images/NorthIndian/mushroomparatharound.png")
    mushroomparatha_Btn = Button(second_frame1, image=mushroomparatha,
                                 command=lambda: [mushroomparathaClick(), mushroomparathaClick1()],
                                 font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                                 cursor='hand2',
                                 bd=4)
    mushroomparatha_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# THALI
def thaliBtn():
    thali = Toplevel()
    thali.title('Thali')
    thali.config(bg='light yellow')
    thali.geometry('450x330+705+440')
    thali.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, specialthali, familythali, executivethali, regularthali

    # defining the functions to increase each count by 1
    def specialthaliCLick():
        global specialthaliCount
        specialthaliCount += 1

    def regularthaliCLick():
        global regularthaliCount
        regularthaliCount += 1

    def executivethaliClick():
        global executivethaliCount
        executivethaliCount += 1

    def familythaliClick():
        global familythaliCount
        familythaliCount += 1

    def close():
        thali.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(thali, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Thali', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def regularthaliClick1():
        global regularthaliCount, regularthaliPrice
        regularthaliPrice = regularthaliCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(regularthaliCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=100, y=270, width=20, height=20)

    regularthali = PhotoImage(file="images/Thali/regularthaliround.png")
    regularthali_Btn = Button(second_frame1, image=regularthali,
                              command=lambda: [regularthaliCLick(), regularthaliClick1()],
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2',
                              bd=4)
    regularthali_Btn.grid(row=1, column=0, pady=10, padx=17, ipadx=5, ipady=5)

    def executivethaliClick1():
        global executivethaliCount, executivethaliPrice
        executivethaliPrice = executivethaliCount * 180
        MochaLabel = Label(second_frame1, text=f"{str(executivethaliCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=310, y=270, width=20, height=20)

    executivethali = PhotoImage(file="images/Thali/executivethaliround.png")
    executivethali_Btn = Button(second_frame1, image=executivethali,
                                command=lambda: [executivethaliClick(), executivethaliClick1()],
                                font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                                cursor='hand2', bd=4)
    executivethali_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def familythaliClick1():
        global familythaliCount, familythaliPrice
        familythaliPrice = familythaliCount * 200
        MochaLabel = Label(second_frame1, text=f"{str(familythaliCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=102, y=516, width=20, height=20)

    familythali = PhotoImage(file="images/Thali/familythaliround.png")
    familythali_Btn = Button(second_frame1, image=familythali,
                             command=lambda: [familythaliClick(), familythaliClick1()],
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                             cursor='hand2', bd=4)
    familythali_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def specialthaliClick1():
        global specialthaliCount, specialthaliPrice
        specialthaliPrice = specialthaliCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(specialthaliCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=314, y=516, width=20, height=20)

    specialthali = PhotoImage(file="images/Thali/specialthaliround.png")
    specialthali_Btn = Button(second_frame1, image=specialthali,
                              command=lambda: [specialthaliCLick(), specialthaliClick1()],
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2',
                              bd=4)
    specialthali_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# CONTINENTAL
def continentalBtn():
    continental = Toplevel()
    continental.title('Continental')
    continental.config(bg='light yellow')
    continental.geometry('450x330+1110+440')
    continental.focus_force()
    unbindmenu()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, parfait, sandwich1, pancakes, waffle

    # defining the functions to increase each count by 1
    def waffleCLick():
        global waffleCount
        waffleCount += 1

    def parfaitCLick():
        global parfaitCount
        parfaitCount += 1

    def sandwichClick():
        global capresesandwichCount
        capresesandwichCount += 1

    def pancakesClick():
        global pancakesCount
        pancakesCount += 1

    def close():
        continental.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu()

    # Create A Main Frame
    main_frame1 = Frame(continental, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Continental', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()],
                        font=('times new roman', 30), bg='lightyellow',
                        fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def parfaitClick1():
        global parfaitCount, parfaitPrice
        parfaitPrice = parfaitCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(parfaitCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=270, width=20, height=20)

    parfait = PhotoImage(file="images/Continental/parfaitround.png")
    parfait_Btn = Button(second_frame1, image=parfait, command=lambda: [parfaitCLick(), parfaitClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                         bd=4)
    parfait_Btn.grid(row=1, column=0, pady=10, padx=17, ipadx=5, ipady=5)

    def sandwichClick1():
        global capresesandwichCount, capresesandwichPrice
        capresesandwichPrice = capresesandwichCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(capresesandwichCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=310, y=270, width=20, height=20)

    sandwich1 = PhotoImage(file="images/Continental/sandwichround.png")
    sandwich_Btn = Button(second_frame1, image=sandwich1, command=lambda: [sandwichClick(), sandwichClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    sandwich_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def waffleClick1():
        global waffleCount, wafflePrice
        wafflePrice = waffleCount * 180
        MochaLabel = Label(second_frame1, text=f"{str(waffleCount)}", font=('times new roman', 15),
                           bg='black', fg='lightyellow').place(x=102, y=516, width=20, height=20)

    waffle = PhotoImage(file="images/Continental/waffleround.png")
    waffle_Btn = Button(second_frame1, image=waffle, command=lambda: [waffleCLick(), waffleClick1()],
                        font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                        cursor='hand2', bd=4)
    waffle_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def pancakesClick1():
        global pancakesCount, pancakesPrice
        pancakesPrice = pancakesCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(pancakesCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=314, y=516, width=20, height=20)

    pancakes = PhotoImage(file="images/Continental/pancakesround.png")
    pancakes_Btn = Button(second_frame1, image=pancakes, command=lambda: [pancakesClick(), pancakesClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    pancakes_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


##BEVERAGES

# COFFEE
def coffeeBtn():
    coffee = Toplevel()
    coffee.title('Coffee')
    coffee.config(bg='light yellow')
    coffee.geometry('450x330+300+370')
    coffee.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, cappuccino, Americano, Espresso, Machiato, Latte, Mocha

    # defining the functions to increase each count by 1
    def cappuccinoCLick():
        global cappuccinoCount
        cappuccinoCount += 1

    def americanoCLick():
        global americanoCount
        americanoCount += 1

    def machiatoClick():
        global machiatoCount
        machiatoCount += 1

    def espressoClick():
        global espressoCount
        espressoCount += 1

    def latteClick():
        global latteCount
        latteCount += 1

    def mochaClick():
        global mochaCount
        mochaCount += 1

    def close():
        coffee.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(coffee, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Coffee', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, command=lambda: [close()], font=('times new roman', 30),
                        bg='lightyellow', fg='black', cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def cappuccinoClick1():
        global cappuccinoCount, cappuccinoPrice
        cappuccinoPrice = cappuccinoCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(cappuccinoCount)}", font=('times new roman', 15),
                           bg='lightyellow',
                           fg='black').place(x=100, y=270, width=20, height=20)

    cappuccino = PhotoImage(file="images/Coffee/cappuccino.png")
    cappuccino_Btn = Button(second_frame1, image=cappuccino, command=lambda: [cappuccinoCLick(), cappuccinoClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    cappuccino_Btn.grid(row=1, column=0, pady=10, padx=15)

    def americanoClick1():
        global americanoCount, americanoPrice
        americanoPrice = americanoCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(americanoCount)}", font=('times new roman', 15),
                           bg='lightyellow',
                           fg='black').place(x=304, y=270, width=20, height=20)

    Americano = PhotoImage(file="images/Coffee/americano.png")
    Americano_Btn = Button(second_frame1, image=Americano, command=lambda: [americanoCLick(), americanoClick1()],
                           font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                           bd=4)
    Americano_Btn.grid(row=1, column=1)

    def espressoClick1():
        global espressoCount, espressoPrice
        espressoPrice = espressoCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(espressoCount)}", font=('times new roman', 15),
                           bg='lightyellow',
                           fg='black').place(x=95, y=522, width=20, height=20)

    Espresso = PhotoImage(file="images/Coffee/espresso.png")
    Espresso_Btn = Button(second_frame1, image=Espresso, command=lambda: [espressoClick(), espressoClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    Espresso_Btn.grid(row=2, column=0, pady=48)

    def machiatoClick1():
        global machiatoCount, machiatoPrice
        machiatoPrice = machiatoCount * 170
        MochaLabel = Label(second_frame1, text=f"{str(machiatoCount)}", font=('times new roman', 15),
                           bg='lightyellow',
                           fg='black').place(x=304, y=522, width=20, height=20)

    Machiato = PhotoImage(file="images/Coffee/machiato.png")
    Machiato_Btn = Button(second_frame1, image=Machiato, command=lambda: [machiatoClick(), machiatoClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    Machiato_Btn.grid(row=2, column=1)

    def latteClick1():
        global latteCount, lattePrice
        lattePrice = latteCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(latteCount)}", font=('times new roman', 15), bg='lightyellow',
                           fg='black').place(x=100, y=775, width=20, height=20)

    Latte = PhotoImage(file="images/Coffee/latte.png")
    Latte_Btn = Button(second_frame1, image=Latte, command=lambda: [latteClick(), latteClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Latte_Btn.grid(row=3, column=0)

    def mochaClick1():
        global mochaCount, mochaPrice
        mochaPrice = mochaCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(mochaCount)}", font=('times new roman', 15), bg='lightyellow',
                           fg='black').place(x=304, y=775, width=20, height=20)

    Mocha = PhotoImage(file="images/Coffee/mocha.png")
    Mocha_Btn = Button(second_frame1, image=Mocha, command=lambda: [mochaClick(), mochaClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Mocha_Btn.grid(row=3, column=1, pady=10)


# TEA
def teaBtn():
    tea = Toplevel()
    tea.title('Tea')
    tea.config(bg='light yellow')
    tea.geometry('450x330+705+370')
    tea.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, green, chamomile, oolong, white, ginger, hibiscus, lavender, lemon

    # defining the functions to increase each count by 1
    def greenCLick():
        global greenTeaCount
        greenTeaCount += 1

    def chamomileCLick():
        global chamomileCount
        chamomileCount += 1

    def oolongClick():
        global oolongTeaCount
        oolongTeaCount += 1

    def gingerClick():
        global gingerTeaCount
        gingerTeaCount += 1

    def hibiscusClick():
        global hibiscusTeaCount
        hibiscusTeaCount += 1

    def whiteClick():
        global whiteTeaCount
        whiteTeaCount += 1

    def lavenderClick():
        global lavenderTeaCount
        lavenderTeaCount += 1

    def lemonClick():
        global lemonTeaCount
        lemonTeaCount += 1

    def close():
        tea.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(tea, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Tea', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, font=('times new roman', 30), bg='lightyellow', fg='black',
                        command=lambda: [close()],
                        cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def chamomileClick1():
        global chamomileCount, chamomilePrice
        chamomilePrice = chamomileCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(chamomileCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=253, width=20, height=20)

    chamomile = PhotoImage(file="images/Tea/Chammomile.png")
    chamomile_Btn = Button(second_frame1, image=chamomile, command=lambda: [chamomileCLick(), chamomileClick1()],
                           font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                           bd=4)
    chamomile_Btn.grid(row=1, column=0, pady=10, padx=30, ipadx=5, ipady=5)

    def oolongClick1():
        global oolongTeaCount, oolongTeaPrice
        oolongTeaPrice = oolongTeaCount * 130
        MochaLabel = Label(second_frame1, text=f"{str(oolongTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=253, width=20, height=20)

    oolong = PhotoImage(file="images/Tea/Oolong.png")
    oolong_Btn = Button(second_frame1, image=oolong, command=lambda: [oolongClick(), oolongClick1()],
                        font=('times new roman', 30),
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    oolong_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def whiteClick1():
        global whiteTeaCount, whiteTeaPrice
        whiteTeaPrice = whiteTeaCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(whiteTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=483, width=20, height=20)

    white = PhotoImage(file="images/Tea/white.png")
    white_Btn = Button(second_frame1, image=white, command=lambda: [whiteClick(), whiteClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    white_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def gingerClick1():
        global gingerTeaCount, gingerTeaPrice
        gingerTeaPrice = gingerTeaCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(gingerTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=483, width=20, height=20)

    ginger = PhotoImage(file="images/Tea/ginger.png")
    ginger_Btn = Button(second_frame1, image=ginger, command=lambda: [gingerClick(), gingerClick1()],
                        font=('times new roman', 30),
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    ginger_Btn.grid(row=2, column=1, ipadx=5, ipady=5)

    def hibiscusClick1():
        global hibiscusTeaCount, hibiscusTeaPrice
        hibiscusTeaPrice = hibiscusTeaCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(hibiscusTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=753, width=20, height=20)

    hibiscus = PhotoImage(file="images/Tea/hibiscus.png")
    hibiscus_Btn = Button(second_frame1, image=hibiscus, command=lambda: [hibiscusClick(), hibiscusClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    hibiscus_Btn.grid(row=3, column=0, ipadx=5, ipady=5)

    def lavenderClick1():
        global lavenderTeaCount, lavenderTeaPrice
        lavenderTeaPrice = lavenderTeaCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(lavenderTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=753, width=20, height=20)

    lavender = PhotoImage(file="images/Tea/lavender.png")
    Lavender_Btn = Button(second_frame1, image=lavender, command=lambda: [lavenderClick(), lavenderClick1()],
                          font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                          bd=4)
    Lavender_Btn.grid(row=3, column=1, pady=48, ipadx=5, ipady=5)

    def lemonClick1():
        global lemonTeaCount, lemonTeaPrice
        lemonTeaPrice = lemonTeaCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(lemonTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=108, y=983, width=20, height=20)

    lemon = PhotoImage(file="images/Tea/lemon.png")
    lemon_Btn = Button(second_frame1, image=lemon, command=lambda: [lemonClick(), lemonClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    lemon_Btn.grid(row=4, column=0, pady=10, ipadx=5, ipady=5)

    def greenClick1():
        global greenTeaCount, greenTeaPrice
        greenTeaPrice = greenTeaCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(greenTeaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=313, y=983, width=20, height=20)

    green = PhotoImage(file="images/Tea/greentea.png")
    green_Btn = Button(second_frame1, image=green, command=lambda: [greenCLick(), greenClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    green_Btn.grid(row=4, column=1, pady=10, ipadx=5, ipady=5)


# COLDDRINK
def colddrinkBtn():
    colddrink = Toplevel()
    colddrink.title('Cold Drink')
    colddrink.config(bg='light yellow')
    colddrink.geometry('470x330+1097+370')
    colddrink.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, pepsi, sevenup, coke, zero

    # defining the functions to increase each count by 1
    def pepsiCLick():
        global pepsiCount
        pepsiCount += 1

    def cokeCLick():
        global cokeCount
        cokeCount += 1

    def zeroClick():
        global zeroCount
        zeroCount += 1

    def sevenupClick():
        global sevenupCount
        sevenupCount += 1

    def close():
        colddrink.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(colddrink, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Cold Drinks', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, font=('times new roman', 30), bg='lightyellow', fg='black',
                        command=lambda: [close()],
                        cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def pepsiClick1():
        global pepsiCount, pepsiPrice
        pepsiPrice = pepsiCount * 80
        MochaLabel = Label(second_frame1, text=f"{str(pepsiCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=112, y=395, width=20, height=20)

    pepsi = PhotoImage(file="images/Coke/pepsiround.png")
    pepsi_Btn = Button(second_frame1, image=pepsi, command=lambda: [pepsiCLick(), pepsiClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    pepsi_Btn.grid(row=1, column=0, pady=10, padx=14, ipadx=5, ipady=5)

    def sevenupClick1():
        global sevenupCount, sevenupPrice
        sevenupPrice = sevenupCount * 80
        MochaLabel = Label(second_frame1, text=f"{str(sevenupCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=325, y=395, width=20, height=20)

    sevenup = PhotoImage(file="images/Coke/7upround.png")
    sevenup_Btn = Button(second_frame1, image=sevenup, command=lambda: [sevenupClick(), sevenupClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                         bd=4)
    sevenup_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def zeroClick1():
        global zeroCount, zeroPrice
        zeroPrice = zeroCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(zeroCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=112, y=773, width=20, height=20)

    zero = PhotoImage(file="images/Coke/0round.png")
    zero_Btn = Button(second_frame1, image=zero, command=lambda: [zeroClick(), zeroClick1()],
                      font=('times new roman', 30),
                      bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    zero_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def cokeClick1():
        global cokeCount, cokePrice
        cokePrice = cokeCount * 80
        MochaLabel = Label(second_frame1, text=f"{str(cokeCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=325, y=773, width=20, height=20)

    coke = PhotoImage(file="images/Coke/cokeround.png")
    coke_Btn = Button(second_frame1, image=coke, command=lambda: [cokeCLick(), cokeClick1()],
                      font=('times new roman', 30),
                      bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    coke_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# JUICE
def juiceBtn():
    juice = Toplevel()
    juice.title('Juices')
    juice.config(bg='light yellow')
    juice.geometry('470x330+300+370')
    juice.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, orangejuice, watermelon, lemonjuice, carrotjuice

    # defining the functions to increase each count by 1
    def carrotjuiceClick():
        global carrotjuiceCount
        carrotjuiceCount += 1

    def orangejuiceClick():
        global orangejuiceCount
        orangejuiceCount += 1

    def lemonjuiceClick():
        global lemonjuiceCount
        lemonjuiceCount += 1

    def watermelonClick():
        global watermelonCount
        watermelonCount += 1

    def close():
        juice.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(juice, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Juices', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, font=('times new roman', 30), bg='lightyellow', fg='black',
                        command=lambda: [close()],
                        cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def orangejuiceClick1():
        global orangejuiceCount, orangejuicePrice
        orangejuicePrice = orangejuiceCount * 90
        MochaLabel = Label(second_frame1, text=f"{str(orangejuiceCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=103, y=254, width=20, height=20)

    orangejuice = PhotoImage(file="images/Juice/orangejuiceround.png")
    orangejuice_Btn = Button(second_frame1, image=orangejuice, command=lambda: [orangejuiceClick(), orangejuiceClick1()],
                        font=('times new roman', 30),
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    orangejuice_Btn.grid(row=1, column=0, ipady=20, ipadx=20, padx=5, pady=5)

    def watermelonClick1():
        global watermelonCount, watermelonPrice
        watermelonPrice = watermelonCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(watermelonCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=327, y=254, width=20, height=20)

    watermelon = PhotoImage(file="images/Juice/watermelonjuiceround.png")
    watermelon_Btn = Button(second_frame1, image=watermelon,
                            command=lambda: [watermelonClick(), watermelonClick1()],
                            font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                            bd=4)
    watermelon_Btn.grid(row=1, column=1, ipadx=20, ipady=20, padx =5, pady=5)

    def lemonjuiceClick1():
        global lemonjuiceCount, lemonjuicePrice
        lemonjuicePrice = lemonjuiceCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(lemonjuiceCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=103, y=490, width=20, height=20)

    lemonjuice = PhotoImage(file="images/Juice/lemonjuiceround.png")
    lemonjuice_Btn = Button(second_frame1, image=lemonjuice,
                            command=lambda: [lemonjuiceClick(), lemonjuiceClick1()],
                            font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                            bd=4)
    lemonjuice_Btn.grid(row=2, column=0, ipadx=20, ipady=20, padx =5, pady=5)

    def carrotjuiceClick1():
        global carrotjuiceCount, carrotjuicePrice
        carrotjuicePrice = carrotjuiceCount * 145
        MochaLabel = Label(second_frame1, text=f"{str(carrotjuiceCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=327, y=490, width=20, height=20)

    carrotjuice = PhotoImage(file="images/Juice/carrotjuiceround.png")
    carrotjuice_Btn = Button(second_frame1, image=carrotjuice, command=lambda: [carrotjuiceClick(), carrotjuiceClick1()],
                           font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                           bd=4)
    carrotjuice_Btn.grid(row=2, column=1, ipadx=20, ipady=20, padx =5, pady=5)


# FRAPPE
def frappeBtn():
    frappe = Toplevel()
    frappe.title('Frappe')
    frappe.config(bg='light yellow')
    frappe.geometry('450x330+705+370')
    frappe.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, chocoFrappe, berryFrappe, caramelFrappe, orangeFrappe

    # defining the functions to increase each count by 1
    def chocoFrappeClick():
        global chocoFrappeCount
        chocoFrappeCount += 1

    def orangeFrappeClick():
        global orangeFrappeCount
        orangeFrappeCount += 1

    def caramelFrappeClick():
        global caramelFrappeCount
        caramelFrappeCount += 1

    def berryFrappeClick():
        global berryFrappeCount
        berryFrappeCount += 1

    def close():
        frappe.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(frappe, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Frappe', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, font=('times new roman', 30), bg='lightyellow', fg='black',
                        command=lambda: [close()],
                        cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def chocoFrappeClick1():
        global chocoFrappeCount, chocoFrappePrice
        chocoFrappePrice = chocoFrappeCount * 180
        MochaLabel = Label(second_frame1, text=f"{str(chocoFrappeCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=107, y=253, width=20, height=20)

        def updatePrice():
            global chocoFrappeCount, chocoFrappePrice, frankieTotal3
            frankieTotal3 = str(caramelFrappePrice + berryFrappePrice + chocoFrappePrice + orangeFrappePrice)
            print(frankieTotal3)
            if frankieTotal3 == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='Frappe', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=10, y=4, height=75, width=200)
            elif frankieTotal3 != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='Frappe Total', font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal3, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=160, height=50)

        updatePrice()

    chocoFrappe = PhotoImage(file="images/Frappe/chocoFrapperound.png")
    chocoFrappe_Btn = Label(second_frame1, image=chocoFrappe,
                            font=('times new roman', 30), anchor='c')
    chocoFrappe_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=1, ipady=1)

    def add3():
        global chocoFrappeCount
        chocoFrappeCount += 1

    def subtract3():
        global chocoFrappeCount
        if chocoFrappeCount > 0:
            chocoFrappeCount -= 1
        elif chocoFrappeCount <= 0:
            chocoFrappeCount = 0

    addImage2 = PhotoImage(file="images/Extras/addition.png")
    AddButton3 = Button(second_frame1, image=addImage2, font=('times new roman', 15), bg='lightyellow'
                        , anchor='c', cursor='hand2', bd=2, command=lambda: [add3(), chocoFrappeClick1()])
    AddButton3.image=addImage2
    AddButton3.place(x=128, y=253, width=20, height=20)

    subtractImage2 = PhotoImage(file="images/Extras/subtraction.png")
    SubtractButton3 = Button(second_frame1, image=subtractImage2, font=('times new roman', 15), bg='lightyellow'
                             , anchor='c', cursor='hand2', bd=2, command=lambda: [subtract3(), chocoFrappeClick1()])
    SubtractButton3.image=subtractImage2
    SubtractButton3.place(x=86, y=253, width=20, height=20)

    def orangeFrappeClick1():
        global orangeFrappeCount, orangeFrappePrice
        orangeFrappePrice = orangeFrappeCount * 150
        MochaLabel = Label(second_frame1, text=f"{str(orangeFrappeCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=320, y=253, width=20, height=20)

        def updatePrice():
            global orangeFrappeCount, orangeFrappePrice, frankieTotal4
            frankieTotal4 = str(caramelFrappePrice + berryFrappePrice + chocoFrappePrice + orangeFrappePrice)
            print(frankieTotal4)
            if frankieTotal4 == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='Frappe', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=10, y=4, height=75, width=200)
            elif frankieTotal4 != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='Frappe Total', font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal4, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=160, height=50)

        updatePrice()

    orangeFrappe = PhotoImage(file="images/Frappe/orangeFrapperound.png")
    orangeFrappe_Btn = Label(second_frame1, image=orangeFrappe,
                             font=('times new roman', 30), anchor='c')
    orangeFrappe_Btn.image = orangeFrappe
    orangeFrappe_Btn.grid(row=1, column=1, pady=10, padx=20, ipadx=1, ipady=1)

    def add4():
        global orangeFrappeCount
        orangeFrappeCount += 1

    def subtract4():
        global orangeFrappeCount
        if orangeFrappeCount > 0:
            orangeFrappeCount -= 1
        elif orangeFrappeCount <= 0:
            orangeFrappeCount = 0

    AddButton4 = Button(second_frame1, image=addImage2, font=('times new roman', 15), bg='lightyellow'
                        , anchor='c', cursor='hand2', bd=2, command=lambda: [add4(), orangeFrappeClick1()])
    AddButton4.place(x=341, y=253, width=20, height=20)

    SubtractButton4 = Button(second_frame1, image=subtractImage2, font=('times new roman', 15), bg='lightyellow'
                             , anchor='c', cursor='hand2', bd=2, command=lambda: [subtract4(), orangeFrappeClick1()])
    SubtractButton4.place(x=299, y=253, width=20, height=20)

    def berryFrappeClick1():
        global berryFrappeCount, berryFrappePrice
        berryFrappePrice = berryFrappeCount * 160
        MochaLabel = Label(second_frame1, text=f"{str(berryFrappeCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=107, y=517, width=20, height=20)

    berryFrappe = PhotoImage(file="images/Frappe/berryFrapperound.png")
    berryFrappe_Btn = Button(second_frame1, image=berryFrappe,
                             command=lambda: [berryFrappeClick(), berryFrappeClick1()],
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                             bd=4)
    berryFrappe_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def caramelFrappeClick1():
        global caramelFrappeCount, caramelFrappePrice
        caramelFrappePrice = caramelFrappeCount * 180
        MochaLabel = Label(second_frame1, text=f"{str(caramelFrappeCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=319, y=517, width=20, height=20)

    caramelFrappe = PhotoImage(file="images/Frappe/caramelFrapperound.png")
    caramelFrappe_Btn = Button(second_frame1, image=caramelFrappe,
                               command=lambda: [caramelFrappeClick(), caramelFrappeClick1()],
                               font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                               cursor='hand2',
                               bd=4)
    caramelFrappe_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


# ICECREAM
def iceCreamBtn():
    iceCream = Toplevel()
    iceCream.title('Ice Cream')
    iceCream.config(bg='light yellow')
    iceCream.geometry('450x330+1110+370')
    iceCream.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, vanilla, mango, butterscotch, blackcurrant

    # defining the functions to increase each count by 1
    def blackcurrantClick():
        global blackcurrantCount
        blackcurrantCount += 1

    def vanillaClick():
        global vanillaCount
        vanillaCount += 1

    def mangoClick():
        global mangoCount
        mangoCount += 1

    def butterscotchClick():
        global butterscotchCount
        butterscotchCount += 1

    def close():
        iceCream.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(iceCream, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='IceCream', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, font=('times new roman', 30), bg='lightyellow', fg='black',
                        command=lambda: [close()],
                        cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def vanillaClick1():
        global vanillaCount, vanillaPrice
        vanillaPrice = vanillaCount * 135
        MochaLabel = Label(second_frame1, text=f"{str(vanillaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=279, width=20, height=20)

    vanilla = PhotoImage(file="images/IceCream/vanillaround.png")
    vanilla_Btn = Button(second_frame1, image=vanilla, command=lambda: [vanillaClick(), vanillaClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                         bd=4)
    vanilla_Btn.grid(row=1, column=0, pady=10, padx=10, ipadx=5, ipady=5)

    def butterscotchClick1():
        global butterscotchCount, butterscotchPrice
        butterscotchPrice = butterscotchCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(butterscotchCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=310, y=279, width=20, height=20)

    butterscotch = PhotoImage(file="images/IceCream/butterscotchround.png")
    butterscotch_Btn = Button(second_frame1, image=butterscotch,
                              command=lambda: [butterscotchClick(), butterscotchClick1()],
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2',
                              bd=4)
    butterscotch_Btn.grid(row=1, column=1, ipadx=5, ipady=5)

    def blackcurrantClick1():
        global blackcurrantCount, blackcurrantPrice
        blackcurrantPrice = blackcurrantCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(blackcurrantCount)}", font=('times new roman', 15),
                           bg='black',
                           fg='lightyellow').place(x=102, y=536, width=20, height=20)

    blackcurrant = PhotoImage(file="images/IceCream/blackcurrantround.png")
    blackcurrant_Btn = Button(second_frame1, image=blackcurrant,
                              command=lambda: [blackcurrantClick(), blackcurrantClick1()],
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2',
                              bd=4)
    blackcurrant_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def mangoClick1():
        global mangoCount, mangoPrice
        mangoPrice = mangoCount * 130
        MochaLabel = Label(second_frame1, text=f"{str(mangoCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=310, y=536, width=20, height=20)

    mango = PhotoImage(file="images/IceCream/mangoround.png")
    mango_Btn = Button(second_frame1, image=mango, command=lambda: [mangoClick(), mangoClick1()],
                       font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    mango_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


##DESSERTS
def dessertBtn():
    dessert = Toplevel()
    dessert.title('Desserts')
    dessert.config(bg='light yellow')
    dessert.geometry('450x330+705+485')
    dessert.focus_force()
    unbindmenu1()

    # initialising the images to be used in the sandwich toplevel window
    global OKtoGo, rasgulla, rasmalai, gulabjamun, brownie

    # defining the functions to increase each count by 1
    def brownieClick():
        global brownieCount
        brownieCount += 1

    def rasgullaClick():
        global rasgullaCount
        rasgullaCount += 1

    def gulabJamunClick():
        global gulabjamunCount
        gulabjamunCount += 1

    def rasmalaiClick():
        global rasmalaiCount
        rasmalaiCount += 1

    def close():
        dessert.destroy()
        my_canvas1.unbind_all('<Configure>')
        my_canvas1.unbind_all("<MouseWheel>")
        bindmenu1()

    # Create A Main Frame
    main_frame1 = Frame(dessert, bg="lightyellow")
    main_frame1.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    Coffee_Lbl = Label(second_frame1, text='Desserts', font=('times new roman', 30, 'bold'), bg='lightyellow',
                       fg='black').grid(row=0, column=0, pady=15)

    OKtoGo = PhotoImage(file="images/Extras/Done.png")
    OKtoGo_Btn = Button(second_frame1, image=OKtoGo, font=('times new roman', 30), bg='lightyellow', fg='black',
                        command=lambda: [close()],
                        cursor='hand2')
    OKtoGo_Btn.grid(row=0, column=1, pady=10)

    def rasgullaClick1():
        global rasgullaCount, rasgullaPrice
        rasgullaPrice = rasgullaCount * 120
        MochaLabel = Label(second_frame1, text=f"{str(rasgullaCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=253, width=20, height=20)

        def updatePrice():
            global rasgullaCount, rasgullaPrice, frankieTotal5
            frankieTotal5 = str(rasgullaPrice + gulabjamunPrice + browniePrice + rasmalaiPrice + 0)
            print(frankieTotal5)
            if frankieTotal5 == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='Desserts', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=10, y=4, height=75, width=200)
            elif frankieTotal5 != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='Dessert Total',
                                                font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal5, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=160, height=50)

        updatePrice()

    rasgulla = PhotoImage(file="images/Dessert/rasgullaround.png")
    rasgulla_Btn = Label(second_frame1, image=rasgulla,
                         font=('times new roman', 30), anchor='c')
    rasgulla_Btn.image = rasgulla
    rasgulla_Btn.grid(row=1, column=0, pady=10, padx=20, ipadx=1, ipady=1)

    def add5():
        global rasgullaCount
        rasgullaCount += 1

    def subtract5():
        global rasgullaCount
        if rasgullaCount > 0:
            rasgullaCount -= 1
        elif rasgullaCount <= 0:
            rasgullaCount = 0

    addImage3 = PhotoImage(file="images/Extras/addition - Copy (2).png")
    AddButton5 = Button(second_frame1, image=addImage3, font=('times new roman', 15), bg='lightyellow'
                        , anchor='c', cursor='hand2', bd=2, command=lambda: [add5(), rasgullaClick1()])
    AddButton5.image = addImage3
    AddButton5.place(x=121, y=253, width=20, height=20)

    subtractImage3 = PhotoImage(file="images/Extras/subtraction - Copy (2).png")
    SubtractButton5 = Button(second_frame1, image=subtractImage3, font=('times new roman', 15), bg='lightyellow'
                             , anchor='c', cursor='hand2', bd=2, command=lambda: [subtract5(), rasgullaClick1()])
    SubtractButton5.image = subtractImage3
    SubtractButton5.place(x=79, y=253, width=20, height=20)

    def rasmalaiClick1():
        global rasmalaiCount, rasgullaPrice
        rasmalaiPrice = rasmalaiCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(rasmalaiCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=320, y=253, width=20, height=20)

        def updatePrice():
            global rasmalaiCount, rasgullaPrice, frankieTotal6
            frankieTotal6 = str(rasgullaPrice + gulabjamunPrice + browniePrice + rasmalaiPrice)
            print(frankieTotal6)
            if frankieTotal6 == '0':
                print(1)
                Coffee_Lbl = Label(second_frame1, text='Desserts', font=('times new roman', 30, 'bold'),
                                   bg='lightyellow',
                                   fg='black').place(x=10, y=4, height=75, width=200)
            elif frankieTotal6 != '0':
                print(2)
                priceShow_LblFrame = LabelFrame(second_frame1, text='Dessert Total',
                                                font=('times new roman', 13, 'bold')
                                                , relief=RIDGE, bd=2, bg='lightyellow', fg='red')
                priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
                priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal6, relief=RIDGE,
                                      font=('times new roman', 30, 'bold'),
                                      bg='lightblue', fg='black')
                priceShow_Lbl.place(x=10, y=0, width=160, height=50)

        updatePrice()

    rasmalai = PhotoImage(file="images/Dessert/rasmalairound.png")
    rasmalai_Btn = Label(second_frame1, image=rasmalai,
                         font=('times new roman', 30), anchor='c')
    rasmalai_Btn.image = rasmalai
    rasmalai_Btn.grid(row=1, column=1, pady=10, padx=20, ipadx=1, ipady=1)

    def add6():
        global rasmalaiCount
        rasmalaiCount += 1

    def subtract6():
        global rasmalaiCount
        if rasmalaiCount > 0:
            rasmalaiCount -= 1
        elif rasmalaiCount <= 0:
            rasmalaiCount = 0

    AddButton6 = Button(second_frame1, image=addImage3, font=('times new roman', 15), bg='lightyellow'
                        , anchor='c', cursor='hand2', bd=2, command=lambda: [add6(), rasmalaiClick1()])

    AddButton6.place(x=341, y=253, width=20, height=20)

    SubtractButton6 = Button(second_frame1, image=subtractImage3, font=('times new roman', 15), bg='lightyellow'
                             , anchor='c', cursor='hand2', bd=2, command=lambda: [subtract6(), rasmalaiClick1()])
    SubtractButton6.place(x=299, y=253, width=20, height=20)

    def gulabjamunClick1():
        global gulabjamunCount, gulabjamunPrice
        gulabjamunPrice = gulabjamunCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(gulabjamunCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=100, y=517, width=20, height=20)

    gulabjamun = PhotoImage(file="images/Dessert/gulabjamunround.png")
    gulabjamun_Btn = Button(second_frame1, image=gulabjamun,
                            command=lambda: [gulabJamunClick(), gulabjamunClick1()],
                            font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                            bd=4)
    gulabjamun_Btn.grid(row=2, column=0, pady=48, ipadx=5, ipady=5)

    def brownieClick1():
        global brownieCount, browniePrice
        browniePrice = brownieCount * 140
        MochaLabel = Label(second_frame1, text=f"{str(brownieCount)}", font=('times new roman', 15), bg='black',
                           fg='lightyellow').place(x=315, y=517, width=20, height=20)

    brownie = PhotoImage(file="images/Dessert/brownieround.png")
    brownie_Btn = Button(second_frame1, image=brownie, command=lambda: [brownieClick(), brownieClick1()],
                         font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                         bd=4)
    brownie_Btn.grid(row=2, column=1, ipadx=5, ipady=5)


##Creating the Dessert Tab:

def dessert():
    dessert = Toplevel(root)
    dessert.title('Menu Management System')
    dessert.config(bg='light yellow')
    dessert.geometry('1293x730+295+95')
    dessert.focus_force()

    # initialising the variables for pictures
    global coffee1, colddrink, juice, frappe, dessert1, icecream, logo_title, tea1

    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Title
    logo_title = PhotoImage(file='images/Extras/47418f210e99160c3b648cd840ff0f641.png')
    title = Label(dessert, text=' Menu Management System', image=logo_title, compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=2,
                                                                                                relwidth=1,
                                                                                                height=65)

    # Underline 2
    underline2 = Label(dessert,
                       text='                                                                                                                                                             ',
                       font=font1, bg='lightyellow', fg='black').place(x=0, y=65, relwidth=1)

    # Create A Main Frame
    main_frame2 = Frame(dessert, bg="lightyellow")
    main_frame2.place(x=0, y=102, relwidth=1, height=619)

    # Create A Canvas
    global my_canvas2
    my_canvas2 = Canvas(main_frame2, bg="lightyellow")
    my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar2 = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
    my_canvas2.bind_all('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame2 = Frame(my_canvas2, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas2.create_window((0, 0), window=second_frame2, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas2.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas2.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    # Beverages

    Beverages_Lbl = Label(second_frame2, text='Beverages', font=('courier', 40, 'bold'), bg='lightyellow',
                          fg='black').grid(row=0, column=1, padx=0, ipady=20)
    Beverages_Lbl = Label(second_frame2, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                          fg='black').grid(row=0, column=2, padx=0, ipady=20)
    Beverages_Lbl = Label(second_frame2, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                          fg='black').grid(row=0, column=0, padx=0, ipady=20)

    coffee1 = PhotoImage(file="images/Coffee/Re_Coffee.png")
    Coffee_Btn = Button(second_frame2, image=coffee1, command=coffeeBtn, font=('times new roman', 30),
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Coffee_Btn.grid(row=1, column=0, pady=50, ipady=20, ipadx=30, padx=70)

    tea1 = PhotoImage(file="images/Tea/Tea.png")
    Tea_Btn = Button(second_frame2, image=tea1, command=teaBtn, font=('times new roman', 30), bg='lightyellow',
                     anchor='c', fg='black', cursor='hand2', bd=4)
    Tea_Btn.grid(row=1, column=1, pady=50, ipady=20, ipadx=30, padx=70)

    colddrink = PhotoImage(file="images/Coke/Cold Drink.png")
    ColdDrink_Btn = Button(second_frame2, image=colddrink, command=colddrinkBtn, font=('times new roman', 30),
                           bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    ColdDrink_Btn.grid(row=1, column=2, pady=50, ipady=20, ipadx=30, padx=70)

    juice = PhotoImage(file="images/Juice/Juices.png")
    Juice_Btn = Button(second_frame2, image=juice, command=juiceBtn, font=('times new roman', 30),
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Juice_Btn.grid(row=2, column=0, pady=0, ipady=20, ipadx=30, padx=70)

    frappe = PhotoImage(file="images/Frappe/Frappe.png")
    Frappe_Btn = Button(second_frame2, image=frappe, command=frappeBtn, font=('times new roman', 30),
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Frappe_Btn.grid(row=2, column=1, pady=0, ipady=20, ipadx=30, padx=70)

    icecream = PhotoImage(file="images/IceCream/IceCream.png")
    IceCream_Btn = Button(second_frame2, image=icecream, command=iceCreamBtn, font=('times new roman', 30),
                          bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    IceCream_Btn.grid(row=2, column=2, pady=0, ipady=20, ipadx=30, padx=70)

    # Desserts

    Desserts_Lbl = Label(second_frame2, text='Sweets', font=('courier', 40, 'bold'), bg='lightyellow',
                         fg='black').grid(
        row=3, column=1, padx=0, ipady=20, pady=50)
    Desserts_Lbl = Label(second_frame2, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                         fg='black').grid(row=3, column=2, padx=0, ipady=20, pady=50)
    Desserts_Lbl = Label(second_frame2, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                         fg='black').grid(row=3, column=0, padx=0, ipady=20, pady=50)

    dessert1 = PhotoImage(file="images/Dessert/Desserts.png")
    Dessert_Btn = Button(second_frame2, image=dessert1, font=('times new roman', 30), command=dessertBtn,
                         bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Dessert_Btn.grid(row=4, column=1, pady=0, ipady=20, ipadx=30, padx=70)


def _on_mouse_wheel1(event):
    global my_canvas2
    my_canvas2.yview_scroll(-1 * int((event.delta / 120)), "units")


def unbindmenu1():
    global my_canvas2
    my_canvas2.unbind_all('<Configure>')
    my_canvas2.unbind_all('<MouseWheel>')


def bindmenu1():
    global my_canvas2
    my_canvas2.bind_all('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))
    my_canvas2.bind_all("<MouseWheel>", _on_mouse_wheel1)


##Creating the Menu Tab:
def menu():
    menu = Toplevel(root)
    menu.title('Menu Management System')
    menu.config(bg='light yellow')
    menu.geometry('1293x730+295+95')
    menu.focus_force()

    # initialising the variables for photos of menu tab
    global logo_title1, subway, thali, continental, frankie, sandwich, pasta, vegcurry, indianbreads, northindian, southindian, pizza, burger
    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Title
    logo_title1 = PhotoImage(file='images/Extras/Removal-1791.png')
    title = Label(menu, text=' Menu Management System', image=logo_title1, compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=6,
                                                                                                relwidth=1,
                                                                                                height=70)

    # Underline 2
    underline2 = Label(menu,
                       text='                                                                                                                                                             ',
                       font=font1, bg='lightyellow', fg='black').place(x=0, y=65, relwidth=1)

    # Create A Main Frame
    main_frame1 = Frame(menu, bg="lightyellow")
    main_frame1.place(x=0, y=102, width=1290, height=619)

    # Create A Canvas
    global my_canvas1
    my_canvas1 = Canvas(main_frame1, bg="lightyellow")
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas1, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas1.create_window((0, 0), window=second_frame, anchor="nw")

    # Using Mouse Wheel To Scroll
    def _on_mouse_wheel(event):
        my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")

    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Creating The Menu

    # Starters

    Starter_Lbl = Label(second_frame, text='Starters', font=('courier', 40, 'bold'), bg='lightyellow',
                        fg='black').grid(
        row=0, column=1, padx=0, ipady=20)
    Starter_Lbl = Label(second_frame, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                        fg='black').grid(row=0, column=2, padx=0, ipady=20)
    Starter_Lbl = Label(second_frame, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                        fg='black').grid(row=0, column=0, padx=0, ipady=20)

    sandwich = PhotoImage(file="images/Sandwiches/Sandwich.png")
    Sandwich_Btn = Button(second_frame, image=sandwich, command=sandwichBtn, bg='lightyellow', anchor='c',
                          fg='black', cursor='hand2', bd=4)
    Sandwich_Btn.grid(row=1, column=0, pady=50, ipady=20, ipadx=30, padx=70)

    frankie = PhotoImage(file="images/Frankie/Frankie.png")
    Frankie_Btn = Button(second_frame, image=frankie, bg='lightyellow', anchor='c', command=frankieBtn,
                         fg='black', cursor='hand2', bd=4)
    Frankie_Btn.grid(row=1, column=1, pady=50, ipady=20, ipadx=30, padx=70)

    subway = PhotoImage(file="images/Subway/Subway.png")
    Subway_Btn = Button(second_frame, image=subway, font=('times new roman', 30), command=SubwayBtn,
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Subway_Btn.grid(row=1, column=2, pady=50, ipady=20, ipadx=30, padx=70)

    burger = PhotoImage(file="images/Burger/Burger.png")
    Burger_Btn = Button(second_frame, image=burger, font=('times new roman', 30), command=BurgerBtn,
                        bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Burger_Btn.grid(row=2, column=0, pady=0, ipady=20, ipadx=30, padx=70)

    pizza = PhotoImage(file="images/Pizza/Pizza.png")
    Pizza_Btn = Button(second_frame, image=pizza, font=('times new roman', 30), command=PizzaBtn,
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Pizza_Btn.grid(row=2, column=1, pady=0, ipady=20, ipadx=30, padx=70)

    pasta = PhotoImage(file="images/Pasta/Pasta.png")
    Pasta_Btn = Button(second_frame, image=pasta, font=('times new roman', 30), command=pastaBtn,
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Pasta_Btn.grid(row=2, column=2, pady=0, ipady=20, ipadx=30, padx=70)

    # Main Course

    MainCourse_Lbl = Label(second_frame, text='Main Course', font=('courier', 40, 'bold'), bg='lightyellow',
                           fg='black').grid(row=4, column=1, padx=0, ipady=20, pady=50)
    MainCourse_Lbl = Label(second_frame, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                           fg='black').grid(row=4, column=2, padx=0, ipady=20, pady=50)
    MainCourse_Lbl = Label(second_frame, text='---------', font=('courier', 40, 'bold'), bg='lightyellow',
                           fg='black').grid(row=4, column=0, padx=0, ipady=20, pady=50)

    southindian = PhotoImage(file="images/SouthIndian/SouthIndian.png")
    SouthIndian_Btn = Button(second_frame, image=southindian,
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                             command=southIndianBtn,
                             bd=4)
    SouthIndian_Btn.grid(row=5, column=0, pady=0, ipady=20, ipadx=30, padx=70)

    vegcurry = PhotoImage(file="images/Curries/VegCurry.png")
    VegCurry_Btn = Button(second_frame, image=vegcurry, font=('times new roman', 30), command=curryBtn,
                          bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    VegCurry_Btn.grid(row=5, column=1, pady=0, ipady=20, ipadx=30, padx=70)

    indianbreads = PhotoImage(file="images/Roti/IndianBreads.png")
    IndianBreads_Btn = Button(second_frame, image=indianbreads,
                              font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black',
                              cursor='hand2', command=rotiBtn,
                              bd=4)
    IndianBreads_Btn.grid(row=5, column=2, pady=0, ipady=20, ipadx=30, padx=70)

    northindian = PhotoImage(file="images/NorthIndian/NorthIndian.png")
    NorthIndian_Btn = Button(second_frame, image=northindian,
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                             command=northindianBtn,
                             bd=4)
    NorthIndian_Btn.grid(row=6, column=0, pady=50, ipady=20, ipadx=30, padx=70)

    thali = PhotoImage(file="images/Thali/Thali.png")
    Thali_Btn = Button(second_frame, image=thali, font=('times new roman', 30), command=thaliBtn,
                       bg='lightyellow', anchor='c', fg='black', cursor='hand2', bd=4)
    Thali_Btn.grid(row=6, column=1, pady=50, ipady=20, ipadx=30, padx=70)

    continental = PhotoImage(file="images/Continental/Continental.png")
    Continental_Btn = Button(second_frame, image=continental,
                             font=('times new roman', 30), bg='lightyellow', anchor='c', fg='black', cursor='hand2',
                             command=continentalBtn,
                             bd=4)
    Continental_Btn.grid(row=6, column=2, pady=50, ipady=20, ipadx=30, padx=70)


def _on_mouse_wheel(event):
    global my_canvas1
    my_canvas1.yview_scroll(-1 * int((event.delta / 120)), "units")


def unbindmenu():
    global my_canvas1
    my_canvas1.unbind_all('<Configure>')
    my_canvas1.unbind_all('<MouseWheel>')


def bindmenu():
    global my_canvas1
    my_canvas1.bind_all('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))
    my_canvas1.bind_all("<MouseWheel>", _on_mouse_wheel)


##Creating The Employee Tab

def employee():
    employee = Toplevel(root)
    employee.title('Employee Management System')
    employee.config(bg='light yellow')
    employee.geometry('1293x730+295+95')
    employee.focus_force()

    # initialising the variables for images in Employee Tab
    global logo_title, SearchBox_Btn_image

    # Creating the functions
    def counter():
        counter_tuple = 0
        counter_tuple1 = 0
        tuple = (
            var_empID.get(), var_Email.get(), var_Password.get(), var_Salary.get(), var_DOJ.get(),
            var_Name.get())
        for i in range(0, 6):
            if (tuple[i] == ""):
                counter_tuple += 1
            else:
                continue

        tuple2 = (var_Designation.get(), var_Gender.get(), var_Branch.get())
        for i in range(0, 3):
            if (tuple2[i] == "Select"):
                counter_tuple1 += 1
            else:
                continue

        global finalcount_str, finalcount
        finalcount = counter_tuple + counter_tuple1
        finalcount_str = str(finalcount)

    def databaseOpen():
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            cur.execute('select * from employee')
            rows = cur.fetchall()
            database.delete(*database.get_children())
            for row in rows:
                database.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=employee)

    def save():
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            if (var_empID.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Employee ID Required", parent=employee)
            elif (var_empID.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=employee)
            elif (var_Password.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Password Required", parent=employee)
            elif (var_Password.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Email.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Email Required", parent=employee)
            elif (var_Email.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Gender.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Gender Required", parent=employee)
            elif (var_Gender.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Branch.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Branch Required", parent=employee)
            elif (var_Branch.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_DOJ.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Date Of Join Required", parent=employee)
            elif (var_DOJ.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Designation.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Designation Required", parent=employee)
            elif (var_Designation.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Salary.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Salary Required", parent=employee)
            elif (var_Salary.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Name.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Name Required", parent=employee)
            elif (var_Name.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)

            elif (var_Password.get() != ''):
                cur.execute('Select * from employee where pswd=?', (var_Password.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("SQL Database", "This is an already assigned Password\nPlease Try Another",
                                         parent=employee)
                else:
                    cur.execute('Select * from employee where empID=?', (var_empID.get(),))
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror("SQL Database",
                                             "This is an already assigned EmpID\nPlease Try Another",
                                             parent=employee)
                    else:
                        cur.execute(
                            'Insert into employee(empID,name,DOJ,salary,email,pswd,gender,dsgntn,branch) values(?,?,?,?,?,?,?,?,?)',
                            (
                                var_empID.get(),
                                var_Name.get(),
                                var_DOJ.get(),
                                var_Salary.get(),
                                var_Email.get(),
                                var_Password.get(),
                                var_Gender.get(),
                                var_Designation.get(),
                                var_Branch.get(),
                            ))
                        con.commit()
                        messagebox.showinfo('SQL Database', 'Employee Details Added Successfully', parent=employee)
                        databaseOpen()


        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=employee)

    def update():
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            if (var_empID.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Employee ID Required", parent=employee)
            elif (var_empID.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=employee)
            elif (var_Password.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Password Required", parent=employee)
            elif (var_Password.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Email.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Email Required", parent=employee)
            elif (var_Email.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Gender.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Gender Required", parent=employee)
            elif (var_Gender.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Branch.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Branch Required", parent=employee)
            elif (var_Branch.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_DOJ.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Date Of Join Required", parent=employee)
            elif (var_DOJ.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Designation.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Designation Required", parent=employee)
            elif (var_Designation.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Salary.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Salary Required", parent=employee)
            elif (var_Salary.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Name.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Name Required", parent=employee)
            elif (var_Name.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)

            else:
                cur.execute('Select * from employee where empID=?', (var_empID.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("SQL Database", "Invalid Employee ID", parent=employee)
                else:
                    cur.execute(
                        'Update employee set name=?,DOJ=?,salary=?,email=?,pswd=?,gender=?,dsgntn=?,branch=? where empID=?',
                        (
                            var_Name.get(),
                            var_DOJ.get(),
                            var_Salary.get(),
                            var_Email.get(),
                            var_Password.get(),
                            var_Gender.get(),
                            var_Designation.get(),
                            var_Branch.get(),
                            var_empID.get(),
                        ))
                    con.commit()
                    messagebox.showinfo('SQL Database', 'Employee Details Updated Successfully', parent=employee)
                    databaseOpen()

        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=employee)

    def delete():
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            if (var_empID.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Employee ID Required", parent=employee)
            elif (var_empID.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=employee)
            elif (var_Password.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Password Required", parent=employee)
            elif (var_Password.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Email.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Email Required", parent=employee)
            elif (var_Email.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Gender.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Gender Required", parent=employee)
            elif (var_Gender.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Branch.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Branch Required", parent=employee)
            elif (var_Branch.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_DOJ.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Date Of Join Required", parent=employee)
            elif (var_DOJ.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Designation.get() == "Select" and finalcount == 1):
                messagebox.showerror('SQL Database', "Designation Required", parent=employee)
            elif (var_Designation.get() != 'Select' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Salary.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Salary Required", parent=employee)
            elif (var_Salary.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)
            elif (var_Name.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Name Required", parent=employee)
            elif (var_Name.get() != '' and finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount)} Fields Required", parent=employee)

            else:
                cur.execute('Select * from employee where empID=?', (var_empID.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("SQL Database", "Invalid Employee ID", parent=employee)
                else:
                    op = messagebox.askyesno('SQL Database', "Do You Want To Delete The Selected Record?",
                                             parent=employee)
                    if op == True:
                        cur.execute('delete from employee where empID=?', (var_empID.get(),))
                        con.commit()
                        messagebox.showinfo('SQL Database', 'Employee Details Deleted Successfully',
                                            parent=employee)
                        databaseOpen()

        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=employee)

    def passData(ev):
        f = database.focus()
        content = (database.item(f))
        row = content['values']
        var_empID.set(row[0])
        var_Salary.set(row[3])
        var_Email.set(row[4])
        var_Password.set(row[5])
        var_Gender.set(row[6])
        var_Designation.set(row[7])
        var_Branch.set(row[8])
        var_DOJ.set(row[2])
        var_Name.set(row[1])

    def clear():
        var_empID.set('')
        var_Salary.set('')
        var_Email.set('')
        var_Password.set('')
        var_Gender.set('Select')
        var_Designation.set('Select')
        var_Branch.set('Select')
        var_DOJ.set('')
        var_Name.set('')
        var_searchTxt.set('')
        var_searchBy.set('Select')

    def searchBar():
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:

            if (var_searchBy.get() == "Select"):
                messagebox.showerror("SQL Database", "Please Specify The Search Parameter", parent=employee)

            elif var_searchBy.get() == "Branch":
                cur.execute('select * from employee where branch=?', (var_searchTxt.get(),))
                rows = cur.fetchall()
                database.delete(*database.get_children())
                for row in rows:
                    database.insert("", END, values=row)
                con.commit()
            elif var_searchBy.get() == "Salary":
                cur.execute('select * from employee where salary=?', (var_searchTxt.get(),))
                rows = cur.fetchall()
                database.delete(*database.get_children())
                for row in rows:
                    database.insert("", END, values=row)
                con.commit()
            elif var_searchBy.get() == "Designation":
                cur.execute('select * from employee where dsgntn=?', (var_searchTxt.get(),))
                rows = cur.fetchall()
                database.delete(*database.get_children())
                for row in rows:
                    database.insert("", END, values=row)
                con.commit()
            elif var_searchBy.get() == "Gender":
                cur.execute('select * from employee where gender=?', (var_searchTxt.get(),))
                rows = cur.fetchall()
                database.delete(*database.get_children())
                for row in rows:
                    database.insert("", END, values=row)
                con.commit()
            elif var_searchBy.get() == "Emp ID":
                cur.execute('select * from employee where empID=?', (var_searchTxt.get(),))
                rows = cur.fetchall()
                database.delete(*database.get_children())
                for row in rows:
                    database.insert("", END, values=row)
                con.commit()
            elif var_searchBy.get() == "Name":
                cur.execute('select * from employee where name=?', (var_searchTxt.get(),))
                rows = cur.fetchall()
                database.delete(*database.get_children())
                for row in rows:
                    database.insert("", END, values=row)
                con.commit()
            else:
                print('hello')

        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=employee)

    # Declaring Search Variables
    var_searchBy = StringVar()
    var_searchTxt = StringVar()

    # Declaring Employee Detail Variables
    var_empID = StringVar()
    var_Salary = StringVar()
    var_Email = StringVar()
    var_Password = StringVar()
    var_Gender = StringVar()
    var_Designation = StringVar()
    var_Branch = StringVar()
    var_DOJ = StringVar()
    var_Name = StringVar()

    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Title
    logo_title = PhotoImage(file='images/Extras/6609538_preview1.png')
    title = Label(employee, text=' Employee Management System', image=logo_title, compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=6,
                                                                                                relwidth=1,
                                                                                                height=70)

    # Underline 1
    underline = Label(employee,
                      text='                                                                                                                                                             ',
                      font=font1, bg='lightyellow', fg='black').place(x=0, y=64, width=1400)

    # Search Label
    SearchFrame = LabelFrame(employee, text="Search Database", font=('goudy old style', 12, 'bold'), bd=2,
                             relief=RAISED,
                             bg='light yellow', fg='red')
    SearchFrame.place(x=250, y=120, width=800, height=70)

    # Search Drop-Down Menu
    DropDown_SearchFrame = ttk.Combobox(SearchFrame,
                                        values=(
                                            'Select', 'Branch', 'Salary', 'Designation', 'Gender', 'Name',
                                            'Emp ID'),
                                        state='readonly', textvariable=var_searchBy, justify=CENTER,
                                        font=('verdana', 15))
    DropDown_SearchFrame.place(x=10, y=5, width=180)
    DropDown_SearchFrame.current(0)

    # Search Bar
    SearchBox = Entry(SearchFrame, textvariable=var_searchTxt, font=('goudy old style', 23, "bold"),
                      bg='NavajoWhite2',
                      fg='dim gray', relief=GROOVE, bd=1)
    SearchBox.place(x=220, y=5, width=450, height=31)

    # Search Button
    SearchBox_Btn_image = PhotoImage(file='images/Extras/[removal.ai]_tmp-6111873d2a67c.png')
    SearchBox_Btn = Button(SearchFrame, command=lambda: [searchBar()], image=SearchBox_Btn_image, compound=LEFT,
                           relief=GROOVE, cursor='hand2', bd=2, anchor='c')
    SearchBox_Btn.place(x=720, y=5, width=50, height=31)

    # Underline 2
    underline2 = Label(employee,
                       text='                                                                                                                                                             ',
                       font=font1, bg='lightyellow', fg='black').place(x=0, y=189, width=1400)

    # Database
    database_Frame = Frame(employee, bd=3, relief=RIDGE)
    database_Frame.place(x=-2, y=226, relwidth=1, height=200)

    # ScrollBars
    scroll_xdir = Scrollbar(database_Frame, orient=HORIZONTAL)
    scroll_ydir = Scrollbar(database_Frame, orient=VERTICAL)

    # Table Creation
    database = ttk.Treeview(database_Frame,
                            columns=(
                                'empID', 'name', 'DOJ', 'salary', 'email', 'pswd', 'gender', 'dsgntn', 'branch'),
                            yscrollcommand=scroll_ydir.set, xscrollcommand=scroll_xdir.set)
    scroll_xdir.pack(side=BOTTOM, fill=X)
    scroll_ydir.pack(side=RIGHT, fill=Y)
    scroll_ydir.config(command=database.yview)
    scroll_xdir.config(command=database.xview)
    database.heading('empID', text="EmpID")
    database.heading('name', text="Name")
    database.heading('DOJ', text="DOJ")
    database.heading('salary', text="Salary")
    database.heading('email', text="Email")
    database.heading('pswd', text="Password")
    database.heading('gender', text="Gender")
    database.heading('dsgntn', text="Designation")
    database.heading('branch', text="Branch")

    database['show'] = 'headings'

    database.column('empID', width=100)
    database.column('name', width=130)
    database.column('DOJ', width=100)
    database.column('salary', width=100)
    database.column('email', width=100)
    database.column('pswd', width=100)
    database.column('gender', width=100)
    database.column('dsgntn', width=100)
    database.column('branch', width=100)

    database.pack(fill=BOTH, expand=1)
    database.bind('<ButtonRelease-1>', passData)

    databaseOpen()

    # Add Employee
    empID_Lbl = Label(employee, text='EmployeeID', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                      fg='black').place(x=-20, y=444, width=250, height=60)
    empID_Entry = Entry(employee, textvariable=var_empID, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                        bg='white', fg='black').place(x=230, y=449, width=150, height=50)

    Name_Lbl = Label(employee, text='Name', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                     fg='black').place(
        x=380, y=444, width=250, height=60)
    Name_Entry = Entry(employee, textvariable=var_Name, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                       bg='white', fg='black').place(x=570, y=449, width=150, height=50)

    Salary_Lbl = Label(employee, text='Salary', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                       fg='black').place(
        x=-20, y=544, width=250, height=60)
    Salary_Entry = Entry(employee, textvariable=var_Salary, font=('goudy old style', 15, 'bold'), bd=2,
                         relief=SUNKEN,
                         bg='white', fg='black').place(x=230, y=549, width=150, height=50)

    Branch_Lbl = Label(employee, text='Branch ', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                       fg='black').place(
        x=380, y=544, width=250, height=60)
    Branch_Combobox = ttk.Combobox(employee, textvariable=var_Branch,
                                   values=('Select', 'Mumbai', 'Bangalore', 'Chennai'), state='readonly',
                                   justify=CENTER,
                                   font=('verdana', 15))
    Branch_Combobox.place(x=570, y=560, width=150)
    Branch_Combobox.current(0)

    Designation_Lbl = Label(employee, text='Designation', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                            fg='black').place(x=-20, y=644, width=250, height=60)
    Designation_Combobox = ttk.Combobox(employee, textvariable=var_Designation,
                                        values=('Select', 'Admin', 'Employee'), state='readonly', justify=CENTER,
                                        font=('verdana', 15))
    Designation_Combobox.place(x=230, y=660, width=150)
    Designation_Combobox.current(0)

    Gender_Lbl = Label(employee, text='Gender ', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                       fg='black').place(
        x=380, y=644, width=250, height=60)
    Gender_Combobox = ttk.Combobox(employee, textvariable=var_Gender, values=('Select', 'Male', 'Female', 'Other'),
                                   state='readonly', justify=CENTER, font=('verdana', 15))
    Gender_Combobox.place(x=570, y=660, width=150)
    Gender_Combobox.current(0)

    Email_Lbl = Label(employee, text='Email ID', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                      fg='black').place(
        x=720, y=444, width=250, height=60)
    empID_Entry = Entry(employee, textvariable=var_Email, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                        bg='white', fg='black').place(x=940, y=449, width=150, height=50)

    Password_Lbl = Label(employee, text='Password', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                         fg='black').place(x=720, y=544, width=250, height=60)
    empID_Entry = Entry(employee, textvariable=var_Password, font=('goudy old style', 15, 'bold'), bd=2,
                        relief=SUNKEN, bg='white', fg='black').place(x=940, y=549, width=150, height=50)

    DOJ_Lbl = Label(employee, text='DOJ', font=('goudy old style', 30, 'bold'), bg='lightyellow', fg='black').place(
        x=720,
        y=644,
        width=250,
        height=60)
    DOJ_Entry = Entry(employee, textvariable=var_DOJ, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                      bg='white', fg='black').place(x=940, y=649, width=150, height=50)

    # Buttons For Adding Employee Details
    Save_Btn = Button(employee, text='Save', command=lambda: [counter(), save()], cursor='hand2',
                      font=('helvetica', 30), bg='IndianRed2', fg='black', bd=4, relief=RAISED).place(x=1150, y=444,
                                                                                                      width=140,
                                                                                                      height=45)
    Update_Btn = Button(employee, text='Update', command=lambda: [counter(), update()], cursor='hand2',
                        font=('helvetica', 30), bg='gold', fg='black', bd=4, relief=RAISED).place(x=1150, y=524,
                                                                                                  width=140,
                                                                                                  height=46)
    Delete_Btn = Button(employee, text='Delete', command=lambda: [counter(), delete()], cursor='hand2',
                        font=('helvetica', 30), bg='OliveDrab2', fg='black', bd=4, relief=RAISED).place(x=1150,
                                                                                                        y=604,
                                                                                                        width=140,
                                                                                                        height=45)
    Clear_Btn = Button(employee, text='Clear', command=lambda: [clear()], cursor='hand2', font=('helvetica', 30),
                       bg='DodgerBlue', fg='black', bd=4, relief=RAISED).place(x=1150, y=684, width=140, height=45)


#Creating the Support Tab:
def support():
    support = Toplevel(root)
    support.title('Support Management System')
    support.config(bg='light yellow')
    support.geometry('1293x730+295+95')
    support.focus_force()

    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Initialising global picture variables
    global logo_title3



    # Title
    logo_title3 = PhotoImage(file='images/Extras/customer-care-87-11313951.png')
    title = Label(support, text=' Support Management System', image=logo_title3, compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=4,
                                                                                                relwidth=1,
                                                                                                height=70)

    # Underline 1
    underline = Label(support,
                      text='                                                                                                                                                             ',
                      font=font1, bg='lightyellow', fg='black').place(x=0, y=63, width=1400)


    var_searchTxt1 = StringVar()
    var_orderIDmention = StringVar()
    var_refundAmount = IntVar()

    def cleartxt():
        var_searchTxt1.set('')

    def cleartxt1():
        var_orderIDmention.set('')

    # PDF VIEWER
    def pdfViewer():
        global fileSearch
        pdf_Frame = Frame(support, bd=3, relief=RIDGE)
        pdf_Frame.place(x=700, y=100, width=600, height=650)

        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(pdf_Frame,
                         pdf_location=f"{fileSearch}",
                         width=100, height=120)
        v2.pack()

    # Search Label
    SearchFrame = LabelFrame(support, text="Search For File", font=('goudy old style', 12, 'bold'), bd=2,
                             relief=RAISED,
                             bg='light yellow', fg='red')
    SearchFrame.place(x=4, y=100, width=697, height=80)

    # Search Button
    SearchBox_Btn_image1 = PhotoImage(file='images/Extras/wrong-black-wrong-icon-symbol-logo-trademark-rug-transparent-png-822781.png')
    SearchBox_Btn1 = Button(SearchFrame, command=lambda:[cleartxt()], image=SearchBox_Btn_image1, compound=LEFT,
                           relief=GROOVE, cursor='hand2', bd=2, anchor='c')
    SearchBox_Btn1.place(x=45, y=5, width=60, height=40)
    SearchBox_Btn1.image=SearchBox_Btn_image1

    # Search Bar
    SearchBox = Entry(SearchFrame, textvariable=var_searchTxt1, font=('goudy old style', 14),
                      bg='NavajoWhite2',
                      fg='dim gray', relief=GROOVE, bd=1)
    SearchBox.place(x=110, y=5, width=450, height=40)

    # Search Button
    SearchBox_Btn_image = PhotoImage(file='images/Extras/[removal.ai]_tmp-6111873d2a67c - Copy.png')
    SearchBox_Btn = Button(SearchFrame, command=lambda: [pdfViewer()], image=SearchBox_Btn_image, compound=LEFT,
                           relief=GROOVE, cursor='hand2', bd=2, anchor='c')
    SearchBox_Btn.place(x=565, y=5, width=60, height=40)
    SearchBox_Btn.image=SearchBox_Btn_image


    def passData1(ev):
        global fileSearch,fileSearch3
        f = database.focus()
        content = (database.item(f))
        row = content['values']
        fileSearch = row[3]+row[0]
        fileSearch1=list(fileSearch)
        fileSearch1=fileSearch1[67:87]
        fileSearch3=''.join(fileSearch1)
        fileSearch2=fileSearch3+'.pdf'

        var_searchTxt1.set(fileSearch2)

    def refundAmount():
        refundamt.config(state='normal')


    def messagebox1():

        op=messagebox.askyesno('Refund Mechanism', "Are you sure you want to issue refund?",
                            parent=support)
        if op==True:
            username = "eatify.python@gmail.com"
            pswd = "Eatify@Python3"

            url = "https://dashboard.razorpay.com/#/access/signin"

            driver = webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver")

            driver.get(url)

            # EmailID
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "Email or Mobile Number"))
            )
            element.send_keys(username)
            driver.find_element_by_xpath("//button[@type='submit']").click()

            # Password
            driver.find_element_by_id("Password").send_keys(pswd)

            # Login Button
            driver.find_element_by_xpath("//button[@type='submit']").click()

            # Transactions Button Click
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'×')]")))
            element.click()
            driver.find_element_by_xpath("//a[contains(@class,'NavLink')][contains(text(),'Transactions')]").click()

            # OrderID Click
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, f"//code[contains(text(),{var_orderIDmention})]")))
            element.click()

            # Starting to Issue Refund Button
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Issue Refund')]")))
            element.click()

            # Refund Amount Entry
            print(var_refundAmount)
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class,'InputField')]//input[contains(@type,'number')]")))
            element.send_keys(var_refundAmount)

            # Issue Refund
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'btn btn-primary btn-block')]')]")))
            element.click()

        if op == False:
            messagebox.showinfo("Refund Mechanism", f"Refund for order ID:{var_orderIDmention}\n has been halted.", parent=support)

    def databaseOpen():
        con = sqlite3.connect(database=r'FileDetails.db')
        cur = con.cursor()
        try:
            cur.execute('select * from FileDetails')
            rows = cur.fetchall()
            database.delete(*database.get_children())
            for row in rows:
                database.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Refund Mechanism", f"Error Details: {str(ex)}", parent=support)

    # Database
    database_Frame = Frame(support, bd=3, relief=RIDGE)
    database_Frame.place(x=1, y=190, width=700, height=200)

    # ScrollBars
    scroll_xdir = Scrollbar(database_Frame, orient=HORIZONTAL)
    scroll_ydir = Scrollbar(database_Frame, orient=VERTICAL)

    # Table Creation
    database = ttk.Treeview(database_Frame,
                            columns=(
                                'Name', 'Extension', 'Date Created', 'Folder Path'),
                            yscrollcommand=scroll_ydir.set, xscrollcommand=scroll_xdir.set)
    scroll_xdir.pack(side=BOTTOM, fill=X)
    scroll_ydir.pack(side=RIGHT, fill=Y)
    scroll_ydir.config(command=database.yview)
    scroll_xdir.config(command=database.xview)
    database.heading('Name', text="Name")
    database.heading('Extension', text="Extension")
    database.heading('Date Created', text="Date Created")
    database.heading('Folder Path', text="Folder Path")
    database['show'] = 'headings'

    database.column('Name', width=200)
    database.column('Extension', width=48)
    database.column('Date Created', width=93)
    database.column('Folder Path', width=280)

    database.pack(fill=BOTH, expand=1)
    database.bind('<ButtonRelease-1>', passData1)

    databaseOpen()

    # refund Label
    refundFrame = LabelFrame(support, text="Refund Details", font=('goudy old style', 12, 'bold'), bd=2,
                             relief=RAISED,
                             bg='light yellow', fg='red')
    refundFrame.place(x=4, y=400, width=697, height=150)


    # refund Button
    refundBox_Btn_image1 = PhotoImage(file='images/Extras/wrong-black-wrong-icon-symbol-logo-trademark-rug-transparent-png-822781.png')
    refundBox_Btn1 = Button(refundFrame, command=lambda:[cleartxt1()], image=refundBox_Btn_image1, compound=LEFT,
                           relief=GROOVE, cursor='hand2', bd=2, anchor='c')
    refundBox_Btn1.place(x=45, y=5, width=60, height=40)
    refundBox_Btn1.image=refundBox_Btn_image1

    # refund Bar
    refundBar = Entry(refundFrame, textvariable=var_orderIDmention, font=('goudy old style', 14),
                      bg='NavajoWhite2',
                      fg='dim gray', relief=GROOVE, bd=1)
    refundBar.place(x=110, y=5, width=450, height=40)

    # refund Button
    refundBox_Btn_image = PhotoImage(file='images/Extras/transparent-refund-icon-e-commerce-icon-5f976f8ea6a6f6.5947196816037600146826.png')
    refundBox_Btn = Button(refundFrame, command=lambda: [refundAmount()], image=refundBox_Btn_image, compound=LEFT,
                           relief=GROOVE, cursor='hand2', bd=2, anchor='c')
    refundBox_Btn.place(x=565, y=5, width=60, height=40)
    refundBox_Btn.image=refundBox_Btn_image

    #refundAmountmention
    refundamt = Entry(refundFrame, textvariable=var_refundAmount, font=('goudy old style', 14),
                      bg='NavajoWhite2',
                      fg='dim gray', relief=GROOVE, bd=1)
    refundamt.place(x=115, y=70, width=300, height=40)
    refundamt.config(state='disabled')


    #refundiconfinal
    refundicon1_Btn_image = PhotoImage(file='images/Extras/6-2-refund-png.png')
    refundicon1_Btn = Button(refundFrame, command=lambda: [messagebox1()], image=refundicon1_Btn_image, compound=LEFT,
                           relief=GROOVE, cursor='hand2', bd=2, anchor='c')
    refundicon1_Btn.place(x=456, y=70, width=80, height=40)
    refundicon1_Btn.image=refundicon1_Btn_image




# Creating the Discount Tab
def discount():
    discount = Toplevel(root)
    discount.title('Discount Management System')
    discount.config(bg='light yellow')
    discount.geometry('1293x730+295+95')
    discount.focus_force()

    # Initialising global picture variables
    global PoliceDisc, StudentDisc, logo_title, PizzaDisc, BDAYDisc, MainCourseDisc, CoffeeDisc, CoffeeDisc1, CoffeeDisc2

    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Title
    logo_title = PhotoImage(file='images/Extras/SodaPDF-converted-voucher-icon-131.png')
    title = Label(discount, text=' Discount Management System', image=logo_title, compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=6,
                                                                                                relwidth=1,
                                                                                                height=70)

    # Underline 1
    underline = Label(discount,
                      text='                                                                                                                                                             ',
                      font=font1, bg='lightyellow', fg='black').place(x=0, y=64, width=1400)

    # Create A Main Frame
    main_frame = Frame(discount, bg="lightyellow")
    main_frame.place(x=0, y=102, relwidth=1, height=619)

    # Create A Canvas
    my_canvas = Canvas(main_frame, bg="lightyellow")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas, bg="lightyellow")

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")



    PoliceDisc = PhotoImage(file="images/Discount/FANTASTIC10.png")
    PoliceDisc_Btn = Label(second_frame, image=PoliceDisc, font=('times new roman', 30), bg='lightyellow',
                           anchor='c', fg='black', cursor='hand2', bd=4)

    PoliceDisc_Btn.grid(row=1, column=0, pady=40, padx=70)

    StudentDisc = PhotoImage(file="images/Discount/AMAZING20.png")
    StudentDisc_Btn = Label(second_frame, image=StudentDisc, font=('times new roman', 30), bg='lightyellow',
                            anchor='c', fg='black', cursor='hand2', bd=4)
    StudentDisc_Btn.grid(row=1, column=2, pady=0)

    PizzaDisc = PhotoImage(file="images/Discount/SUPER30.png")
    PizzaDisc_Btn = Label(second_frame, image=PizzaDisc, font=('times new roman', 30), bg='lightyellow',
                          anchor='c', fg='black', cursor='hand2', bd=4)
    PizzaDisc_Btn.grid(row=2, column=0, pady=40)

    MainCourseDisc = PhotoImage(file="images/Discount/FABULOUS40.png")
    MaincourseDisc_Btn = Label(second_frame, image=MainCourseDisc, font=('times new roman', 30), bg='lightyellow',
                               anchor='c', fg='black', cursor='hand2', bd=4)
    MaincourseDisc_Btn.grid(row=2, column=2, pady=0)

    BDAYDisc = PhotoImage(file="images/Discount/STUD50.png")
    BDAY_Btn = Label(second_frame, image=BDAYDisc, font=('times new roman', 30), bg='lightyellow', anchor='c',
                     fg='black', cursor='hand2', bd=4)
    BDAY_Btn.grid(row=3, column=0, pady=40)

    CoffeeDisc = PhotoImage(file="images/Discount/DEFENCE50.png")
    CoffeeDisc_Btn = Label(second_frame, image=CoffeeDisc, font=('times new roman', 30), bg='lightyellow',
                           anchor='c', fg='black', cursor='hand2', bd=4)
    CoffeeDisc_Btn.grid(row=3, column=2, pady=0)

    CoffeeDisc1 = PhotoImage(file="images/Discount/PIZZA45.png")
    CoffeeDisc_Btn = Label(second_frame, image=CoffeeDisc1, font=('times new roman', 30), bg='lightyellow',
                           anchor='c', fg='black', cursor='hand2', bd=4)
    CoffeeDisc_Btn.grid(row=4, column=0, pady=0)

    CoffeeDisc2 = PhotoImage(file="images/Discount/MOD50.png")
    CoffeeDisc_Btn = Label(second_frame, image=CoffeeDisc2, font=('times new roman', 30), bg='lightyellow',
                           anchor='c', fg='black', cursor='hand2', bd=4)
    CoffeeDisc_Btn.grid(row=4, column=2, pady=0)


##CALCULATIONS

##Creating the place order tab
def placeOrder():
    placeOrder = Toplevel()
    placeOrder.title('Bill Management System')
    placeOrder.config(bg='light yellow')
    placeOrder.geometry('1293x730+295+95')
    placeOrder.focus_force()

    # initialising the variables for photos of buttons
    global logo_title2, clear, updateImage, generatePDF, generateBill
    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Promo Frame
    global var_Promo
    PromoFrame = Frame(placeOrder, bd=1, relief=SUNKEN, bg='lightgreen')
    PromoFrame.place(x=424, y=120, width=420, height=70)
    promoLbl1 = Label(PromoFrame, text='Promo Code', font=('goudy old style', 25, 'bold'), fg='black',
                      bg='lightgreen').place(x=0, y=4, width=198, height=60)
    promoLbl2 = Label(PromoFrame, text=':', font=('goudy old style', 25, 'bold'), fg='black',
                      bg='lightgreen').place(
        x=198, y=3, width=10, height=55)
    promoDetails = Entry(PromoFrame, textvariable=var_Promo, font=('times new roman', 20, 'bold'), fg='darkgreen',
                         bg='lightgreen').place(x=213, y=5, width=197, height=60)

    # creating the text input from the user in calculator
    var_CalcInput = StringVar()
    global operator
    operator = ""

    # Title
    logo_title2 = PhotoImage(file='images/Extras/checkout-1553147-1314013_21.png')
    title = Label(placeOrder, text=' Bill Management System', image=logo_title2, compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=6,
                                                                                                relwidth=1,
                                                                                                height=70)

    # Underline 1
    underline = Label(placeOrder,
                      text='                                                                                                                                                             ',
                      font=font1, bg='lightyellow', fg='black').place(x=0, y=70, width=1400)

    # CalcFrame
    CalcFrame = Frame(placeOrder, bd=4, relief=RIDGE, bg='black')
    CalcFrame.place(x=424, y=200, width=422, height=300)
    CalcLbl = Label(CalcFrame, text='Calculator', font=('times new roman', 30, 'bold'), fg='white',
                    bg='black').grid(
        row=0, column=0, columnspan=4)

    # creating the calculator
    generateCalculator = Entry(CalcFrame, width=45, bg="white", bd=4, font=('arial', 12, 'bold'), justify=RIGHT,
                               textvariable=var_CalcInput)
    generateCalculator.grid(row=1, column=0, columnspan=4, pady=1)

    generateCalculator.insert(0, "0")

    # creating the buttons for calculator --- first line
    button_display7 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="7", bg="white", command=lambda: buttonClick(7)).grid(row=3, column=0)
    button_display8 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="8", bg="white", command=lambda: buttonClick(8)).grid(row=3, column=1)
    button_display9 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="9", bg="white", command=lambda: buttonClick(9)).grid(row=3, column=2)
    button_displayAdd = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                               text="+", bg="white", command=lambda: buttonClick("+")).grid(row=3, column=3)

    # creating the buttons for calculator --- second line
    button_display4 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="4", bg="white", command=lambda: buttonClick(4)).grid(row=4, column=0)
    button_display5 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="5", bg="white", command=lambda: buttonClick(5)).grid(row=4, column=1)
    button_display6 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="6", bg="white", command=lambda: buttonClick(6)).grid(row=4, column=2)
    button_displayMinus = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                                 text="-", bg="white", command=lambda: buttonClick("-")).grid(row=4, column=3)

    # creating the buttons for calculator --- third line
    button_display1 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="1", bg="white", command=lambda: buttonClick(1)).grid(row=5, column=0)
    button_display2 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="2", bg="white", command=lambda: buttonClick(2)).grid(row=5, column=1)
    button_display3 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="3", bg="white", command=lambda: buttonClick(3)).grid(row=5, column=2)
    button_displayMultiply = Button(CalcFrame, padx=16, bd=7, pady=1, fg='black', font=('arial', 16, 'bold'),
                                    width=4,
                                    text="*", bg="white", command=lambda: buttonClick("*")).grid(row=5, column=3)

    # creating the buttons for calculator --- third line
    button_display0 = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                             text="0", bg="white", command=lambda: buttonClick(0)).grid(row=6, column=0)
    button_displayClear = Button(CalcFrame, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4,
                                 text="C", bg="white", command=lambda: button_displayClear()).grid(row=6, column=1)
    button_displayEqualto = Button(CalcFrame, padx=16, bd=7, pady=1, fg='black', font=('arial', 16, 'bold'),
                                   width=4,
                                   text="=", bg="white", command=lambda: button_Equalto()).grid(row=6, column=2)
    button_displayDivide = Button(CalcFrame, padx=16, bd=7, pady=1, fg='black', font=('arial', 16, 'bold'), width=4,
                                  text="/", bg="white", command=lambda: buttonClick("/")).grid(row=6, column=3)

    def buttonClick(numbers):
        global operator
        operator = operator + str(numbers)
        var_CalcInput.set(operator)

    # defining clear button in calculator
    def button_displayClear():
        global operator
        operator = ""
        var_CalcInput.set("0")

    # Variables
    global var_CustName, var_CustPhone, var_CheckBox, var_CustEmail
    var_CustName = StringVar()
    var_CustPhone = IntVar()
    var_CheckBox = IntVar()
    var_CustEmail = StringVar()

    # CustomerDetailFrame
    CustomerDetailFrame = Frame(placeOrder, bd=1, relief=RIDGE, bg='lightgreen')
    CustomerDetailFrame.place(x=2, y=530, width=410, height=200)
    customerDetails = Label(CustomerDetailFrame, text='Customer Details', font=('times new roman', 30, 'bold'),
                            bg='black', fg='white').place(x=1, y=1, width=405)

    CustName = LabelFrame(CustomerDetailFrame, text="Name Of Customer", font=('goudy old style', 18, 'bold'), bd=2,
                          relief=RAISED, bg='lightgreen', fg='red')
    CustName.place(x=7, y=56, width=392, height=60)
    CustNameEntry = Entry(CustName, textvariable=var_CustName, font=('times new roman', 18), bg='lightblue',
                     fg='black').place(x=0, y=0, relwidth=1, relheight=1)

    CustPhone = LabelFrame(CustomerDetailFrame, text="Phone", font=('goudy old style', 18, 'bold'), bd=2,
                           relief=RAISED,
                           bg='lightgreen', fg='red')
    CustPhone.place(x=240, y=130, width=160, height=60)
    CustPhoneEntry = Entry(CustPhone, textvariable=var_CustPhone, font=('times new roman', 18), bg='lightblue',
                        fg='black').place(x=0, y=0, relwidth=1, relheight=1)

    CustEmail = LabelFrame(CustomerDetailFrame, text="Email", font=('goudy old style', 18, 'bold'),
                                 bd=2, relief=RAISED, bg='lightgreen', fg='red')
    CustEmail.place(x=7, y=130, width=224, height=60)
    CustEmailEntry = Entry(CustEmail, textvariable=var_CustEmail,
                                         font=('times new roman', 15), bg='lightblue', fg='black').place(x=0, y=0,
                                                                                                           relwidth=1,
                                                                                                       relheight=1)

    # initialising variables
    def calc():
        global var_pizzaTotal, var_pastaTotal, var_subwayTotal, var_frankieTotal, var_sandwichTotal, var_burgerTotal, \
            var_southindianTotal, var_northindianTotal, var_rotiTotal, var_thaliTotal, var_continentalTotal, var_curryTotal, \
            var_coffeeTotal, var_teaTotal, var_juiceTotal, var_frappeTotal, var_icecreamTotal, var_colddrinkTotal, \
            var_dessertTotal, var_starterTotal, var_mainCourseTotal, var_beveragesTotal, var_dessertTotal, var_bill, var_discountTotal, \
            var_netBill, var_tax

        # STARTER-TOTALS
        var_pizzaTotal = margheritaPrice + basilpaneerPrice + onioncheesePrice + mushroomPrice
        var_pastaTotal = garlicPrice + spinachPrice + paneerpastaPrice + whitesaucePrice
        var_subwayTotal = harabharaPrice + paneerFilletPrice + paneertikkaPrice + mexicanCount2Price
        var_frankieTotal = mixvegPrice + cheeseCount1Price + schezwanpaneerPrice + chillipaneerCount1Price
        var_sandwichTotal = pizzaPrice + tandooriPrice + mexicanCount1Price + clubCountPrice
        var_burgerTotal = paneerCount2Price + cheeseCount2Price + regularPrice + maharajaPrice

        # MAINCOURSE-TOTALS
        var_southindianTotal = idliPrice + dosaPrice + avalakkibhaatPrice + kharabhaatPrice + vadaPrice + puliyogrePrice
        var_northindianTotal = paneerparathaPrice + mushroomparathaPrice + rajmaparathaPrice + dalparathaPrice
        var_rotiTotal = parathaPrice + naanPrice + tandoorirotiPrice + missiPrice
        var_thaliTotal = familythaliPrice + executivethaliPrice + specialthaliPrice + regularthaliPrice
        var_continentalTotal = parfaitPrice + capresesandwichPrice + wafflePrice + pancakesPrice
        var_curryTotal = rajmaPrice + dalPrice + kolhapuriPrice + cholePrice

        # BEVERAGES-TOTALS
        var_coffeeTotal = americanoPrice + cappuccinoPrice + machiatoPrice + espressoPrice + lattePrice + mochaPrice
        var_teaTotal = lavenderTeaPrice + oolongTeaPrice + chamomilePrice + gingerTeaPrice + whiteTeaPrice + lemonTeaPrice + greenTeaPrice + hibiscusTeaPrice
        var_juiceTotal = watermelonPrice + lemonjuicePrice + carrotjuicePrice + orangejuicePrice
        var_frappeTotal = caramelFrappePrice + chocoFrappePrice + orangeFrappePrice + berryFrappePrice
        var_icecreamTotal = vanillaPrice + butterscotchPrice + blackcurrantPrice + mangoPrice
        var_colddrinkTotal = cokePrice + zeroPrice + sevenupPrice + pepsiPrice

        # DESSERTS-TOTALS
        global var_dessertTotal1
        var_dessertTotal = rasgullaPrice + rasmalaiPrice + browniePrice + gulabjamunPrice
        var_dessertTotal1 = var_dessertTotal

        # FINAL-TOTALS
        global var_starterTotal1, var_mainCourseTotal1, var_beveragesTotal1, var_bill1, var_tax1, var_netBill1, var_discountTotal1
        var_starterTotal = var_pizzaTotal + var_pastaTotal + var_subwayTotal + var_burgerTotal + var_sandwichTotal + var_frankieTotal
        var_starterTotal1 = var_starterTotal
        var_mainCourseTotal = var_southindianTotal + var_northindianTotal + var_curryTotal + var_rotiTotal + var_thaliTotal + var_continentalTotal
        var_mainCourseTotal1 = var_mainCourseTotal
        var_beveragesTotal = var_colddrinkTotal + var_coffeeTotal + var_teaTotal + var_juiceTotal + var_frappeTotal + var_icecreamTotal
        var_beveragesTotal1 = var_beveragesTotal
        var_bill = var_starterTotal + var_mainCourseTotal + var_beveragesTotal + var_dessertTotal
        var_bill1 = var_bill
        if var_Promo.get() == "FANTASTIC10":
            var_discountTotal = (10 / 100) * var_bill
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "":
            var_discountTotal = 0
        elif var_Promo.get() == "AMAZING20":
            var_discountTotal = (20 / 100) * var_bill
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "SUPER30":
            var_discountTotal = (30 / 100) * var_bill
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "FABULOUS40":
            var_discountTotal = (40 / 100) * var_bill
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "DEFENCE50" and var_CheckBox.get() == 1:
            var_discountTotal = (50 / 100) * var_mainCourseTotal
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "PIZZA45":
            var_discountTotal = (45 / 100) * var_pizzaTotal
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "STUD50":
            var_discountTotal = (50 / 100) * var_starterTotal
            var_discountTotal1 = var_discountTotal
        elif var_Promo.get() == "MOD50":
            var_discountTotal = (50 / 100) * var_dessertTotal
            var_discountTotal1 = var_discountTotal
        else:
            var_discountTotal = 0

        var_discountTotal = math.ceil(var_discountTotal)
        var_tax = (var_bill - var_discountTotal) * (18 / 100)
        var_tax = math.ceil(var_tax)
        var_tax1 = var_tax

        var_netBill = var_bill - var_discountTotal + var_tax
        var_netBill = math.ceil(var_netBill)
        var_netBill1 = var_netBill



    def razorpayGenerate():
        global var_netBill1,var_CustName,var_custEmail,var_orderID
        client = razorpay.Client(auth=("rzp_test_pCXkJRJbbWoRXV", "pYWdwH1Wwj9pS4OlGZL7Yn9A"))
        randnum = str(random.randint(1353898, 6558990))
        data = {
            "amount": var_netBill1*100,
            "currency": "INR",
            "receipt": randnum,
            "notes": {}
        }
        order = client.order.create(data=data)
        order_id = order["id"]
        var_orderID = order_id
        f = open("payment.html", "r")
        paymenthtmlstore = f.readlines()
        changethisorderid = paymenthtmlstore[6]
        changethisname = paymenthtmlstore[20]
        changethisemail = paymenthtmlstore[21]
        changethisphone = paymenthtmlstore[22]
        changethisorderid = "    " + '"order_id"' + ': "' + order_id + '",\n'
        print(order_id)
        changethisname = "        " + '"name"' + ': "' + var_CustName.get() + '",\n'
        print(changethisname)
        changethisemail = "       " + '"email"' + ': "' + var_CustEmail.get() + '",\n'
        print(changethisemail)
        changethisphone = "       " + '"contact"' + ': "' + str(var_CustPhone.get()) + '",\n'
        print(changethisphone)
        paymenthtmlstore[6] = changethisorderid
        paymenthtmlstore[20] = changethisname
        paymenthtmlstore[21] = changethisemail
        paymenthtmlstore[22] = changethisphone
        f = open("payment.html", "w")
        f.writelines(paymenthtmlstore)
        f.flush()
        f.close()
        invoice = client.order.create(data=data)



        # Search Label
        SearchFrame1 = LabelFrame(BillDetailsFrame, text="Starters", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED, bg='light yellow', fg='red')
        SearchFrame1.place(x=7, y=56, width=180, height=70)
        starterBill = Label(SearchFrame1, text=var_starterTotal, font=('times new roman', 18), bg='lightyellow',
                            fg='black').place(x=0,
                                              y=0,
                                              relwidth=1,
                                              relheight=1)

        SearchFrame2 = LabelFrame(BillDetailsFrame, text="MainCourse", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED, bg='light yellow', fg='red')
        SearchFrame2.place(x=220, y=56, width=180, height=70)
        maincourseBill = Label(SearchFrame2, text=var_mainCourseTotal, font=('times new roman', 18), fg='black',
                               bg='lightyellow').place(x=0, y=0, relwidth=1, relheight=1)

        SearchFrame3 = LabelFrame(BillDetailsFrame, text="Beverages", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED, bg='light yellow', fg='red')
        SearchFrame3.place(x=7, y=150, width=180, height=70)
        beveragesBill = Label(SearchFrame3, text=var_beveragesTotal, font=('times new roman', 18), fg='black',
                              bg='lightyellow').place(
            x=0, y=0, relwidth=1, relheight=1)

        SearchFrame4 = LabelFrame(BillDetailsFrame, text="Desserts", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED, bg='light yellow', fg='red')
        SearchFrame4.place(x=220, y=150, width=180, height=70)
        dessertsBill = Label(SearchFrame4, text=var_dessertTotal, font=('times new roman', 18), fg='black',
                             bg='lightyellow').place(
            x=0, y=0, relwidth=1, relheight=1)

        SearchFrame5 = LabelFrame(BillDetailsFrame, text="Bill", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED,
                                  bg='light yellow', fg='red')
        SearchFrame5.place(x=7, y=244, width=180, height=70)
        dessertsBill = Label(SearchFrame5, text=var_bill, font=('times new roman', 18), fg='black',
                             bg='lightyellow').place(
            x=0, y=0, relwidth=1, relheight=1)

        SearchFrame6 = LabelFrame(BillDetailsFrame, text="Discount", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED, bg='light yellow', fg='red')
        SearchFrame6.place(x=220, y=244, width=180, height=70)
        dessertsBill = Label(SearchFrame6, text=var_discountTotal, font=('times new roman', 18), fg='black',
                             bg='lightyellow').place(
            x=0, y=0, relwidth=1, relheight=1)

        SearchFrame7 = LabelFrame(BillDetailsFrame, text="Tax", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED,
                                  bg='light yellow', fg='red')
        SearchFrame7.place(x=7, y=338, width=180, height=70)
        dessertsBill = Label(SearchFrame7, text=var_tax, font=('times new roman', 18), fg='black',
                             bg='lightyellow').place(
            x=0, y=0, relwidth=1, relheight=1)

        SearchFrame8 = LabelFrame(BillDetailsFrame, text="NetPayable", font=('goudy old style', 18, 'bold'), bd=2,
                                  relief=RAISED, bg='light yellow', fg='red')
        SearchFrame8.place(x=220, y=338, width=180, height=70)
        dessertsBill = Label(SearchFrame8, text=var_netBill, font=('times new roman', 18), fg='black',
                             bg='lightyellow').place(
            x=0, y=0, relwidth=1, relheight=1)

    # defining equal to button in calculator
    def button_Equalto():
        global operator
        sumup = str(eval(operator))
        var_CalcInput.set(sumup)

    # ButtonFrame
    ButtonFrame = Frame(placeOrder, bd=1, relief=RIDGE, bg='lightyellow')
    ButtonFrame.place(x=420, y=513, width=432, height=202)
    customerDetails = Label(CustomerDetailFrame, text='Customer Details', font=('times new roman', 30, 'bold'),
                            bg='black', fg='white').place(x=1, y=1, width=405)


    def appcommand():

        for i in range(1):
            def open_link(url):
                sys.excepthook = cef.ExceptHook
                cef.Initialize()
                cef.CreateBrowserSync(url=url, window_title="Payment Page")
                cef.MessageLoop()

            if __name__ == '__main__':
                html = """<h3></h3>"""
                name = "payment.html"
                # if the file already exists, it will not be created again
                if name not in os.listdir():
                    with open(name, "w") as file:
                        file.write(html)
                openlink = open_link("file:///" + "payment.html")
                driver = webdriver.Chrome()
                driver.get("file:///" + "payment.html")
                button = driver.find_element_by_id('rzp-button1')
                button.click()

    def Receipt():
        # create a company name and information
        generateReceipt.delete("1.0", END)
        company_name = 'Cafè Connoseiurs Co.'
        company_address = 'MG ROAD'
        company_city = 'BENGALURU'
        date = datetime.now()
        dt_string = date.strftime("%d/%m/%Y %H:%M:%S")
        orderid= var_orderID



        # create a top border
        generateReceipt.insert(END, '^' * 46+'\n')

        generateReceipt.insert(END, '\t      \t    {}'.format(company_name)+'\n')
        generateReceipt.insert(END, '\t      \t         {}'.format(company_address)+'\n')
        generateReceipt.insert(END, '\t      \t        {}'.format(company_city)+'\n')
        generateReceipt.insert(END, '\t      \t   {}'.format(orderid)+'\n')
        generateReceipt.insert(END, '\t      \t {}'.format(dt_string) + '\n')

        generateReceipt.insert(END, '-' * 84+'\n')

        generateReceipt.insert(END, 'Product Name\t\t\tQuantity\t\tProduct Price'+'\n')

        generateReceipt.insert(END, '-' * 84+'\n')

        # create a print statement for each item

        # STARTERS
        if var_starterTotal!=0:
            generateReceipt.insert(END, '----Starter---------------------------------------------------------'+'\n')

        # SANDWICHES

        if pizzaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PIZZA SANDWICH", pizzaCount, pizzaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if tandooriCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("TANDOORI SANDWICH", tandooriCount, tandooriPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        if mexicanCount1 != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MEXICAN SANDWICH", mexicanCount1, mexicanCount1Price)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if clubCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CLUB SANDWICH", clubCount, clubCountPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # FRANKIE
        if mixvegCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MIXVEG FRANKIE", mixvegCount, mixvegPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if chillipaneerCount1 != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CHILLI PANEER FRANKIE", chillipaneerCount1, chillipaneerCount1Price)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if cheeseCount1 != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("VEG FINGERS", cheeseCount1, cheeseCount1Price)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if schezwanpaneerCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("SHEZWAN PANEER FRANKIE", schezwanpaneerCount, schezwanpaneerPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # SUBWAY
        if harabharaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("HARA BHARA SUBWAY", harabharaCount, harabharaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if paneerFilletCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PANEER FILLET SUBWAY", paneerFilletCount, paneerFilletPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if mexicanCount2 != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MEXICAN SUBWAY", mexicanCount2, mexicanCount2Price)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if paneertikkaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PANEER TIKKA SUBWAY", paneertikkaCount, paneertikkaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # BURGER
        if cheeseCount2 != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CHEESE BURGER", cheeseCount2, cheeseCount2Price)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if regularCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("REGULAR BURGER", regularCount, regularPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if paneerCount2 != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PANEER BURGER", paneerCount2, paneerCount2Price)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if maharajaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MAHARAJA BURGER", maharajaCount, maharajaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # PIZZA
        if margheritaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MARGHERITA PIZZA", margheritaCount, margheritaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if basilpaneerCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("BASIL PANEER PIZZA", basilpaneerCount, basilpaneerPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if mushroomCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MUSHROOM PIZZA", mushroomCount, mushroomPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if onioncheeseCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("ONION CHEESE PIZZA", onioncheeseCount, onioncheesePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # PASTA
        if garlicCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("GARLIC PASTA", garlicCount, garlicPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if whitesauceCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("WHITE SAUCE PASTA", whitesauceCount, whitesaucePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if spinachCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("SPINACH PASTA", spinachCount, spinachPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if paneerpastaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PANEER PASTA", paneerpastaCount, paneerpastaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # MAINCOURSE
        if var_mainCourseTotal!=0:
            generateReceipt.insert(END, '----Main Course----------------------------------------------------------'+'\n')

        # SOUTHINDIAN
        if idliCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("IDLI", idliCount, idliPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if vadaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("VADA", vadaCount, vadaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if dosaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("DOSA", dosaCount, dosaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if avalakkibhaatCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("AVALAKKIBHAAT", avalakkibhaatCount, avalakkibhaatPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if kharabhaatCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("KHARABHAAT", kharabhaatCount, kharabhaatPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if puliyogreCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PULIYOGRE", puliyogreCount, puliyogrePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # VEGCURRY
        if rajmaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("RAJMA", rajmaCount, rajmaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if dalCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("DAL", dalCount, dalPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if kolhapuriCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("KOLHAPURI", kolhapuriCount, kolhapuriPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if choleCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CHOLE", choleCount, cholePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # ROTI
        if naanCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("NAAN", naanCount, naanPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if missiCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MISSI ROTI", missiCount, missiPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if parathaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PARATHA", parathaCount, parathaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if tandoorirotiCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("TANDOORI ROTI", tandoorirotiCount, tandoorirotiPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # NORTHINDIAN
        if rajmaparathaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("RAJMA PARATHA", rajmaparathaCount, rajmaparathaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if dalparathaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("DAL PARATHA", dalparathaCount, dalparathaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if paneerparathaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PANEER PARATHA", paneerparathaCount, paneerparathaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if mushroomparathaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MUSHROOM PARATHA", mushroomparathaCount, mushroomparathaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # THALI
        if regularthaliCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("REGULAR THALI", regularthaliCount, regularthaliPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if executivethaliCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("EXECUTIVE THALI", executivethaliCount, executivethaliPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if familythaliCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("FAMILY THALI", familythaliCount, familythaliPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if specialthaliCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("SPECIAL THALI", specialthaliCount, specialthaliPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # CONTINENTAL
        if parfaitCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PARFAIT", parfaitCount, parfaitPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if capresesandwichCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CAPRESES SANDWICH", capresesandwichCount, capresesandwichPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if waffleCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("WAFFLE", waffleCount, wafflePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if pancakesCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PANCAKES", pancakesCount, pancakesPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # BEVERAGES
        if var_beveragesTotal!=0:
            generateReceipt.insert(END, '----Beverages---------------------------------------------------------------'+'\n')

        # COFFEE
        if cappuccinoCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CAPUCCINO", cappuccinoCount, cappuccinoPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if americanoCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("AMERICANO", americanoCount, americanoPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if espressoCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("ESPRESSO", espressoCount, espressoPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if machiatoCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MACHIATO", machiatoCount, machiatoPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if latteCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("LATTE", latteCount, lattePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if mochaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MOCHA", mochaCount, mochaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # TEA
        if chamomileCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CHAMOMILE", chamomileCount, chamomilePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if oolongTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("OOLONG TEA", oolongTeaCount, oolongTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if whiteTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("WHITE TEA", whiteTeaCount, whiteTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if gingerTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("GINGER TEA", gingerTeaCount, gingerTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if hibiscusTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("HIBISCUS TEA", hibiscusTeaCount, hibiscusTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if lavenderTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("LAVENDER TEA", lavenderTeaCount, lavenderTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if lemonTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("LEMON TEA", lemonTeaCount, lemonTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if greenTeaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("GREEN TEA", greenTeaCount, greenTeaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # COLDRINK
        if pepsiCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("PEPSI", pepsiCount, pepsiPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if sevenupCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("SEVEN UP", sevenupCount, sevenupPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if zeroCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("ZERO", zeroCount, zeroPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if cokeCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("COKE", cokeCount, cokePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # JUICE
        if orangejuiceCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("ORANGE JUICE", orangejuiceCount, orangejuicePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if watermelonCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("WATER MELON JUICE", watermelonCount, watermelonPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if lemonjuiceCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("LEMON JUICE", lemonjuiceCount, lemonjuicePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if carrotjuiceCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CARROT JUICE", carrotjuiceCount, carrotjuicePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # FRAPPE
        if chocoFrappeCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CHOCO FRAPPE", chocoFrappeCount, chocoFrappePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if orangeFrappeCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("ORANGE FRAPPE", orangeFrappeCount, orangeFrappePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if berryFrappeCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("BERRY FRAPPE", berryFrappeCount, berryFrappePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if caramelFrappeCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("CARAMEL FRAPPE", caramelFrappeCount, caramelFrappePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # ICECREAM
        if vanillaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("VANILLA", vanillaCount, vanillaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if butterscotchCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("BUTTERSCOTCH", butterscotchCount, butterscotchPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if blackcurrantCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("BLACKCURRANT", blackcurrantCount, blackcurrantPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if mangoCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("MANGO", mangoCount, mangoPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        # DESSERTS
        if var_dessertTotal!=0:
            generateReceipt.insert(END, '----Dessert----------------------------------------------------------'+'\n')
        if rasgullaCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("RASGULLA", rasgullaCount, rasgullaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if rasmalaiCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("RASMALAI", rasmalaiCount, rasgullaPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if gulabjamunCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("GULAB JAMUN", gulabjamunCount, gulabjamunPrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')
        if brownieCount != 0:
            generateReceipt.insert(END, '{}\t\t     \t       {}\t\t       ₹{}'.format("BROWNIE", brownieCount, browniePrice)+'\n')
            generateReceipt.insert(END, '=' * 46+'\n')

        generateReceipt.insert(END, '=' * 46 + '\n')
        generateReceipt.insert(END, 'Tax\t\t\t\t\t      ₹{}'.format(var_tax)+'\n')


        # print a line between sections
        generateReceipt.insert(END, '=' * 46+'\n')

        #discount section
        if var_discountTotal!=0:
            generateReceipt.insert(END, 'Discount\t\t\t\t\t      -₹{}'.format(var_discountTotal) + '\n')

        # print a line between sections
        generateReceipt.insert(END, '=' * 46+'\n')

        # calculate total price and print out
        total = var_netBill
        generateReceipt.insert(END, 'Total\t\t\t\t\t     ₹{}'.format(total)+'\n')

        # print a line between sections
        generateReceipt.insert(END, '=' * 46+'\n')

        # output thank you message
        generateReceipt.insert(END, '\t               {}\n\t                  {}'.format("Thank You For Coming!","Have A Nice Day")+'\n')

        # create a bottom border
        generateReceipt.insert(END, '*' * 52+'\n')

    def Receipt1():
        # create a company name and information
        generateReceipt1.delete("1.0", END)
        company_name = 'Cafè Connoseiurs Co.'
        company_address = 'MG ROAD'
        company_city = 'BENGALURU'
        orderid= var_orderID


        # create a top border
        generateReceipt1.insert(END, '^' * 80+'\n')

        generateReceipt1.insert(END, '\t      \t    {}'.format(company_name)+'\n')
        generateReceipt1.insert(END, '\t      \t         {}'.format(company_address)+'\n')
        generateReceipt1.insert(END, '\t      \t        {}'.format(company_city)+'\n')
        generateReceipt1.insert(END, '\t      \t   {}'.format(orderid)+'\n')

        generateReceipt1.insert(END, '-' * 84+'\n')

        generateReceipt1.insert(END, 'Product Name\t\t\tQuantity\t\tProduct Price'+'\n')

        generateReceipt1.insert(END, '-' * 84+'\n')

        # create a print statement for each item

        # STARTERS
        if var_starterTotal!=0:
            generateReceipt1.insert(END, '----Starter---------------------------------------------------------------------------'+'\n')

        # SANDWICHES

        if pizzaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PIZZA SANDWICH", pizzaCount, pizzaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if tandooriCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("TANDOORI SANDWICH", tandooriCount, tandooriPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        if mexicanCount1 != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MEXICAN SANDWICH", mexicanCount1, mexicanCount1Price)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if clubCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CLUB SANDWICH", clubCount, clubCountPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # FRANKIE
        if mixvegCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MIXVEG FRANKIE", mixvegCount, mixvegPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if chillipaneerCount1 != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CHILLI PANEER FRANKIE", chillipaneerCount1, chillipaneerCount1Price)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if cheeseCount1 != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("VEG FINGERS", cheeseCount1, cheeseCount1Price)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if schezwanpaneerCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("SHEZWAN PANEER FRANKIE", schezwanpaneerCount, schezwanpaneerPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # SUBWAY
        if harabharaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("HARA BHARA SUBWAY", harabharaCount, harabharaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if paneerFilletCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PANEER FILLET SUBWAY", paneerFilletCount, paneerFilletPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if mexicanCount2 != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MEXICAN SUBWAY", mexicanCount2, mexicanCount2Price)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if paneertikkaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PANEER TIKKA SUBWAY", paneertikkaCount, paneertikkaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # BURGER
        if cheeseCount2 != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CHEESE BURGER", cheeseCount2, cheeseCount2Price)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if regularCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("REGULAR BURGER", regularCount, regularPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if paneerCount2 != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PANEER BURGER", paneerCount2, paneerCount2Price)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if maharajaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MAHARAJA BURGER", maharajaCount, maharajaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # PIZZA
        if margheritaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MARGHERITA PIZZA", margheritaCount, margheritaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if basilpaneerCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("BASIL PANEER PIZZA", basilpaneerCount, basilpaneerPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if mushroomCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MUSHROOM PIZZA", mushroomCount, mushroomPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if onioncheeseCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("ONION CHEESE PIZZA", onioncheeseCount, onioncheesePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # PASTA
        if garlicCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("GARLIC PASTA", garlicCount, garlicPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if whitesauceCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("WHITE SAUCE PASTA", whitesauceCount, whitesaucePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if spinachCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("SPINACH PASTA", spinachCount, spinachPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if paneerpastaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PANEER PASTA", paneerpastaCount, paneerpastaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # MAINCOURSE
        if var_mainCourseTotal!=0:
            generateReceipt1.insert(END, '----Main Course-----------------------------------------------------------------------'+'\n')

        # SOUTHINDIAN
        if idliCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("IDLI", idliCount, idliPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if vadaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("VADA", vadaCount, vadaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if dosaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("DOSA", dosaCount, dosaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if avalakkibhaatCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("AVALAKKIBHAAT", avalakkibhaatCount, avalakkibhaatPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if kharabhaatCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("KHARABHAAT", kharabhaatCount, kharabhaatPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if puliyogreCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PULIYOGRE", puliyogreCount, puliyogrePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # VEGCURRY
        if rajmaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("RAJMA", rajmaCount, rajmaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if dalCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("DAL", dalCount, dalPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if kolhapuriCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("KOLHAPURI", kolhapuriCount, kolhapuriPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if choleCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CHOLE", choleCount, cholePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # ROTI
        if naanCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("NAAN", naanCount, naanPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if missiCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MISSI ROTI", missiCount, missiPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if parathaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PARATHA", parathaCount, parathaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if tandoorirotiCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("TANDOORI ROTI", tandoorirotiCount, tandoorirotiPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # NORTHINDIAN
        if rajmaparathaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("RAJMA PARATHA", rajmaparathaCount, rajmaparathaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if dalparathaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("DAL PARATHA", dalparathaCount, dalparathaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if paneerparathaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PANEER PARATHA", paneerparathaCount, paneerparathaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if mushroomparathaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MUSHROOM PARATHA", mushroomparathaCount, mushroomparathaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # THALI
        if regularthaliCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("REGULAR THALI", regularthaliCount, regularthaliPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if executivethaliCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("EXECUTIVE THALI", executivethaliCount, executivethaliPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if familythaliCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("FAMILY THALI", familythaliCount, familythaliPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if specialthaliCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("SPECIAL THALI", specialthaliCount, specialthaliPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # CONTINENTAL
        if parfaitCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PARFAIT", parfaitCount, parfaitPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if capresesandwichCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CAPRESES SANDWICH", capresesandwichCount, capresesandwichPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if waffleCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("WAFFLE", waffleCount, wafflePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if pancakesCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PANCAKES", pancakesCount, pancakesPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # BEVERAGES
        if var_beveragesTotal!=0:
            generateReceipt1.insert(END, '----Beverages---------------------------------------------------------------------------'+'\n')

        # COFFEE
        if cappuccinoCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CAPUCCINO", cappuccinoCount, cappuccinoPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if americanoCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("AMERICANO", americanoCount, americanoPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if espressoCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("ESPRESSO", espressoCount, espressoPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if machiatoCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MACHIATO", machiatoCount, machiatoPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if latteCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("LATTE", latteCount, lattePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if mochaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MOCHA", mochaCount, mochaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # TEA
        if chamomileCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CHAMOMILE", chamomileCount, chamomilePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if oolongTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("OOLONG TEA", oolongTeaCount, oolongTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if whiteTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("WHITE TEA", whiteTeaCount, whiteTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if gingerTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("GINGER TEA", gingerTeaCount, gingerTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if hibiscusTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("HIBISCUS TEA", hibiscusTeaCount, hibiscusTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if lavenderTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("LAVENDER TEA", lavenderTeaCount, lavenderTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if lemonTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("LEMON TEA", lemonTeaCount, lemonTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if greenTeaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("GREEN TEA", greenTeaCount, greenTeaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # COLDRINK
        if pepsiCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("PEPSI", pepsiCount, pepsiPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if sevenupCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("SEVEN UP", sevenupCount, sevenupPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if zeroCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("ZERO", zeroCount, zeroPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if cokeCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("COKE", cokeCount, cokePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # JUICE
        if orangejuiceCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("ORANGE JUICE", orangejuiceCount, orangejuicePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if watermelonCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("WATER MELON JUICE", watermelonCount, watermelonPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if lemonjuiceCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("LEMON JUICE", lemonjuiceCount, lemonjuicePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if carrotjuiceCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CARROT JUICE", carrotjuiceCount, carrotjuicePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # FRAPPE
        if chocoFrappeCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CHOCO FRAPPE", chocoFrappeCount, chocoFrappePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if orangeFrappeCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("ORANGE FRAPPE", orangeFrappeCount, orangeFrappePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if berryFrappeCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("BERRY FRAPPE", berryFrappeCount, berryFrappePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if caramelFrappeCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("CARAMEL FRAPPE", caramelFrappeCount, caramelFrappePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # ICECREAM
        if vanillaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("VANILLA", vanillaCount, vanillaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if butterscotchCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("BUTTERSCOTCH", butterscotchCount, butterscotchPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if blackcurrantCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("BLACKCURRANT", blackcurrantCount, blackcurrantPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if mangoCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("MANGO", mangoCount, mangoPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        # DESSERTS
        if var_dessertTotal!=0:
            generateReceipt1.insert(END, '----Dessert------------------------------------------------------------------------------------'+'\n')
        if rasgullaCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("RASGULLA", rasgullaCount, rasgullaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if rasmalaiCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("RASMALAI", rasmalaiCount, rasgullaPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if gulabjamunCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("GULAB JAMUN", gulabjamunCount, gulabjamunPrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')
        if brownieCount != 0:
            generateReceipt1.insert(END, '{}\t\t     \t       {}\t\t       {}'.format("BROWNIE", brownieCount, browniePrice)+'\n')
            generateReceipt1.insert(END, '=' * 80+'\n')

        generateReceipt1.insert(END, '=' * 80 + '\n')
        generateReceipt1.insert(END, 'Tax\t\t\t\t\t      {}'.format(var_tax)+'\n')


        # print a line between sections
        generateReceipt1.insert(END, '=' * 80+'\n')

        #discount section
        if var_discountTotal!=0:
            generateReceipt1.insert(END, 'Discount\t\t\t\t\t      -{}'.format(var_discountTotal) + '\n')

        # print a line between sections
        generateReceipt1.insert(END, '=' * 80+'\n')

        # calculate total price and print out
        total = var_netBill
        generateReceipt1.insert(END, 'Total\t\t\t\t\t     {}'.format(total)+'\n')

        # print a line between sections
        generateReceipt1.insert(END, '=' * 80+'\n')

        # output thank you message
        generateReceipt1.insert(END, '\t               {}\n\t                  {}'.format("Thank You For Coming!","Have A Nice Day")+'\n')

        # create a bottom border
        generateReceipt1.insert(END, '*' * 80+'\n')

#saving the bill

    def saveReceipt():
        url = open(f"Bills/txt/Bill for Order - {var_orderID}.txt","w+")
        receipt = generateReceipt1.get("1.0", "end-1c")
        print(receipt)
        url.write(receipt)
        url.close()

        # save FPDF() class into
        # a variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)

        # open the text file in read mode
        f = open(f"Bills/txt/Bill for Order - {var_orderID}.txt", "r")

        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='C')

        # save the pdf with name .pdf
        pdf.output(f"Bills/pdf/Bill for Order - {var_orderID}.pdf")

        messagebox.showinfo("Bill Management System","Bill Generated Succssfully"+"\n"+r"Bill Location -"+"\n"+r"C:\Users\DELL\Downloads\COMP_PROJ_21-22\Bills"+f"\Bill for Order - {var_orderID}.pdf",parent=placeOrder)


    def onupdateClick():
        global count
        count = IntVar
        count=1


    def paymentClick():
        if var_netBill==0:
            messagebox.showerror("Bill Management System", "Please Create An Order To Proceed", parent=placeOrder)
        if count!=1:
            messagebox.showerror("Bill Management System", "Please Click On Update To Proceed", parent=placeOrder)

    def onPaymentButtonClick():
            generateBill_Btn.config(state=NORMAL)

    def onbillGenerateClick():
            saveBill_Btn.config(state=NORMAL)

    saveBill = PhotoImage(file='images/Extras/generatePDF.png')
    saveBill_Btn = Button(ButtonFrame, image=saveBill, font=('times new roman', 30),
                             bg='lightyellow', fg='black', cursor='hand2', bd=1,state=DISABLED, relief=FLAT, command=lambda: [saveReceipt()])
    saveBill_Btn.image=saveBill
    saveBill_Btn.grid(row=2, column=0)


    payment = PhotoImage(file="images/Extras/payment1.png")
    Payment_Btn = Button(ButtonFrame, image=payment, font=('times new roman', 30), bg='lightyellow', fg='black',
                       cursor='hand2', bd=1, relief=FLAT,command= lambda:[paymentClick(),onPaymentButtonClick(),appcommand()])
    Payment_Btn.image=payment
    Payment_Btn.grid(row=1, column=0)


    generateBill = PhotoImage(file='images/Extras/generateBill.png')
    generateBill_Btn = Button(ButtonFrame, image=generateBill, font=('times new roman', 30),
                              bg='lightyellow', fg='black',state=DISABLED, cursor='hand2', bd=1, relief=FLAT, command=lambda: [Receipt(),Receipt1(),onbillGenerateClick()])
    generateBill_Btn.grid(row=2, column=1)



    updateImage = PhotoImage(file='images/Extras/update.png')
    update_Btn = Button(ButtonFrame, image=updateImage, font=('times new roman', 30),
                        bg='lightyellow', fg='black', cursor='hand2', bd=1, relief=FLAT,command=lambda: [calc(), razorpayGenerate(), onupdateClick()])
    update_Btn.grid(row=1, column=1)





    # BillDetails Frame
    BillDetailsFrame = Frame(placeOrder, bd=1, relief=RIDGE, bg='lightyellow')
    BillDetailsFrame.place(x=2, y=110, width=410, height=415)
    billDetails = Label(BillDetailsFrame, text='Bill Details', font=('times new roman', 30, 'bold'), bg='black',
                        fg='white').place(x=1, y=1, width=405)

    # Search Label
    SearchFrame1 = LabelFrame(BillDetailsFrame, text="Starters", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED, bg='light yellow', fg='red')
    SearchFrame1.place(x=7, y=56, width=180, height=70)
    starterBill = Label(SearchFrame1, text='0', font=('times new roman', 18), bg='lightyellow', fg='black').place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1)

    SearchFrame2 = LabelFrame(BillDetailsFrame, text="MainCourse", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED, bg='light yellow', fg='red')
    SearchFrame2.place(x=220, y=56, width=180, height=70)
    maincourseBill = Label(SearchFrame2, text='0', font=('times new roman', 18), fg='black',
                           bg='lightyellow').place(x=0, y=0, relwidth=1, relheight=1)

    SearchFrame3 = LabelFrame(BillDetailsFrame, text="Beverages", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED, bg='light yellow', fg='red')
    SearchFrame3.place(x=7, y=150, width=180, height=70)
    beveragesBill = Label(SearchFrame3, text='0', font=('times new roman', 18), fg='black', bg='lightyellow').place(
        x=0, y=0, relwidth=1, relheight=1)

    SearchFrame4 = LabelFrame(BillDetailsFrame, text="Desserts", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED, bg='light yellow', fg='red')
    SearchFrame4.place(x=220, y=150, width=180, height=70)
    dessertsBill = Label(SearchFrame4, text='0', font=('times new roman', 18), fg='black', bg='lightyellow').place(
        x=0, y=0, relwidth=1, relheight=1)

    SearchFrame5 = LabelFrame(BillDetailsFrame, text="Bill", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED,
                              bg='light yellow', fg='red')
    SearchFrame5.place(x=7, y=244, width=180, height=70)
    dessertsBill = Label(SearchFrame5, text='0', font=('times new roman', 18), fg='black', bg='lightyellow').place(
        x=0, y=0, relwidth=1, relheight=1)

    SearchFrame6 = LabelFrame(BillDetailsFrame, text="Discount", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED, bg='light yellow', fg='red')
    SearchFrame6.place(x=220, y=244, width=180, height=70)
    dessertsBill = Label(SearchFrame6, text='0', font=('times new roman', 18), fg='black', bg='lightyellow').place(
        x=0, y=0, relwidth=1, relheight=1)

    SearchFrame7 = LabelFrame(BillDetailsFrame, text="Tax", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED,
                              bg='light yellow', fg='red')
    SearchFrame7.place(x=7, y=338, width=180, height=70)
    dessertsBill = Label(SearchFrame7, text='0', font=('times new roman', 18), fg='black', bg='lightyellow').place(
        x=0, y=0, relwidth=1, relheight=1)

    SearchFrame8 = LabelFrame(BillDetailsFrame, text="NetPayable", font=('goudy old style', 18, 'bold'), bd=2,
                              relief=RAISED, bg='light yellow', fg='red')
    SearchFrame8.place(x=220, y=338, width=180, height=70)
    dessertsBill = Label(SearchFrame8, text='0', font=('times new roman', 18), fg='black', bg='lightyellow').place(
        x=0, y=0, relwidth=1, relheight=1)

    # Bill
    BillFrame = Frame(placeOrder, bd=1, relief=RIDGE, bg='lightyellow')
    BillFrame.place(x=858, y=110, width=432, height=50)
    bill = Label(BillFrame, text='Bill', font=('times new roman', 30, 'bold'), bg='black', fg='white').place(x=1,
                                                                                                             y=1,
                                                                                                             width=429)
    BillFrame2 = Frame(placeOrder, bd=1, relief=RIDGE, bg='lightyellow')
    BillFrame2.place(x=858, y=160, width=432, height=560)


    #Receipt
    generateReceipt = Text(BillFrame2, bg="white", bd=4, font=('times new roman', 12, 'bold'),height=560, width=432)
    generateReceipt.grid(row=0,column=0)
    generateReceipt.pack()

    #FakeReceipt
    generateReceipt1 = Text(BillFrame2, bg="white", bd=4, font=('times new roman', 12, 'bold'),height=560, width=432)




def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # updating seconds hand
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # updating minutes hand
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # updating hours hand
    hours_x = hours_hand_len * math.sin(math.radians(hours * 31)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 31)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    root.after(1000, update_clock)


canvas = Canvas(root, width=400, height=400, bg="#0B1C26",bd=3, relief=RIDGE)
canvas.place(x=-2,y=71,width=301,height=229)

# create background
bg = PhotoImage(file='images/Extras/c.png')
canvas.create_image(145, 115, image=bg)


# create clock hands
# seconds hand
center_x = 145
center_y = 114

seconds_hand_len = 75
minutes_hand_len = 60
hours_hand_len = 40

seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
# minutes hand
minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
# hours hand
hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')

update_clock()

# Creating the root window
# Title
logo_title10 = PhotoImage(file='images/Extras/R1.png')
title = Label(root, text=' CompEatify - Restaurants And Employees', image=logo_title10, compound=LEFT,
              font=('courier', 40, 'bold'), bg='#020b39', fg='white', anchor='w').place(x=0, y=0, relwidth=1,
                                                                                        height=70)


def logoutBtn():
    root.destroy()


# Logout Button
Logout_Btn = Button(root, text='Logout', font=('lucid consolas', 28, 'bold'), bg='red', cursor='hand2',
                    command=logoutBtn,
                    fg='yellow').place(x=1420, y=12, height=47)

# Creating the Menu Side Bar
Left_Tabs = Frame(root, bd=1, relief=RIDGE, bg='white')
Left_Tabs.place(x=0, y=300, width=301, height=780)

#Creating The Startup Image
StartupImage = Frame(root, bd=1, relief=RIDGE, bg='white')
StartupImage.place(x=301, y=71, width=1300, height=765)

#Placing the Startup Image
startupimage= PhotoImage(file='images/Extras/StartupImage.png')
Image = Label(StartupImage, image=startupimage,bg='light yellow', fg='black', anchor='center', bd=3)
Image.pack(fill=BOTH)

#Changing Employee Name
global sandy1
sandy1=sandy[0]

# Employee Details
Employee = Label(Left_Tabs, relief=RAISED, text=sandy1, compound=LEFT, font=('times new roman', 30),
                 bg='light yellow', fg='black', anchor='center', bd=3).pack(side=TOP, fill=X)

# Main Menu Tab
mainmenu_logo = PhotoImage(file='images/Extras/Removal-179.png')
MainMenu_Btn = Button(Left_Tabs, text='  Main Menu', image=mainmenu_logo, compound=LEFT, command=menu,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='center',
                      bd=3).pack(side=TOP, fill=X)

# Drinks And Desserts Tab
drinksdesserts_logo = PhotoImage(file='images/Extras/47418f210e99160c3b648cd840ff0f64.png')
DrinksDesserts_Btn = Button(Left_Tabs, text='Desserts', image=drinksdesserts_logo,
                            compound=LEFT, font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2',
                            command=dessert,
                            anchor='c', bd=3).pack(side=TOP, fill=X)

# Support Tab
support_logo = PhotoImage(file='images/Extras/customer-care-87-1131395.png')
Support_Btn = Button(Left_Tabs, text='  Support', image=support_logo, compound=LEFT, command=support,
                     font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='c',
                     bd=3).pack(
    side=TOP, fill=X)

# Discounts Tab
discount_logo = PhotoImage(file='images/Extras/SodaPDF-converted-voucher-icon-13.png')
Disc_Btn = Button(Left_Tabs, text='  Discounts', image=discount_logo, compound=LEFT, command=discount,
                  font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='c', bd=3).pack(
    side=TOP, fill=X)

# Employee Tab
employee_logo = PhotoImage(file='images/Extras/6609538_preview.png')
Employee_Btn = Button(Left_Tabs, text=' Employee', image=employee_logo, compound=LEFT, command=employee,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='c',
                      bd=3).pack(
    side=TOP, fill=X)

# Checkout Tab
checkout_logo = PhotoImage(file='images/Extras/checkout-1553147-1314013_2.png')
Chkout_Btn = Button(Left_Tabs, text=' Place Order',
                    image=checkout_logo, compound=LEFT, font=('times new roman', 30), bg='sky blue', fg='black',
                    command=placeOrder,
                    cursor='hand2', anchor='c', bd=3).pack(side=TOP, fill=X)


root.mainloop()

