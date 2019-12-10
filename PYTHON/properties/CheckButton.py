from Tkinter import *
import Tkinter

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(top, text = "Programming ", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20,activebackground="red",activeforeground="yellow",bg="gold",font=('Tahoma',20,'italic'))
C2 = Checkbutton(top, text = "Sports ", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20,activebackground="blue",activeforeground="brown",bg="lime",font=('script',20,'bold italic'))
C1.pack()
C2.pack()

top.mainloop()
