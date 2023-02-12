# this python code is to create the blank window in python using tkinter..
from tkinter import *

# to use any GUI component we have to create object for is so, root is object for this...
root = Tk()

root.title("Hello")
# this how we display the text or label in python using tkinter..
Label(root, text="Hello Raj Bhushan Dixit").pack()

# this mainloop method is used to run the screen on until we close it..
root.mainloop()