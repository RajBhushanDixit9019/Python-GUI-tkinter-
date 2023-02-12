# this python code is to create a calculator in python using tkinter...
from tkinter import *
root=Tk()
def click(number):
    #e.delete(0,END)
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c) + str(number))
def clear():
    e.delete(0,END) 
def calc():
    exp=e.get()
    e.delete(0,END)
    e.insert(0,eval(exp))
root.title("Raj's Calculator")  
# input feild..
e=Entry(root,width=70,borderwidth=5,bg="aqua")
e.grid(row=0,column=0, columnspan=4)

#Defining Buttons...

# number buttons..
btn1=Button(root,text="1",padx=40,pady=20, command=lambda:click("1"), borderwidth=5,fg="brown",bg="blue",activebackground='green')
btn2=Button(root,text="2",padx=40,pady=20, command=lambda:click("2"), borderwidth=5,fg="brown",bg="blue", activebackground='green')
btn3=Button(root,text="3",padx=40,pady=20, command=lambda:click("3"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn4=Button(root,text="4",padx=40,pady=20, command=lambda:click("4"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn5=Button(root,text="5",padx=40,pady=20, command=lambda:click("5"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn6=Button(root,text="6",padx=40,pady=20, command=lambda:click("6"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn7=Button(root,text="7",padx=40,pady=20, command=lambda:click("7"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn8=Button(root,text="8",padx=40,pady=20, command=lambda:click("8"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn9=Button(root,text="9",padx=40,pady=20, command=lambda:click("9"), borderwidth=5, fg="brown",bg="blue", activebackground='green')
btn0=Button(root,text="0",padx=40,pady=20, command=lambda:click("0"), borderwidth=5,fg="brown",bg="blue",activebackground='green')
btn_add=Button(root,text="+", padx=40, pady=20, command=lambda:click("+"), borderwidth=5,fg="red",bg="grey",activebackground='yellow')
btn_sub=Button(root,text="-", padx=40, pady=20, command=lambda:click("-"), borderwidth=5, fg="red",bg="grey", activebackground='yellow')
btn_mult=Button(root,text="x", padx=40, pady=20, command=lambda:click("*"), borderwidth=5, fg="red",bg="grey", activebackground='yellow')
btn_div=Button(root,text="÷", padx=40, pady=20, command=lambda:click("/"), borderwidth=5, fg="red",bg="grey", activebackground='yellow')
btn_mod=Button(root,text="%", padx=40, pady=20, command=lambda:click("%"), borderwidth=5,fg="red",bg="grey", activebackground='yellow')

# operator Buttons..
btn_equal=Button(root,text="=", padx=40, pady=20, command=calc, borderwidth=5,fg="red",bg="grey",activebackground='brown')
btn_clear=Button(root,text="CE", padx=100, pady=20,command=clear, borderwidth=5,fg="black",bg="red", activebackground='brown')
# showing the buttons on the screen..

# 1st row
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn_sub.grid(row=3, column=3)

# 2nd row
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn_mult.grid(row=2, column=3)

# 3rd row
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn_div.grid(row=1, column=3)

# 4th row
btn_add.grid(row=4,column=0)
btn0.grid(row=4,column=1)
btn_equal.grid(row=4,column=2)
btn_mod.grid(row=4, column=3)

# 5th row
btn_clear.grid(row=5,column=0,columnspan=6)
root.mainloop()