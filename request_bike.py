
from ast import While
from tkinter import *
from tkinter import messagebox


from DataBase import conn_db as db
from datetime import datetime as dt
from final_message import *
# def (request_bike()):


def request_bike():
    
    def store_to_db():
        
        # name_exists= db.to_search_name(name_text.get())
        
        dublicate_name = db.to_search_name(name_text.get())
        if dublicate_name:
            print('Someone has used this name')
            messagebox.showerror('Try Again', f"Error: This name is already Used.\n {dublicate_name[0][1]}")
        else:
            if int(number_bikes_text.get()) < 100:
                time_now =dt.now()
                db.to_insert(name_text.get(), number_bikes_text.get(), time_now)
                print(name_text.get(), number_bikes_text.get(), time_now)
                global current_user_name, current_user_bikes
                current_user_name = name_text.get()
                current_user_bikes = number_bikes_text.get()
                # print(f"My intrest :  {test_var}  {name_text.get()}")
                window2.destroy()
                message_request_final()
            else:
                messagebox.showerror('Try Again', f"We only have 100 bikes.")
                
                
                
    font_family = "Roman"

    window2 = Tk()
    window2.wm_title('Request a Bike')
    window2.geometry("550x300")

    l = Label(window2, text="Currently we have 100 bikes")
    l.config(font=(font_family, 15))
    # l.grid(row=1,column=1)
    l.pack(side=TOP, pady=10)

    l2 = Label(window2, text="Fill the registration from")
    l2.config(font=(font_family, 13))
    l2.pack(pady=10)

    l3 = Label(window2, text="Name")
    l3.config(font=(font_family, 11))
    l3.pack(pady=(10, 0))

    name_text = StringVar()
    e1 = Entry(window2, textvariable=name_text, width=35)
    e1.config(font=(font_family, 12))
    e1.pack(pady=(0, 0))
    
    l5 = Label(window2, text='')
    l5.config(font=(font_family, 11))
    l5.pack(pady=(0, 0))
    
    # if name_exists:
    #     print('good to go')
    # else:
    #     print('Already used')

    l4 = Label(window2, text="Number of Bikes to Book")
    l4.config(font=(font_family, 11))
    l4.pack(pady=(10, 0))

    number_bikes_text = StringVar()
    e2 = Entry(window2, textvariable=number_bikes_text, width=35)
    e2.config(font=(font_family, 12))
    e2.pack(pady=(0, 30))

    b1 = Button(window2, text='Submit', width=20,
                height=2, command=store_to_db)
    b1.config(font=(font_family, 12))
    b1.pack()
    
    print(name_text.get())

    window2.mainloop()


# request_bike()
