from Tkinter import*

Top=Tk()
Top.geometry("220x220")

def Addition(event):
    a=int(T1.get("1.0",END))
    b=int(T2.get("1.0",END))
    c=a+b
    T3.insert("1.0",str(c))
T1=Text(Top)
T1.place(x=10,y=20,height=50,width=200)
T2=Text(Top)
T2.place(x=10,y=80,height=50,width=200)
T3=Text(Top)
T3.place(x=10,y=150,height=50,width=200)
T3.bind('<Return>',Addition)
Top.mainloop()

