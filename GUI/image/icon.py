
### this code work just in replit or windows 

from tkinter import *
from PIL import Image ,ImageTk


app = Tk()
app.title('App')
app['background'] = '#2A3638'
app.iconphoto(True, PhotoImage(file="res/python1.png"))

img = ImageTk.PhotoImage(Image.open('res/python1.png' ))
lbl = Label(app, image=img)
lbl.pack()



app.mainloop()
