from Tkinter import *

root = Tk()
root.geometry("968x1024")

frame1 = Frame(root,bg="yellow",height="200",width="400")
frame2 = Frame(root,bg="green",height="200",width="400")

frame1.pack(side="left",expand="true")
frame2.pack(side="right",expand="true")
'''
bt2 = Button(frame1, text="Red", fg="red")
bt2.place("10","10")

bt3 = Button(frame1, text="Brown", fg="brown")
bt3.pack()

bt4 = Button(frame2, text="Blue", fg="blue")
bt4.pack()

bt5 = Button(frame2, text="Green", fg="green")
bt5.pack()
'''

root.mainloop()

