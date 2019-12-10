from Tkinter import *
def fun():
    print "clicked"
    a=int(T1.get("1.0",END))
    b=int(T2.get("1.0",END))
    print"multification is "+str(a*b)

L1=Label(text="enter a number")
L1.pack()
T1=Text(height=4,width=20)
T1.pack()
L2=Label(text="enter number")
L2.pack()
T2=Text(height=2,width=20)
T2.pack()

b=Button(text="click here",command=fun)
b.pack()
mainloop()
