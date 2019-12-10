from Tkinter import *
import tkMessageBox


Login_ID=["GAURAV","BHUMI","VIPIN","CHETNA"]
Password=["BIJAY","ANJALI","SURAJ","KAJAL"]
def insert():
    a=E2.get()
    index=0
    for i in range(0,len(Login_ID),1):
        if(a==Login_ID[i]):
            index=i; 
    b=E3.get()
    if(Password[index]==b):
        tkMessageBox.showinfo("Admin","Login Successful")
    else:
        tkMessageBox.showinfo("Admin","Password Match Failed or Wrong Password")
def delete():
    E2.delete(0,END)
    E3.delete(0,END)
    
def ginsert():
    a=E5.get()
    index=0
    for i in range(0,len(Login_ID),1):
        if(a==Login_ID[i]):
            index=i; 
    b=E6.get()
    if(Password[index]==b):
        tkMessageBox.showinfo("Admin","Login Successful")
    else:
        tkMessageBox.showinfo("User","User Login")
def gdelete():
    E5.delete(0,END)
    E6.delete(0,END)

top=Tk()
top.geometry("500x250")

#FRAME
F1=Frame(top,bg="blue")
F1.place(x=0,y=0,height=300,width=250)

F1=Frame(top,bg="yellow")
F1.place(x=250,y=0,height=300,width=250)

L1=Label(top,text="ADMIN BLOCK")
L1.place(x=50,height=50,width=80)

L2=Label(top,text="Login ID :")
L2.place(x=10,y=50,height=30,width=80)
E2=Entry(top,bd=5)
E2.place(x=100,y=50,height=30,width=80)

L3=Label(top,text="Password :")
L3.place(x=10,y=100,height=30,width=80)
E3=Entry(top,bd=5)
E3.place(x=100,y=100,height=30,width=80)

L4=Label(top,text="USER BLOCK ")
L4.place(x=350,y=00,height=50,width=80)

L5=Label(top,text="Login ID :")
L5.place(x=300,y=50,height=30,width=80)
E5=Entry(top,bd=5)
E5.place(x=380,y=50,height=30,width=80)

L6=Label(top,text="Password :")
L6.place(x=300,y=100,height=30,width=80)
E6=Entry(top,bd=5)
E6.place(x=380,y=100,height=30,width=80)

B1=Button(top,text="Login",command=insert)
B1.place(x=50,y=150,height=30,width=50)
B2=Button(top,text="Reset",command=delete)
B2.place(x=120,y=150,height=30,width=50)

B3=Button(top,text="Login",command=ginsert)
B3.place(x=330,y=150,height=30,width=50)
B4=Button(top,text="Reset",command=gdelete)
B4.place(x=400,y=150,height=30,width=50)

top.mainloop()
