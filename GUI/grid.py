import random
from tkinter import *
from random import *
App = Tk()
App.title('Dice_App') # title in taskbar
App.geometry('400x100')#size of window
Inp = Entry(App) ##input
Inp.grid(row = 0, column = 0, columnspan = 2)
def random_():
    Display = Label(App, text=randint(1,6))  # title in main window
    Display.grid(row = 3, column = 0)
def show():
    inp = Inp.get()
    msg = Label(App, text=inp)
    msg.grid(row = 3, column = 1)

Inp1 = Entry(App) ##input
Inp1.grid(row = 0, column = 2, columnspan = 2)

def chose():
    inp = (Inp1.get()).split(',')
    msg = Label(App, text=choice(inp))
    msg.grid(row = 3, column = 2)


B = Button(App, text = 'Click', command=random_)
B.grid(row = 1, column = 0)

A = Button(App, text = 'Show', command=show)
A.grid(row = 1, column = 1)

A = Button(App, text = 'Choose', command=chose)
A.grid(row = 1, column = 2)

quit = Button(App, text = 'Cancel', command=App.quit)
quit.grid(row = 1, column = 3)
App.mainloop()# must be at the end
