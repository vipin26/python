
from Tkinter import *

def show():
   if(var.get()==1):
      a="Male"
      
   elif(var.get()==2):
      a="FeMale"
   else:
      a="Third Gender "
   print a
   L1.config(text = a)

top = Tk()
var = IntVar()
L1 = Label(top,text="GENDER")
L1.pack()
rb1 = Radiobutton(top, text="Male", variable=var, value=1, command=show)
rb1.pack()
rb2 = Radiobutton(top, text="Female ", variable=var, value=2, command=show)
rb2.pack()
rb3 = Radiobutton(top, text="Third Gender", variable=var, value=3,  command=show)
rb3.pack()


top.mainloop()
