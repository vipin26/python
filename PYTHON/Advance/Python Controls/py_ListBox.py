from Tkinter import *
import tkMessageBox

top = Tk()

def sel_value():
   value=Lb1.get(Lb1.curselection())
   print value


Lb1 = Listbox(top, height=3)
Lb1.insert(0, "Java")
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()

b1=Button(top,text="Click me ", width="20",height="5",command=sel_value);
b1.pack()

top.mainloop()
