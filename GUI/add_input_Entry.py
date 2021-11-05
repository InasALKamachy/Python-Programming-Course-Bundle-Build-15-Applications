import random
from tkinter import *
from random import *
App = Tk()
App.title('Dice_App') # title in taskbar
App.geometry('400x100')#size of window
Inp = Entry(App) ##input 
Inp.pack()
def random_():
    Display = Label(App, text=randint(1,6))  # title in main window
    Display.pack()
def show():
    inp = Inp.get()
    msg = Label(App, text=inp)
    msg.pack()


B = Button(App, text = 'Click', command=random_)
B.pack()

A = Button(App, text = 'Show', command=show)
A.pack()

App.mainloop()# must be at the end
