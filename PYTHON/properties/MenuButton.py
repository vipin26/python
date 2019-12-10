from Tkinter import *

def showDialog():
   dialog = Toplevel(root)
   dialog.geometry("200x100")
   
root = Tk()
root.geometry("500x500")

mb = Menu(root)                                       
fmenu = Menu(mb, tearoff=0)   
fmenu.add_command(label="New",activebackground="yellow",activeforeground="red",font=("times new roman",20,"bold"),command=showDialog)   
fmenu.add_command(label="Open", command=showDialog)
fmenu.add_command(label="Save", command=showDialog)
fmenu.add_command(label="Save as...", command=showDialog)
fmenu.add_command(label="Close", command=showDialog)
fmenu.add_separator()
fmenu.add_command(label="Exit", command=root.destroy)
mb.add_cascade(label="File", menu=fmenu)


text = Text(root)                                       
text.pack(fill=BOTH,expand=1)                         
root.config(menu=mb)
root.mainloop()
