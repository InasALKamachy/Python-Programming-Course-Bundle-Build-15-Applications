import random
from tkinter import *
from random import *
App = Tk()
App['background'] = '#2A3638'
App.title('Dice_App') # title in taskbar
App.geometry('250x100')#size of window
Inp1 = Entry(App, background = '#E84A5F', foreground = '#FECEAB') ##input
Inp1.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)

def chose():
    inp = (Inp1.get()).split(',')
    choic = ('The Choice is :'+str(choice(inp)))
    msg = Label(App, text=choic, font = ('Courier',10), background = '#E84A5F', foreground = '#FECEAB', relief = 'raise', width = 25, borderwidth = 4)# or ridge or raise or sunken or flat or groove

    msg.grid(row = 2, column = 0, padx = 25, pady = 5, columnspan = 2)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL



A = Button(App, text = 'Choose', command=chose, background = '#FF847C', foreground = '#FECEAB',relief = 'groove', borderwidth = 4)
A.grid(row = 1, column = 0, padx = 25, pady = 5)

quit = Button(App, text = 'Cancel', command=App.quit, stat = DISABLED, background = 'red', foreground = '#FECEAB', borderwidth = 4)
quit.grid(row = 1, column = 1, padx = 25, pady = 5)
App.mainloop()# must be at the end
