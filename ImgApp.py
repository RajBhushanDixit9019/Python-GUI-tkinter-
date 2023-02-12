# this is a image app in python using tkinter.
from tkinter import *
from PIL import ImageTk,Image

root=Tk()

# functions
def forward(imgnum):
    global my_label,btn_back,btn_forward
    if(imgnum==8):
        btn_back=Button(root,text="->", state=DISABLED)
    my_label=Label(image=img_list[imgnum+1]).grid(row=0,column=0,columnspan=3)
    btn_forward=Button(root,text="->",command=lambda: forward(imgnum+1)).grid(row=1,column=1)
    btn_back=Button(root,text="<-",command=lambda: back(imgnum-1)).grid(row=1,column=0)
def back(imgnum):
    global my_label,btn_back,btn_forward
    if(imgnum==8):
        btn_back=Button(root,text="->", state=DISABLED)
    my_label=Label(image=img_list[imgnum+1]).grid(row=0,column=0,columnspan=3)
    btn_forward=Button(root,text="->",command=lambda: forward(imgnum+1)).grid(row=1,column=1)
    btn_back=Button(root,text="<-",command=lambda: back(imgnum-1)).grid(row=1,column=0)

# Out look of ImgApp
root.title("Image App")
#root.geometry('720x360')

# Images
img_py=ImageTk.PhotoImage(Image.open("images/python.png"))
img_cpp=ImageTk.PhotoImage(Image.open("images/C++.png"))
img_css=ImageTk.PhotoImage(Image.open("images/CSS.png"))
img_html=ImageTk.PhotoImage(Image.open("images/HTML.png"))
img_java=ImageTk.PhotoImage(Image.open("images/Java.png"))
img_js=ImageTk.PhotoImage(Image.open("images/JavaScript.png"))
img_php=ImageTk.PhotoImage(Image.open("images/PHP.png"))
img_xml=ImageTk.PhotoImage(Image.open("images/XML.png"))

# image list
img_list=[img_py,img_cpp,img_css,img_html,img_java,img_js,img_php,img_xml]

# displaying the images on the screen
#py_label=Label(image=img_py).grid(row=0,column=0,columnspan=3)


# buttons
btn_back=Button(root,text="<-", command=back).grid(row=1,column=0)
btn_forward=Button(root,text="->", command=lambda: forward(2)).grid(row=1,column=1)
btn_exit=Button(root,text="X",command=root.quit).grid(row=1,column=2)
root.mainloop()