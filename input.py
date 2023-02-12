# this python code is to illustrate the Entry widgets(input) in python using tkinter...
from tkinter import *
raj=Tk()
raj.title("User Input")
#creating entry widgets
e=Entry(raj, width=25, fg="Red", bg="lightgreen", borderwidth=5)
e.pack()
def click():
    txt="Hello "+e.get()
    inlabel=Label(raj, text=txt)
    inlabel.pack()
    e.delete(0, END)
#def clear():
    #inlabel.insert(0,"")
btn=Button(raj, text="Enter", command=click).pack()
#btn1=Button(raj, text="Clear", command=clear).pack()
raj.mainloop()