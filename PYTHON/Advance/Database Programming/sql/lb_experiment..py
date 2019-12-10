from Tkinter import *

top=Tk()
top.geometry("500x500")

def insert():
    Lb1.activate(3)
    value=Lb1.get(Lb1.curselection())
    print value
    
Lb1=Listbox(top,height=5)
Lb1.insert(0,"DEHRADUN")
Lb1.insert(1,"HARIDWAR")
Lb1.insert(2,"RISHIKESH")
Lb1.insert(3,"GOPESHWAR")
Lb1.place(x=120,y=100,width=100)


B=Button(top,text="Insert",command=insert)
B.place(x=50,y=300,height=30,width=80)

top.mainloop()
