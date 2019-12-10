from Tkinter import *

top = Tk()
top.geometry("500x500")

Lframe = LabelFrame(top, text="This is a LabelFrame")
Lframe.pack(fill="both", expand=1)
 
left = Label(Lframe, text="Inside the LabelFrame")
left.pack()
 
top.mainloop()
