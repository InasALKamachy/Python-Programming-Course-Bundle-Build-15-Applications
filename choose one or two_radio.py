from tkinter import *
from random import *

App = Tk()
App.title('Element Picker')

inp = Entry(App, width = 25)
inp.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 5)

no_choice = IntVar()
rb1 = Radiobutton(App, text = '1', variable = no_choice, value = 1)
rb2 = Radiobutton(App, text = '2', variable = no_choice, value = 2)
rb1.deselect()
rb2.deselect()
rb1.grid(row = 1, column = 0)
rb2.grid(row = 1, column = 1)

def pick():
    INP = (inp.get()).split(',')
    if no_choice.get()==2:
        ele = sample(INP,2)
        chois = 'Choice: ' + str(ele[0])+' '+str(ele[1])
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
