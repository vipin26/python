from Tkinter import *

top = Tk()

m1 = PanedWindow(top, bg="green")
m1.pack(fill=BOTH, expand=1)
left = Label(m1, text="Top Panel ")
left.pack()

m2 = PanedWindow(top, bg="blue")
m2.pack(fill=BOTH, expand=1)
middle = Label(m2, text="Mid Panel ")
middle.pack()

m3 = PanedWindow(top, bg="red")
m3.pack(fill=BOTH, expand=1)
bottom = Label(m3, text="Bottom Panel ")
bottom.pack()

top.mainloop()
