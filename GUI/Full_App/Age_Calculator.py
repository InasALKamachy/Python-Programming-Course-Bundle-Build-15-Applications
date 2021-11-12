from tkinter import *
from datetime import *

App = Tk()
App.title('Age Calculator')

def day_():
    d = int(input("Enter THe day of your birth: "))
    return d
def month_():
    d = int(input("Enter THe month of your birth: "))
    return d
def year_():
    d = int(input("Enter THe year of your birth: "))
    return d

lbl_day = Label(App, text='Day')
lbl_day.grid(row = 0, column = 0, padx = 25, pady = 5)
Inp_day = Entry(App) ##input
Inp_day.grid(row = 0, column = 1, padx = 25, pady = 5)

lbl_month = Label(App, text = 'Month')
lbl_month.grid(row = 1, column = 0, padx = 25, pady = 5)
Inp_month = Entry(App) ##input
Inp_month.grid(row = 1, column = 1, padx = 25, pady = 5)


lbl_year = Label(App)
lbl_year.grid(row = 2, column = 0, padx = 25, pady = 5)
Inp_year = Entry(App) ##input
Inp_year.grid(row = 2, column = 1, padx = 25, pady = 5)

def show():
    inp_day = int(Inp_day.get())
    inp_month = int(Inp_month.get())
    inp_year = int(Inp_year.get())
    birth = datetime(inp_year, inp_month, inp_day)
    Time = datetime.now()
    full_birth = Time - birth
    msg = Label(App, text = 'you live about' +str((full_birth.days)/360)+' days!')
    msg.grid(row=1, column=3)

def show_min():
    inp_day = int(Inp_day.get())
    inp_month = int(Inp_month.get())
    inp_year = int(Inp_year.get())
    birth = datetime(inp_year, inp_month, inp_day)
    Time = datetime.now()
    full_birth = (Time - birth)/360
    msg = Label(App, text = full_birth.seconds)
    msg.grid(row=1, column=2)


B = Button(App, text='Calculate minutes', command = show_min)
B.grid(row = 0, column = 2, padx = 25, pady = 5)

A = Button(App, text='Calculate Now', command = show)
A.grid(row = 0, column = 3, padx = 25, pady = 5)

lbl_result = Label(App, text='year')
lbl_result.grid(row = 2, column = 0, padx = 25, pady = 5)

App.mainloop()
