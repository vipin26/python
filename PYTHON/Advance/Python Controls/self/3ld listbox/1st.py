from Tkinter import*
import tkMessageBox

top =Tk()

def children():
    people=Lb1.get(Lb1.curselection())
    print people
    Lb2.insert(0,people)


Lb1=Listbox(top,height=4)
Lb1.insert(0,"Ram")
Lb1.insert(1,"Mohan")
Lb1.insert(2,"Rohan")
Lb1.insert(3,"Sohan")
Lb1.pack()
Lb2=Listbox(top,height=4)
Lb2.pack()
b=Button(top,text="click here",height=2,command=children);
b.pack()
top.mainloop()
