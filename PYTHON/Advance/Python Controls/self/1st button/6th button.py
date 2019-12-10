from Tkinter import*

def reg():
     print "clicked"
     a=T2.get("1.0",END)
     b=T3.get("1.0",END)
     c=T4.get("1.0",END)
     d=T5.get("1.0",END)
     T6.insert(END,str(a+b+c+d))
     T2.delete("1.0",END)
     T3.delete("1.0",END)
     T4.delete("1.0",END)
     T5.delete("1.0",END)
     
L1=Label(text="REGISTRATION")
L1.pack()

L2=Label(text="NAME")
L2.pack()
T2=Text(height=2,width=30)
T2.pack()

L3=Label(text="FATHER'S NAME")
L3.pack()
T3=Text(height=2,width=30)
T3.pack()

L4=Label(text="MOTHER'S NAME")
L4.pack()
T4=Text(height=2,width=30)
T4.pack()

L5=Label(text="CLASS")
L5.pack()
T5=Text(height=2,width=30)
T5.pack()


b=Button(text="CLICK HERE", command =reg)
b.pack()
T6=Text(height=10,width=30)
T6.pack()

mainloop()


