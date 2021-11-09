from tkinter import *
App = Tk()
App.geometry('300x200')
option_menue= StringVar()
lst = ['red', 'white', 'green']
sld = OptionMenu(App, option_menue, *lst)
option_menue.set('white')
sld.pack()
def show():
    msg = Label(App, text = ' ', background = (option_menue.get()).lower())
    msg.pack()

B = Button(App, text = 'show', command = show)
B.pack()

App.mainloop()
