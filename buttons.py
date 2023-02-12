# this python code is to illustrate the about the button in python using tkinter...
from tkinter import *

raj = Tk()
# difining a function to do something..
raj.title("Buttons")


def click():
    label = Label(raj, text="click Button is clicked!", fg="green", bg="lightgrey").pack()
def clear():
    label = Label(raj, text="Size buttion is clicked!", fg="red", bg="lightgrey").pack()



# button..
mybutton = Button(raj, text="Click here!", command=click, fg="red", bg="lightblue", cursor="dot").pack()

# disabled button
# mybutton = Button(raj, text="Click here!", state=DISABLED)

# sizing the buttons..
mybutton1 = Button(raj, text="Size", padx=50, pady=50, highlightcolor="lightgreen", command=clear).pack()
raj.mainloop()
