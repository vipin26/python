from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *      

root = Tk()
root.geometry("1360x768")

def newMenu():
    p=""
    p=askyesnocancel('verify','Do you want to save changes to untitled ?')
    
    if(p==False):
        text.delete("1.0",END)
    elif(p==True):
        name=asksaveasfile(mode='w',defaultextension='.txt')
        name.write(text.get("1.0",END))
        name.close()

def openMenu():
    name=askopenfilename()
    f=open(name,'r')
    s=f.read()
    text.insert(END,s)
    f.close()

def saveMenu():
    name=asksaveasfile(mode='w',defaultextension='.txt')
    name.write(text.get("1.0",END))
    name.close()

class A:
    def showDialog(self):
        self.dialog=Toplevel(root)
        self.dialog.geometry("300x250")
        self.L1=Label(dialog,text="Find What")
        self.L1.place(x=10,y=50,height=30,width=80)
        self.E1=Entry(dialog,bd=5)
        self.E1.place(x=100,y=50,height=30,width=80)
        self.B1=Button(dialog,text="Find Next")
        self.B1.place(x=200,y=50,height=30,width=80)
        self.L2=Label(dialog,text="Replace with")
        self.L2.place(x=10,y=100,height=30,width=80)
        self.E2=Entry(dialog,bd=5)
        self.E2.place(x=100,y=100,height=30,width=80)
        self.B2=Button(dialog,text="Replace",command=replace)
        self.B2.place(x=200,y=100,height=30,width=80)
        self.B3=Button(dialog,text="Replace All")
        self.B3.place(x=200,y=150,height=30,width=80)
        self.B4=Button(dialog,text="Cancel")
        self.B4.place(x=200,y=200,height=30,width=80)

    def editMenu(self,k):
        if(k==1):
            self.a=text.get("1.0",END)
            text.delete("1.0",END)
        if(k==2):
            self.a=text.get("1.0",END)
        if(k==3):
            text.insert(END,self.a)
        if(k==4):
            text.delete("1.0",END)
    
ob=A()

def replace():
    s1=text.get("1.0",END)
    x=ob.dialog.E1.get("1.0",END)
    y=ob.dialog.E2.get("1.0",END)
    s1.replace(x,y)

    
    
    
    

me=Menu(root)
fmenu=Menu(me,tearoff=0)
fmenu.add_command(label="New",command=newMenu)
fmenu.add_command(label="Open",command=openMenu)
fmenu.add_command(label="Save",command=saveMenu)
fmenu.add_command(label="Save As...",command=saveMenu)
fmenu.add_separator()
fmenu.add_command(label="Exit",command=root.destroy)
me.add_cascade(label="File",menu=fmenu)

fmenu1=Menu(me,tearoff=0)
fmenu1.add_command(label="Find",command=replace)
fmenu1.add_separator()
fmenu1.add_command(label="Cut",command=lambda:ob.editMenu(1))
fmenu1.add_command(label="Copy",command=lambda:ob.editMenu(2))
fmenu1.add_command(label="Paste",command=lambda:ob.editMenu(3))
fmenu1.add_separator()
fmenu1.add_command(label="Delete",command=lambda:ob.editMenu(4))
me.add_cascade(label="Edit",menu=fmenu1)

fmenu2=Menu(me,tearoff=0)
fmenu2.add_command(label="Word Wrap")
fmenu2.add_command(label="Font...")
me.add_cascade(label="Format",menu=fmenu2)

fmenu3=Menu(me,tearoff=0)
fmenu3.add_command(label="Zoom")
fmenu3.add_command(label="Status Bar")
me.add_cascade(label="View",menu=fmenu3)

fmenu4=Menu(me,tearoff=0)
fmenu4.add_command(label="View Help")
fmenu4.add_separator()
fmenu4.add_command(label="About Notepad")
me.add_cascade(label="Help",menu=fmenu4)
text=Text(root)
text.pack(fill=BOTH,expand=1)

root.config(menu=me)
root.mainloop()
