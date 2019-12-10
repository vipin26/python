import Tkinter

top = Tkinter.Tk()

#declaring canvas 
C = Tkinter.Canvas(top, bg="blue", height=250, width=300)


coord = 10, 10, 100, 100 # co-ordinates for arc (x_cord, y_cord, width, height)
arc = C.create_arc(coord, start=0, extent=150, fill="red")  # creating arc

line = C.create_line(10,120,100,120)

oval = C.create_oval(10,150,100,150)

C.pack()
top.mainloop()
