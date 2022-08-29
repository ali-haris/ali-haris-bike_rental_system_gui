
from tkinter import *
from tkinter import messagebox
from DataBase import conn_db as db
from datetime import datetime as dt
import final_message as fnl


def return_bikes():

    def core_func():
        result = db.to_search(name_text.get(), id_text.get())
        print(result)

        if result:
            print('result found')
            db.to_update_return_time(id_text.get(), dt.now())
            total_time = dt.strptime(db.to_search(name_text.get(), id_text.get())[
                                    0][4], '%Y-%m-%d %H:%M:%S.%f')-dt.strptime(db.to_search(name_text.get(), id_text.get())[0][3], '%Y-%m-%d %H:%M:%S.%f')
            global cost, number_bikes_used
            number_bikes_used = db.to_search(
                name_text.get(), id_text.get())[0][2]
            cost = round(total_time.seconds/60 * 5 * number_bikes_used)
            db.to_update_cost(id_text.get(), cost)
            print(cost, number_bikes_used)
            window3.destroy()
            fnl.message_return_final()

        else:
            messagebox.showerror('Try Again', f"Data not found.")


    font_family = "Roman"

    window3 = Tk()
    window3.wm_title('Request a Bike')
    window3.geometry("550x300")

    l = Label(window3, text="Bikes are return here")
    l.config(font=(font_family, 15))
    # l.grid(row=1,column=1)
    l.pack(side=TOP, pady=10)

    l2 = Label(window3, text="Fill the from")
    l2.config(font=(font_family, 13))
    l2.pack(pady=10)

    l3 = Label(window3, text="Name")
    l3.config(font=(font_family, 11))
    l3.pack(pady=(10, 0))

    name_text = StringVar()
    e1 = Entry(window3, textvariable=name_text, width=35)
    e1.config(font=(font_family, 12))
    e1.pack(pady=(0, 10))

    l4 = Label(window3, text="Booking ID")
    l4.config(font=(font_family, 11))
    l4.pack(pady=(10, 0))

    id_text = StringVar()
    e2 = Entry(window3, textvariable=id_text, width=35)
    e2.config(font=(font_family, 12))
    e2.pack(pady=(0, 30))

    b1 = Button(window3, text='Submit', width=20, height=2, command=core_func)
    b1.config(font=(font_family, 12))
    b1.pack()

    #pack(padx=5, pady=15, side=tk.LEFT)

    window3.mainloop()
