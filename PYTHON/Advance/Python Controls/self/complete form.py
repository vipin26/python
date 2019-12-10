from Tkinter import*
import Tkinter
import tkMessageBox

def form():
    print "NAME = "+T1.get("1.0",END)
    print "FATHER'S NAME = "+T2.get("1.0",END)
    print "ADDRESS = "+T3.get("1.0",END)

    b=""
    if(var.get()==1):
        b="Male"
    if(var.get()==2):
        b="Female"

    print "GENDER = ",b

    a=""
    if(CheckVar1.get()==1):
        a=a+"Python, "
    if(CheckVar2.get()==1):
        a=a+"Java, "
    if(CheckVar3.get()==1):
        a=a+"Ruby, "
    if(CheckVar4.get()==1):
        a=a+"C++, "
    if(CheckVar5.get()==1):
        a=a+"Kotlin, "
    if(CheckVar6.get()==1):
        a=a+"Pearl, "
    tkMessageBox.showinfo("Title ",a)
    print "LANGUAGE KNOWN = ",a
    print "PHONE NO. = "+T6.get("1.0",END).strip()
    print "Email = "+T7.get("1.0",END)
Top=Tkinter.Tk()
var=IntVar()
Top.geometry("600x600")
CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
CheckVar5=IntVar()
CheckVar6=IntVar()
def form1():
    T1.delete("1.0",END)
    T2.delete("1.0",END)
    T3.delete("1.0",END)
    T6.delete("1.0",END)
    T7.delete("1.0",END)
    CheckVar1.set(0)
    CheckVar2.set(0)
    CheckVar3.set(0)
    CheckVar4.set(0)
    CheckVar5.set(0)
    CheckVar6.set(0)
    #rb1.deselect()
    #rb2.deselect()
    var.set(0)
    
L=Label(Top,text="REGISTRATION")
L.place(x=200,y=0,height=80,width=100)

L1=Label(Top,text="NAME :")
L1.place(x=10,y=50,height=30,width=100)
T1=Text(height=2,width=30)
T1.place(x=110,y=50,width=100,height=30)

L2=Label(Top,text="NAME OF FATHER :")
L2.place(x=10,y=100,height=30,width=100)
T2=Text(height=2,width=30)
T2.place(x=110,y=100,height=30,width=150)

L3=Label(Top,text="ADDRESS :")
L3.place(x=10,y=150,height=30,width=100)
T3=Text(height=2,width=30)
T3.place(x=110,y=150,height=100,width=200)

L4=Label(Top,text="GENDER :")
L4.place(x=10,y=250,height=30,width=100)

rb1=Radiobutton(Top,text="MALE",variable=var,value=1)
rb1.place(x=110,y=250,height=30,width=100)

rb2=Radiobutton(Top,text="FEMALE",variable=var,value=2)
rb2.place(x=200,y=250,height=30,width=100)

L5=Label(Top,text="LANGUAGE KNOWN :")
L5.place(x=10,y=300,height=50,width=200)
C1=Checkbutton(Top,text="Python",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C1.place(x=110,y=300,height=30,width=100)
C2=Checkbutton(Top,text="Java",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C2.place(x=200,y=300,height=30,width=100)
C3=Checkbutton(Top,text="Ruby",variable=CheckVar3,onvalue=1,offvalue=0,height=5,width=20)
C3.place(x=300,y=300,height=30,width=100)
C4=Checkbutton(Top,text="C++",variable=CheckVar4,onvalue=1,offvalue=0,height=5,width=20)
C4.place(x=110,y=350,height=30,width=100)
C5=Checkbutton(Top,text="Kotlin",variable=CheckVar5,onvalue=1,offvalue=0,height=5,width=20)
C5.place(x=200,y=350,height=30,width=100)
C6=Checkbutton(Top,text="Pearl",variable=CheckVar6,onvalue=1,offvalue=0,height=5,width=20)
C6.place(x=300,y=350,height=30,width=100)

L6=Label(Top,text="PHONE NO. :")
L6.place(x=10,y=400,height=30,width=100)
T6=Text(height=2,width=30)
T6.place(x=110,y=400,height=30,width=100)

L7=Label(Top,text="EMAIL :")
L7.place(x=10,y=450,height=30,width=100)
T7=Text(height=2,width=30)
T7.place(x=110,y=450,height=30,width=100)

B1=Button(text="SUBMIT",command=form)
B1.place(x=100,y=500,height=30,width=80)
B2=Button(text="RESET",command=form1)
B2.place(x=200,y=500,height=30,width=80)


mainloop()
