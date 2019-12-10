from Tkinter import *
import Tkinter
import MySQLdb

top=Tk()
top.geometry("500x500")

def fun():
    j=E2.get()
    print "ROLL NO. = ",j
    k=E3.get()
    print"NAME = ",k
    l=E4.get()
    print"MOBILE NUMBER",l
    n=""
    if(var.get()==1):
        n="Male"
    if(var.get()==2):
        n="Female"

    print "GENDER = ",n

    o=""
    if(CheckVar1.get()==1):
        o=o+"HB1"
    if(CheckVar2.get()==1):
        o=o+"HB2"
    print "HOBBIES = ",o

    value=Lb1.get(Lb1.curselection())
    print "city =",value
    


    con= MySQLdb.connect("localhost","root","12345","form")
    print "Database Connected Successfully "
    cur = con.cursor()

    query = "INSERT INTO tb1(rollno,name,mob,gender,hobbies,city)VALUES(%s,%s,%s,%s,%s,%s)"
    args = (j,k,l,n,o,value)

    cur.execute(query,args)
    con.commit()
    print "Values inserted succesfully "

    

var=IntVar()
CheckVar1=IntVar()
CheckVar2=IntVar()

L1=Label(text="Registration Form")
L1.place(x=100,y=00,height=80,width=100)

L2=Label(text="ROLL NO")
L2.place(x=10,y=50,height=30,width=100)
E2=Entry(top,bd=5)
E2.place(x=120,y=50,height=30,width=100)

L3=Label(text="NAME")
L3.place(x=10,y=100,height=30,width=100)
E3=Entry(top,bd=5)
E3.place(x=120,y=100,height=30,width=100)

L4=Label(text=" MOBILE NO ")
L4.place(x=10,y=150,height=30,width=100)
E4=Entry(top,bd=5)
E4.place(x=120,y=150,height=30,width=100)

L5=Label(text="GENDER")
L5.place(x=10,y=200,height=30,width=100)

rb1=Radiobutton(top,text="Male",variable=var,value=1)
rb1.place(x=120,y=200,height=30,width=50)

rb2=Radiobutton(top,text="Female",variable=var,value=2)
rb2.place(x=200,y=200,height=30,width=50)

L6=Label(text="HOBBIES")
L6.place(x=10,y=250,height=30,width=100)
C1=Checkbutton(top,text="HB1",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C1.place(x=120,y=250,height=30,width=100)
C2=Checkbutton(top,text="HB2",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C2.place(x=200,y=250,height=30,width=100)

L7=Label(text="CITY")
L7.place(x=10,y=300,height=30,width=100)
Lb1=Listbox(top,height=5)
Lb1.insert(0,"DEHRADUN")
Lb1.insert(1,"HARIDWAR")
Lb1.insert(2,"RISHIKESH")
Lb1.insert(3,"GOPESHWAR")
Lb1.place(x=120,y=300,width=100)

B=Button(top,text="Insert",command=fun)
B.place(x=120,y=400,height=50,width=80)

top.mainloop()
