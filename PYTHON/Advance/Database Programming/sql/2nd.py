from Tkinter import *
import Tkinter
import MySQLdb
import tkMessageBox

top=Tk()
top.geometry("500x500")

def insert():
    j=E2.get()
    k=E3.get()
    l=E4.get()
    n=""
    if(var.get()==1):
        n="Male"
    if(var.get()==2):
        n="Female"
    o=""
    if(CheckVar1.get()==1):
        o=o+"HB1"
    if(CheckVar2.get()==1):
        o=o+"HB2"
    value=Lb1.get(Lb1.curselection())
    con= MySQLdb.connect("localhost","root","12345","form")
    print "Database Connected Successfully "
    cur = con.cursor()

    query = "INSERT INTO tb1(rollno,name,mob,gender,hobbies,city)VALUES(%s,%s,%s,%s,%s,%s)"
    args = (j,k,l,n,o,value)

    cur.execute(query,args)
    con.commit()
    print "Values inserted succesfully "
    con.close()

def search():
    l1 = []
    j=E2.get()
    con=MySQLdb.connect("localhost","root","12345","form")
    print "Database connected sussfully "
    cur=con.cursor()
    cur.execute("SELECT * FROM tb1 where rollno=%s",j)
    print("fetchall :")
    res=cur.fetchone()
    if(res==None):
        tkMessageBox.showinfo("Title","Record Not Found ")
    else :
        l1 = res
        E3.delete(0,END)
        E4.delete(0,END)
        E3.insert(0,l1[1])
        E4.insert(0,l1[2])
        if(l1[3]=='Male'):
            var.set(1)
        if(l1[3]=='Female'):
            var.set(2)
        con.close()

        if(l1[4].startswith("HB1")):
            CheckVar1.set(1)
        if(l1[4].endswith("HB2")):
            CheckVar2.set(1)

def update():
    j=E2.get()
    k=E3.get()
    l=E4.get()
    n=""
    if(var.get()==1):
        n="Male"
    if(var.get()==2):
        n="Female"
    o=""
    if(CheckVar1.get()==1):
        o=o+"HB1"
    if(CheckVar2.get()==1):
        o=o+"HB2"
    value=Lb1.get(Lb1.curselection())
    print value
    con= MySQLdb.connect("localhost","root","12345","form")
    print "Database Connected Successfully "
    cur = con.cursor()

    query = "UPDATE tb1 SET name=%s,mob=%s,gender=%s,hobbies=%s,city=%s where rollno=%s"
    args = (k,l,n,o,value,j)

    cur.execute(query,args)
    con.commit()
    print "Values Updated succesfully "
    con.close()
    
def delete():
    j=E2.get()
    con=MySQLdb.connect("localhost","root","12345","form")
    print "Database connected sussfully "
    cur=con.cursor()
    cur.execute("delete FROM tb1 where rollno=%s",j)
    con.commit()
    con.close()
    print "Deleted Successfully "

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
#RADIO BUTTON
L5=Label(text="GENDER")
L5.place(x=10,y=200,height=30,width=100)

rb1=Radiobutton(top,text="Male",variable=var,value=1)
rb1.place(x=120,y=200,height=30,width=50)

rb2=Radiobutton(top,text="Female",variable=var,value=2)
rb2.place(x=200,y=200,height=30,width=50)
#CHECK BUTTON
L6=Label(text="HOBBIES")
L6.place(x=10,y=250,height=30,width=100)
C1=Checkbutton(top,text="HB1",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C1.place(x=120,y=250,height=30,width=100)
C2=Checkbutton(top,text="HB2",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C2.place(x=200,y=250,height=30,width=100)
#LIST BOX
L7=Label(text="CITY")
L7.place(x=10,y=300,height=30,width=100)
Lb1=Listbox(top,height=5)
Lb1.insert(0,"DEHRADUN")
Lb1.insert(1,"HARIDWAR")
Lb1.insert(2,"RISHIKESH")
Lb1.insert(3,"GOPESHWAR")
Lb1.place(x=120,y=300,width=100)

B=Button(top,text="Insert",command=insert)
B.place(x=50,y=400,height=30,width=80)

B1=Button(top,text="Search",command=search)
B1.place(x=150,y=400,height=30,width=50)

B2=Button(top,text="Update",command=update)
B2.place(x=100,y=450,height=30,width=50)

B2=Button(top,text="Delete",command=delete)
B2.place(x=180,y=450,height=30,width=50)

top.mainloop()
