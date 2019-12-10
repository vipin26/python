from Tkinter import *
import MySQLdb
Top=Tk()
Top.geometry("600x600")
def insert():
    j=E1.get()
    k=E2.get()
    l=E3.get()
    m=E4.get()
    n=E5.get()
    o=E6.get()
    p=E7.get()
    q=E8.get()
    r=""
    if(var.get()==1):
        r="Male"
    if(var.get()==2):
        r="Female"
    con= MySQLdb.connect("localhost","root","12345","facebook")
    print "Database Connected Successfully "
    cur = con.cursor()

    k=o+p+q
    print k
    
    query = "INSERT INTO tb1(MobileNo,FirstName,LastName,YourEmail,Password,Birthday,Gender)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    args = (j,k,l,m,n,o,p,q,r)

    cur.execute(query,args)
    con.commit()
    print "Values inserted succesfully "
    con.close()


var=IntVar()

m1 = PanedWindow(Top, bg="blue")
m1.pack(fill=BOTH, expand=1)
L=Label(Top,text="FACEBOOK")
L.place(x=250,y=00,height=50,width=100)
L1=Label(Top,text="Mobile NO")
L1.place(x=70,y=50,height=30,width=100)
E1=Entry(Top,bd=5)
E1.place(x=180,y=50,height=30,width=200)
L2=Label(Top,text="First Name")
L2.place(x=70,y=100,height=30,width=100)
E2=Entry(Top,bd=5)
E2.place(x=180,y=100,height=30,width=200)

L3=Label(Top,text="Last Name")
L3.place(x=70,y=150,height=30,width=100)
E3=Entry(Top,bd=5)
E3.place(x=180,y=150,height=30,width=200)

L4=Label(Top,text="Your Email")
L4.place(x=70,y=200,height=30,width=100)
E4=Entry(Top,bd=5)

E4.place(x=180,y=200,height=30,width=200)

L5=Label(Top,text="Password")
L5.place(x=70,y=250,height=30,width=100)
E5=Entry(Top,bd=5)
E5.place(x=180,y=250,height=30,width=200)

L6=Label(Top,text="Birthday")
L6.place(x=70,y=300,height=30,width=100)
E6=Entry(Top,bd=5)
E6.insert(0,"DD")
E6.place(x=180,y=300,height=30,width=30)
E7=Entry(Top,bd=5)
E7.insert(0,"MM")
E7.place(x=220,y=300,height=30,width=50)
E8=Entry(Top,bd=5)
E8.insert(0,"YYYY")
E8.place(x=280,y=300,height=30,width=50)

#Radio Button
L7=Label(Top,text="Gender")
L7.place(x=70,y=350,height=30,width=100)
rb1=Radiobutton(Top,text="Male",variable=var,value=1)
rb1.place(x=180,y=350,height=30,width=50)
rb2=Radiobutton(Top,text="Female",variable=var,value=2)
rb2.place(x=250,y=350,height=30,width=60)

B1=Button(Top,text="Insert",command=insert)
B1.place(x=200,y=400,height=30,width=50)
B2=Button(Top,text="Search")
B2.place(x=270,y=400,height=30,width=50)
B3=Button(Top,text="Update")
B3.place(x=200,y=450,height=30,width=50)
B4=Button(Top,text="Delete")
B4.place(x=270,y=450,height=30,width=50)

Top.mainloop()
