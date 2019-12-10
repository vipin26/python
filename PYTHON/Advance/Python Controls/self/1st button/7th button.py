from Tkinter import*

def switch():
    print"clicked" 
    a=T1.get("1.0",END)
    T1.delete("1.0",END)
    b=T2.get("1.0",END)
    T2.delete("1.0",END)
    T2.insert(END,str(a))
    T1.insert(END,str(b))


T1=Text(height=4,width=20)
T1.pack()

b=Button(text="CLICK HERE", command=switch)
b.pack()

T2=Text(height=4,width=20)
T2.pack()

mainloop()
