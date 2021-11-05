from tkinter import *

App = Tk()
App.title('My First App') # title in taskbar
App.geometry('100x100')#size of window

def gree_():
    Display = Label(App, text='Have a Nice Day!')  # title in main window
    Display.pack()
    

B = Button(App, text = 'Click', command=gree_) 
B.pack()
App.mainloop()# must be at the end
