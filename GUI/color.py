#The following str literals can be used either for the foreground or background parameter:

white

black

red

pink

purple

magenta

blue

cyan

grey

green

orange

brown

silver

gold

make sure to use them without capitalization as 'silver'


import random
from tkinter import *
from random import *
App = Tk()
App['background'] = '#2A3638'
App.title('Dice_App') # title in taskbar
App.geometry('400x100')#size of window
Inp = Entry(App, background = '#E84A5F', foreground = '#FECEAB') ##input
Inp.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)
def random_():
    Display = Label(App, text=randint(1,6), font = ('Courier',10), background = '#E84A5F', foreground = '#FECEAB')  # title in main window
    Display.grid(row = 3, column = 0, padx = 25, pady = 5)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL

def show():
    inp = Inp.get()
    msg = Label(App, text=inp, font = ('Courier',10), background = '#E84A5F', foreground = '#FECEAB')
    msg.grid(row = 3, column = 1, padx = 25, pady = 5)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL

Inp1 = Entry(App, background = '#E84A5F', foreground = '#FECEAB') ##input
Inp1.grid(row = 0, column = 2, columnspan = 2, padx = 25, pady = 5)

def chose():
    inp = (Inp1.get()).split(',')
    choic = ('The Choice is :'+str(choice(inp)))
    msg = Label(App, text=choic, font = ('Courier',10), background = '#E84A5F', foreground = '#FECEAB')
    msg.grid(row = 0, column = 5, padx = 25, pady = 5)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL





B = Button(App, text = 'Click', command=random_,  background = '#FF847C', foreground = 'black')
B.grid(row = 1, column = 0, padx = 25, pady = 5)

A = Button(App, text = 'Show', command=show, background = '#FF847C', foreground = '#FECEAB')
A.grid(row = 1, column = 1, padx = 25, pady = 5)

A = Button(App, text = 'Choose', command=chose, background = '#FF847C', foreground = '#FECEAB')
A.grid(row = 1, column = 2, padx = 25, pady = 5)

quit = Button(App, text = 'Cancel', command=App.quit, stat = DISABLED, background = 'red', foreground = '#FECEAB')
quit.grid(row = 1, column = 3, padx = 25, pady = 5)
App.mainloop()# must be at the end
