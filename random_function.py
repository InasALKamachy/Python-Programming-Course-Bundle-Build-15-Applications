import random
from tkinter import *
from random import *
App = Tk()
App.title('Dice_App') # title in taskbar
App.geometry('400x100')#size of window

def random_():
    Display = Label(App, text=randint(1,6))  # title in main window
    Display.pack()


B = Button(App, text = 'Click', command=random_)
B.pack()
App.mainloop()# must be at the end
