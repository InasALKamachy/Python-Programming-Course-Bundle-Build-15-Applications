from tkinter import *

App = Tk()
App.title('My First App') # title in taskbar
App.geometry('100x100')#size of window
Display = Label(App, text='The main window') # title in main window
Display.pack()
App.mainloop()# must be at the end
