from Tkinter import *
Top=Tk()
Top.geometry("250x250")

B=Button(Top,text="Button1",bg="red",fg="blue",activebackground="green",activeforeground="yellow",font=('TIMES NEW ROMAN',20,'bold'),cursor="plus")
B.place(x=50,y=20,height=30,width=150)
Top.mainloop()
