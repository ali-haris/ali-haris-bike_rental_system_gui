

from tkinter import *
import request_bike
import return_bike
from return_bike import *
from DataBase import conn_db as db
import welcome


def back_request():
    window4.destroy()
    welcome.interface()

def back_return():
    window5.destroy()
    welcome.interface()


def message_request_final():

    # test_var = 'hi test var'

    font_family = "Roman"
    global window4
    window4 = Tk()
    window4.wm_title('Return a Bike')
    window4.geometry("550x300")

    l = Label(window4, text="Thanks for using our service")
    l.config(font=(font_family, 14))
    # l.grid(row=1,column=1)
    l.pack(side=TOP, pady=(30, 0))

    l2 = Label(
        window4, text=f"Hi {request_bike.current_user_name},You have rented {request_bike.current_user_bikes} bikes at \n$5 per hour")
    l2.config(font=(font_family, 13))
    l2.pack(pady=10)

    l4 = Label(
        window4, text=f"User Name: {request_bike.current_user_name} \nYour ID: {db.to_search_id_in_db(request_bike.current_user_name,request_bike.current_user_bikes)[0][0]} ")
    l4.config(font=(font_family, 11))
    l4.pack(pady=(5, 30))

    b1 = Button(window4, text='Return To Shop',
                width=20, height=2, command=back_request)
    b1.config(font=(font_family, 12))
    b1.pack()

    b2 = Button(window4, text='Close', width=20,
                height=2, command=window4.destroy)
    b2.config(font=(font_family, 12))
    b2.pack(pady=(10, 0))

    #pack(padx=5, pady=15, side=tk.LEFT)
    window4.mainloop()

# message_request_final()


def message_return_final():
    font_family = "Roman"
    global window5
    window5 = Tk()
    window5.wm_title('Return a Bike')
    window5.geometry("550x300")

    l = Label(window5, text="Thanks for using our service")
    l.config(font=(font_family, 15))
    # l.grid(row=1,column=1)
    l.pack(side=TOP, pady=(40, 0))

    l2 = Label(
        window5, text="Thanks for returning the bike. Hope you \n enjoyed our service!")
    l2.config(font=(font_family, 13))
    l2.pack(pady=10)

    l4 = Label(
        window5, text=f"Total Cost is {return_bike.cost}$ \n You Returned {return_bike.number_bikes_used}")
    l4.config(font=(font_family, 11))
    l4.pack(pady=(5, 30))

    b1 = Button(window5, text='Return To Shop', width=20, height=2,command=back_return)
    b1.config(font=(font_family, 12))
    b1.pack()

    b2 = Button(window5, text='Close', width=20,
                height=2, command=window5.destroy)
    b2.config(font=(font_family, 12))
    b2.pack(pady=(10, 0))

    #pack(padx=5, pady=15, side=tk.LEFT)

    window5.mainloop()

# message_return_final()
