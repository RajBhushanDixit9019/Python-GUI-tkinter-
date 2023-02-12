# this python code is to illustrate about the message box in python using tkinter
from tkinter import *
from tkinter import messagebox

# app initials
app=Tk()
app.title("Message Box")
app.geometry('700x400')

# function
def popup():
    messagebox.showinfo("Pop-up Message!","Hello")
    print("Pop button is clicked")
    
def waring():
    messagebox.showwarning("Waring!","Hello")
    print("waring button is clicked")

def error():
    messagebox.showerror("Error!","Hello") 
    print("Error button is clicked")

def askquestion():
    messagebox.askquestion("Ask Question!","Hello")
    print("AskQuestion button is clicked")
    
def askokcancel():
    messagebox.askokcancel("Ask Ok Cancel!","Hello")
    print("AskOkCancel button is clicked")

def askyesno():
    messagebox.askyesno("Ask Yes No!","Hello") 
    print("AskYesNo button is clicked")

# button
# showinfo,showwaring,showerror,askquestion,askokcancel,askyesno.
popupbtn=Button(app,text="pop up",command=popup).pack(padx=10,pady=10)
warningbtn=Button(app,text="warning",command=waring).pack(padx=10,pady=10)
errorbtn=Button(app,text="Error",command=error).pack(padx=10,pady=10)
askquestionbtn=Button(app,text="AskQuestions",command=askquestion).pack(padx=10,pady=10)
askokcancelbtn=Button(app,text="AskOkCancel",command=askokcancel).pack(padx=10,pady=10)
askyesnobtn=Button(app,text="AskYesNo",command=askyesno).pack(padx=10,pady=10)

# mainloop
app.mainloop()