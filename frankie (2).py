
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
                          fg='lightyellow').place(x=100, y=270, width=20, height=20)
       def updatePrice():
           global rajmaparathaCount, rajmaparathaPrice, frankieTotal1
           frankieTotal1 = str(rajmaparathaPrice+dalparathaPrice+mushroomparathaPrice+paneerparathaPrice)
           print(frankieTotal1)
           if frankieTotal1 == '0':
               print(1)
               Coffee_Lbl = Label(second_frame1, text='North Indian', font=('times new roman', 30, 'bold'),
                                  bg='lightyellow',
                                  fg='black').place(x=10, y=4, height =75, width=200)
           elif frankieTotal1 != '0':
               print(2)
               priceShow_LblFrame = LabelFrame(second_frame1, text='N.Indian Total', font=('times new roman', 13, 'bold')
                                  , relief = RIDGE, bd = 2, bg='lightyellow',fg='red')
               priceShow_LblFrame.place(x=10, y=4, height=75, width=200)
               priceShow_Lbl = Label(priceShow_LblFrame, text=frankieTotal1, relief=RIDGE, font=('times new roman', 30, 'bold'),
                                  bg='lightblue',fg='black')
               priceShow_Lbl.place(x=10, y=0, width=160, height=50)
       updatePrice()

   rajmaparatha = PhotoImage(file="images/NorthIndian/rajmaparatharound.png")
   rajmaparatha_Btn = Label(second_frame1, image=rajmaparatha,
                    font=('times new roman', 30), anchor='c')
   rajmaparatha_Btn.image = rajmaparatha
   rajmaparatha_Btn.grid(row=2, column=0, pady=10, padx=20, ipadx=1, ipady=1)


   def add1():
       global rajmaparathaCount
       rajmaparathaCount+=1

   def subtract1():
       global rajmaparathaCount
       if rajmaparathaCount > 0:
          rajmaparathaCount-=1
       elif rajmaparathaCount <= 0:
           rajmaparathaCount=0


   AddButton1 = Button(second_frame1, image = addImage, font=('times new roman', 15),bg='lightyellow'
                      , anchor='c', cursor='hand2', bd=2, command = lambda: [add1(),rajmaparathaClick1()])
   AddButton1.place(x=125, y=253, width=20, height=20)


   SubtractButton1 = Button(second_frame1, image = subtractImage, font=('times new roman', 15),bg='lightyellow'
                           , anchor='c', cursor='hand2', bd=2, command = lambda: [subtract1(),rajmaparathaClick1()])
   SubtractButton1.place(x=83, y=253, width=20, height=20)






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

