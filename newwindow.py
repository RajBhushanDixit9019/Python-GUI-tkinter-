# this python code is to create the new windows using tkinter
from tkinter import *

# app initials
app=Tk()
app.title('New window')
app.geometry('300x300')

def open():
    # top level function
    top=Toplevel()
    top.geometry('200x200')
    l=Label(top,text="This is a new window").pack()
    btn=Button(top,text="Exit",command=top.quit).pack()

openbtn=Button(app,text='Open new window',command=open).pack()
# mainloop
app.mainloop()