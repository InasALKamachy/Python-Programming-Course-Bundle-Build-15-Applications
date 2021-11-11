
from tkinter import *
from tkinter import filedialog
from PIL import Image ,ImageTk


app = Tk()
app.title('App')
app['background'] = '#2A3638'
app.iconphoto(True, PhotoImage(file="dd.png"))

def img_select():
    global img
    app.fname = filedialog.askopenfilename(
      initialdir = 'res', title='Select a image', filetypes = (
            ('PNG Files','*.png'),('ICON FIle','*.ico'), ('All Files','*.*')
      ))
    B.destroy()
    img = ImageTk.PhotoImage(Image.open(app.fname))
    lbl = Label(app, image = img)
    lbl.pack()

B = Button(app, text = 'veiw image', command = img_select)
B.pack()
app.mainloop()


app.mainloop()
