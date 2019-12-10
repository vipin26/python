from Tkinter import*

def shyamlaal():
    print "clicked"
    a=int(T1.get("1.0",END))
    b=int(T2.get("1.0",END))
    print "sum is ",(a+b)
    
L1=Label(text="Enter First Number ")
L1.pack()
T1=Text(height=2,width=30)
T1.pack()
L2=Label(text="Enter Second Number ")
L2.pack()
T2=Text(height=2,width=30)
T2.pack()

b=Button(text="click me", command=shyamlaal)
b.pack()

mainloop()
