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
App['background'] = 'blue'
App.title('Dice_App') # title in taskbar
App.geometry('400x100')#size of window
Inp = Entry(App, background = 'yellow', foreground = 'black') ##input
Inp.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)
def random_():
    Display = Label(App, text=randint(1,6), font = ('Courier',14))  # title in main window
    Display.grid(row = 3, column = 0, padx = 25, pady = 5)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL

def show():
    inp = Inp.get()
    msg = Label(App, text=inp, font = ('Courier',14))
    msg.grid(row = 3, column = 1, padx = 25, pady = 5)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL

Inp1 = Entry(App, background = 'red', foreground = 'black') ##input
Inp1.grid(row = 0, column = 2, columnspan = 2, padx = 25, pady = 5)

def chose():
    inp = (Inp1.get()).split(',')
    choic = ('The Choice is :'+str(choice(inp)))
    msg = Label(App, text=choic, font = ('Courier',14), background = 'white', foreground = 'blue')
    msg.grid(row = 0, column = 5, padx = 25, pady = 5)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL





B = Button(App, text = 'Click', command=random_,  background = 'purple', foreground = 'black')
B.grid(row = 1, column = 0, padx = 25, pady = 5)

A = Button(App, text = 'Show', command=show)
A.grid(row = 1, column = 1, padx = 25, pady = 5)

A = Button(App, text = 'Choose', command=chose)
A.grid(row = 1, column = 2, padx = 25, pady = 5)

quit = Button(App, text = 'Cancel', command=App.quit, stat = DISABLED)
quit.grid(row = 1, column = 3, padx = 25, pady = 5)
App.mainloop()# must be at the end
