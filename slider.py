from tkinter import *
App = Tk()
sld_val = IntVar()
sld = Scale(App, from_=0, to=100, variable = sld_val)
sld.pack()
def show():
    msg = Label(App, text = sld_val.get())
    msg.pack()

B = Button(App, text = 'show', command = show)
B.pack()

App.mainloop()
