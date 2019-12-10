from Tkinter import*

def college():
    if(var.get()==1):
        a="dean"
    elif(var.get()==2):
        a="teacher"
    else:
        a="student"
    L1.config(text=a)
top=Tk()
var=IntVar()

L1=Label(top,text="college")
L1.pack()

rb1=Radiobutton(top,text="dean",variable=var,value=1)
rb1.pack()

rb2=Radiobutton(top,text="teacher",variable=var,value=2)
rb2.pack()

rb3=Radiobutton(top,text="student",variable=var,value=3)
rb3.pack()

b=Button(top,text="click Here",command=college)
b.pack()
top.mainloop()
