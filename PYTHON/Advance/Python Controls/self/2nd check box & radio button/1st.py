from Tkinter import *

def showCheckValue():
    a=""
    b=""
    if(CheckVar1.get()==1):
        a=a+" Programming"
    if(CheckVar2.get()==1):
        a=a+" Sports"

    if(var.get()==1):
        b="Male"
    elif(var.get()==2):
        b="FeMale"
    else:
        b="Third Gender "

    print "Hobbies ",a
    print "Gender ",b
    
top = Tk()
var = IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

l2=Label(top,text="Enter Your Name ")
l2.pack()
t1=Text(top,width=30, height=1)
t1.pack()
l3=Label(top,text="Enter Your Father Name ")
l3.pack()
t2=Text(top,width=30, height=1)
t2.pack()
l4=Label(top,text="Enter Your Name ")
l4.pack()
t3=Text(top,width=30, height=1)
t3.pack()

L1 = Label(top,text="GENDER")
L1.pack()
rb1 = Radiobutton(top, text="Male", variable=var, value=1)
rb1.pack()
rb2 = Radiobutton(top, text="Female ", variable=var, value=2)
rb2.pack()
rb3 = Radiobutton(top, text="Third Gender", variable=var, value=3)
rb3.pack()

l5=Label(top,text="Hobbies")
l5.pack()
C1 = Checkbutton(top, text = "Programming ", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 20)
C2 = Checkbutton(top, text = "Sports ", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 20)
C1.pack()
C2.pack()

b1=Button(top,text="Click me",height=5, width=10,command=showCheckValue)
b1.pack()
top.mainloop()
