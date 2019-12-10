from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *      
from tkColorChooser import *
top = Tk()

def msg():
    p=""
    #p = askquestion('Verify', 'Really quit?')
    #p = askokcancel('Title ', ' Really quit?')
    #p = askyesno('Title ', ' Really quit?')
    #p = askretrycancel('Title ', ' Really quit?')
    #p = askyesnocancel('Title ', ' Really quit?')
    #showerror('Dailog Box Title ', 'Result is '+str(p))
    #showinfo('Dailog Box Title ', 'Result is '+str(p))
    showwarning('Dailog Box Title ', 'Result is '+str(p))
   
def dialogs():
    #name=askcolor(color="#6A9662",title = "Bernd's Colour Chooser")
    #name=askopenfilename()
    name=asksaveasfile(mode='w',defaultextension=".txt")
    print name
    showinfo('Dailog Box Title ', 'Result is '+str(name))


b1=Button(top, text="Dialog-1",command=msg)
b1.pack()
b2=Button(top, text="File Dialog ",command=dialogs)
b2.pack()

top.mainloop()
