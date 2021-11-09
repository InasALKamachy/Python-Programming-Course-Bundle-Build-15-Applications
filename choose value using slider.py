from tkinter import *
from random import *

App = Tk()
App.title('Element Picker')

inp = Entry(App, width = 25)
inp.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)

sld_val = IntVar()
sld = Scale(App, from_=0, to=100, variable = sld_val, orient = HORIZONTAL)
sld.grid(row = 1, column = 2, columnspan = 2)

def pick():
    INP = (inp.get()).split(',')

    if sld_val.get()!=1:
        ele = sample(INP,sld_val.get())
        lab = ''
        for e in ele:
            lab += ' '+e
        chois = 'Choice: ' + str(lab)
    else:
        chois = 'Choise: '+str(choice(INP))

    msg = Label(App, text = chois, width=30, relief=RAISED )
    msg.grid(row=4, column=0, columnspan=2, padx=30, pady=5)

    if quit['state'] == DISABLED:
        quit['stat'] ==NORMAL


A = Button(App, text = 'Choose', command=pick, background = '#FF847C', foreground = '#FECEAB',relief = 'groove', borderwidth = 4)
A.grid(row = 3, column = 0, padx = 25, pady = 5)

quit = Button(App, text = 'Cancel', command=App.quit, stat = DISABLED, background = 'red', foreground = '#FECEAB', borderwidth = 4)
quit.grid(row = 3, column = 1, padx = 25, pady = 5)
App.mainloop()# must be at the endd
