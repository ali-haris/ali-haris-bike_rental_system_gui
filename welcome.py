#Welcom to the bike rental system
from tkinter import *
from request_bike import *
from return_bike import *
#from bikeRental import *


def request_command():
    window1.destroy()

    request_bike()


def return_command():
    window1.destroy()
    return_bikes()


def interface():

    font_family = "Roman"
    global window1
    window1 = Tk()
    window1.wm_title('Bike Rental System')
    window1.geometry("550x300")

    l = Label(window1, text="Welcome to Bike Rental System")
    l.config(font=(font_family, 14))
    # l.grid(row=1,column=1)
    l.pack(side=TOP, pady=20)

    b1 = Button(window1, text='Request a Bike', width=20,
                height=3, command=request_command)
    b1.config(font=(font_family, 12))
    b1.pack(pady=10)

    b2 = Button(window1, text='Return a Bike', width=20,
                height=3, command=return_command)
    b2.config(font=(font_family, 12))
    b2.pack(pady=15)

    window1.mainloop()


if __name__ == '__main__':

    interface()
