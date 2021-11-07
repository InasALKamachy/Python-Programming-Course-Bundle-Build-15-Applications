from tkinter import *

App = Tk()
App.title("check_box")
App['background'] = 'pink'
check = IntVar()

chk = Checkbutton(App, text = 'check_here',  variable = check)
chk.pack()

def show():
    msg = Label(App,text=check.get())
    msg.pack()
B = Button(App, text = 'show', command = show)
B.pack()
App.mainloop()



##########################################

from tkinter import *

App = Tk()
App.geometry('200x100')
App.title("check_box")
App['background'] = 'pink'
check = StringVar()

chk = Checkbutton(App, text = 'check_here',  onvalue = 'Yes',offvalue = 'No', variable = check)
chk.deselect()
chk.pack()


def show():
    msg = Label(App,text=check.get())
    msg.pack()
B = Button(App, text = 'show', command = show)
B.pack()
App.mainloop()

#############################################
###built check box to choose two value :

import random
from tkinter import *
from random import *
App = Tk()
App['background'] = '#2A3638'
App.title('Dice_App') # title in taskbar
App.geometry('250x100')#size of window
Inp1 = Entry(App, background = '#E84A5F', foreground = '#FECEAB') ##input
Inp1.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)

check =IntVar()
chk = Checkbutton(App, text = 'Double',  onvalue = 2,offvalue = 1, variable = check)
chk.deselect()
chk.grid(row = 1, column = 0, columnspan = 2, padx = 25, pady = 5)

def chose():
    inp = (Inp1.get()).split(',')
    if check.get() == 2:
        ele = sample(inp, 2)
        choic = ('The Choice is :'+str(ele[0])+' AND '+str(ele[1]))
    else:
        ele = sample(inp,1)
        choic = ('The Choice is :' + str(ele[0]))
    msg = Label(App, text=choic, font = ('Courier',10), background = '#E84A5F', foreground = '#FECEAB', relief = 'raise', width = 30, borderwidth = 4)# or ridge or raise or sunken or flat or groove

    msg.grid(row = 2, column = 0, padx = 25, pady = 5, columnspan = 2)
    if quit['stat'] == DISABLED:
        quit['stat']=NORMAL




A = Button(App, text = 'Choose', command=chose, background = '#FF847C', foreground = '#FECEAB',relief = 'groove', borderwidth = 4)
A.grid(row = 3, column = 0, padx = 25, pady = 5)

quit = Button(App, text = 'Cancel', command=App.quit, stat = DISABLED, background = 'red', foreground = '#FECEAB', borderwidth = 4)
quit.grid(row = 3, column = 1, padx = 25, pady = 5)
App.mainloop()# must be at the endd
