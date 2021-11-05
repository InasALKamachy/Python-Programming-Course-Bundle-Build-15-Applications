import random
from tkinter import *
from random import *
App = Tk()
App.title('Dice_App') # title in taskbar
App.geometry('400x100')#size of window
Inp = Entry(App) ##input
Inp.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)
def random_():
    Display = Label(App, text=randint(1,6))  # title in main window
    Display.grid(row = 3, column = 0, padx = 25, pady = 5)
def show():
    inp = Inp.get()
    msg = Label(App, text=inp)
    msg.grid(row = 3, column = 1, padx = 25, pady = 5)

Inp1 = Entry(App) ##input
Inp1.grid(row = 0, column = 2, columnspan = 2, padx = 25, pady = 5)

def chose():
    inp = (Inp1.get()).split(',')
    choic = ('The Choice is :'+str(choice(inp)))
    msg = Label(App, text=choic)
    msg.grid(row = 0, column = 5, padx = 25, pady = 5)


B = Button(App, text = 'Click', command=random_)
B.grid(row = 1, column = 0, padx = 25, pady = 5)

A = Button(App, text = 'Show', command=show)
A.grid(row = 1, column = 1, padx = 25, pady = 5)

A = Button(App, text = 'Choose', command=chose)
A.grid(row = 1, column = 2, padx = 25, pady = 5)

quit = Button(App, text = 'Cancel', command=App.quit)
quit.grid(row = 1, column = 3, padx = 25, pady = 5)
App.mainloop()# must be at the end
