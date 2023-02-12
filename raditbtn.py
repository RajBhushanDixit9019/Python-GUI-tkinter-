# this python code is to illustrate about the radio buttons in python using tkinter
from tkinter import *

# initilas
app=Tk()
app.title("Radio Button")
#app.geometry('100x100')

#variable
#r=IntVar()
#r.set("2")

# list
modes=[
    # (text,mode)
    ("Pepparoni","Pepparoni"),
    ("Cheese","Cheese"),
    ("Paneer","Paneer"),
    ("Onion","Onion"),
]

# valrable
pizza=StringVar()
pizza.set("Pepparoni")

# loop
for text,mode in modes:
   Radiobutton(app,text=text,variable=pizza,value=mode).pack() 



#function definations
def click(value):
    l=Label(app,text=value).pack()

#Radio button
#Radiobutton(app,text="option 1",variable=r,value=1,command=lambda:click(r.get())).pack()
#Radiobutton(app,text="option 2",variable=r,value=2,command=lambda:click(r.get())).pack()
#Radiobutton(app,text="option 3",variable=r,value=3,command=lambda:click(r.get())).pack()

#label
#l=Label(app,text=pizza.get()).pack()

# button
btn=Button(app,text="click",command=lambda:click(pizza.get())).pack()

# main loop
app.mainloop()