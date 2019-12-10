from Tkinter import *

top = Tk()
top.geometry("500x500")


f1 = Frame(top,bg="green", width="200", height="200")
f1.place(x=0,y=0)

f2 = Frame(top,bg="Red", width="200", height="200")
f2.place(x=300,y=0)

b1= Button(f1,text="Button 1");
b1.place(x=0,y=0)
#b1.pack()
b2= Button(f2,text="Button 1");
b2.place(x=10,y=0)

top.mainloop()
