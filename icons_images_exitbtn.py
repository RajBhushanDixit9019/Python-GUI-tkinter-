# this python code is to liiustrate about icons, images and exit button in python using tkinter.
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons, Images and Exit button")

# adding icon..
p1 = PhotoImage(file='python.png')
root.iconphoto(False, p1)

# adding exit button..
Button(root, text="Click to Exit", command=root.quit).pack()

# adding images
Label(root, text="Below is the pyhton icon images").pack()
pyimg = ImageTk.PhotoImage(Image.open("python.png"))
Label(image=pyimg).pack()
root.mainloop()
