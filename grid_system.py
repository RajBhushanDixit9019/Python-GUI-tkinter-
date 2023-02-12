# this python code is illustrate the grid system using tkinter..
from tkinter import *
raj = Tk()
raj.title("Grid system")
# creating the label to illustrate the grid system..
rajlabel = Label(raj, text="Raj").grid(row=0, column=0)
karanlabel = Label(raj, text="Karan").grid(row=1, column=5)

# moving the mylabel using the grid() methon..
# rajlabel.grid(row=0, column=0)
# karanlabel.grid(row=1, column=5)
raj.mainloop()
