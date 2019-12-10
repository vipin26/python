from Tkinter import *
import tkMessageBox

top = Tk()
top.geometry("200x200")

Lb1 = Listbox(top, height=5,bg="sky blue",fg="red",bd=5,font=("Times New Roman",20,"bold"))
Lb1.insert(0, "Java")
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
top.mainloop()
