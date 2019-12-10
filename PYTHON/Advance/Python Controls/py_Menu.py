from Tkinter import *

def showDialog():
   dialog = Toplevel(root)
   dialog.geometry("200x100")
   b1 = Button(dialog, text="Hello ! I m Top Level Control Behaves like a Dialog")
   b1.pack()
   
root = Tk()
root.geometry("1360x768")

mb = Menu(root)                                        #creating menu strip/menu bar 
fmenu = Menu(mb, tearoff=0)                         #creating file menu adding from index 0
fmenu.add_command(label="New", command=showDialog)  #adding submenu to the window 
fmenu.add_command(label="Open", command=showDialog)
fmenu.add_command(label="Save", command=showDialog)
fmenu.add_command(label="Save as...", command=showDialog)
fmenu.add_command(label="Close", command=showDialog)
fmenu.add_separator()
fmenu.add_command(label="Exit", command=root.destroy)
mb.add_cascade(label="File", menu=fmenu)


text = Text(root)                                           #adding textarea to the frame
text.pack(fill=BOTH,expand=1)                         #expending it to full screen

root.config(menu=mb)
root.mainloop()
