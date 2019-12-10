from Tkinter import *

top = Tk()
top.geometry("500x500")

#width="200", height="200"
f1 = Frame(top,bg="green")
f1.pack(side="left",fill=BOTH,expand=1)

f2 = Frame(top,bg="Red", width="200", height="200")
f2.pack(side="right",fill=BOTH,expand=1)

b1= Button(f1,text="Button 1");
b1.pack()
b2= Button(f2,text="Button 2");
b2.pack()

top.mainloop()
