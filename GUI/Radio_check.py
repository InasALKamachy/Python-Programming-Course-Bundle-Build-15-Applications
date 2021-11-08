from random import *
from tkinter import *

App = Tk()
App['background'] = '#2A3638'
App.title('Dice_App') # title in taskbar
App.geometry('250x100')#size of window

inp = Entry(App,width = 50)
App.geometry('220x150')
radio_choice = IntVar()
rb1 = Radiobutton(App, text = 'Option 1', variable = radio_choice, value = 1)
rb2 = Radiobutton(App, text = 'Option 2', variable = radio_choice, value = 2)
rb1.deselect()
rb1.grid(row = 0, column = 0)
rb2.deselect()
rb2.grid(row = 0, column = 1)

def show():
    msg = Label(App, text = radio_choice.get())
    msg.grid(row = 4, column = 1)

C = Button(App, text = 'Radio_', command=show, background = '#FF847C', foreground = '#FECEAB',relief = 'groove', borderwidth = 4)
C.grid(row = 4, column = 0, padx = 25, pady = 5)
App.mainloop()
