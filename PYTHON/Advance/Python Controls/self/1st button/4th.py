from Tkinter import*

def shop():
    a=int(T2.get("1.0",END))
    T3.insert(END,str(a*10))
    b=int(T4.get("1.0",END))
    T5.insert(END,str(b*15))
    T6.insert(END,str((a*10)+(b*15)))
    c=int(T6.get("1.0",END))
    T7.insert(END,str((((a*10)+(b*15))*10)/100))
    d=int(T7.get("1.0",END))
    T8.insert(END,str(c-d))

L1=Label(text="KUMAI SWEET SHOP")
L1.pack()

L2=Label(text="SAMOSA=10 RUPEES")
L2.pack()
T2=Text(height=2,width=30)
T2.pack()
T3=Text(height=2,width=30)
T3.pack()

L3=Label(text="TEA=15 RUPEES")
L3.pack()
T4=Text(height=2,width=30)
T4.pack()
T5=Text(height=2,width=30)
T5.pack()

L4=Label(text="TOTAL")
L4.pack()
T6=Text(height=2,width=30)
T6.pack()
L5=Label(text="DISCOUNT")
L5.pack()
T7=Text(height=2,width=30)
T7.pack()
L6=Label(text="AMT")
L6.pack()
T8=Text(height=2,width=30)
T8.pack()
b=Button(text="click here",command=shop)
b.pack()
mainloop()
