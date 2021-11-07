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
