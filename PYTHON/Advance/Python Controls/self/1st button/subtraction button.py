from Tkinter import*

def subtraction():
    print"clicked"
    a=int(T1.get("1.0",END))
    b=int(T2.get("1.0",END))
    T3.insert(END,str(a-b))

L1=Label(text="ENTER FIRST NUMBER")
L1.pack()
T1=Text(height=2,width=20)
T1.pack()
L2=Label(text="ENTER SEOND NUMBER")
L2.pack()
T2=Text(height=2,width=20)
T2.pack()
b=Button(text="CLICK HERE",command=subtraction)
b.pack()
L3=Label(text="SUBTRACTION IS ")
L3.pack()
T3=Text(height=2,width=20)
T3.pack()
mainloop()
