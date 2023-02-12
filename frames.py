# this python code is to impliment frames in python using tkinter
from tkinter import *
from PIL import Image,ImageTk

# initials..
app=Tk()
app.title("Frames")
app.geometry('720x360')

# click functionality
#def click():
#    l=Label(frame,text="Button is clicked!")
 #   l.pack()
  #  print("Button is clicked!")
# Frame...
frame=LabelFrame(app,text="This is the frame!",padx=1,pady=1,)
frame.pack(padx=100,pady=100)

# simple button
b=Button(frame,text="click!").grid(row=0,column=0)
b1=Button(frame,text="click1").grid(row=1,column=1)
app.mainloop()