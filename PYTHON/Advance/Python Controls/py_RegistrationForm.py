from Tkinter import *
import tkMessageBox

top = Tk()
top.title("Form")
top.geometry("500x500")

l1 = Label(top,text="Name :",font=("arial",12))
l1.place(x="20",y="10",height="25",width="90")
e1 = Entry(top,font=("cambria",12))
e1.place(x="125",y="10",height="25",width="270")

l2 = Label(top,text="Father's Name : ",font=("arial",12))
l2.place(x="10",y="45",height="25",width="115")
e2 = Entry(top,font=("cambria",12))
e2.place(x="125",y="45",height="25",width="270")

l3 = Label(top,text="Mother's Name : ",font=("arial",12))
l3.place(x="10",y="80",height="25",width="115")
e3 = Entry(top,font=("cambria",12))
e3.place(x="125",y="80",height="25",width="270")

l4 = Label(top,text="Address : ",font=("arial",12))
l4.place(x="20",y="115",height="25",width="90")
text = Text(top,width="38",height="6")
text.insert(INSERT,"")
text.place(x="125",y="115")

l5 = Label(top,text="Gender : ",font=("arial",12))
l5.place(x="20",y="220",height="25",width="90")
r1=Radiobutton(top,text="Male",font=("arial",12),value="Male")
r1.place(x="130",y="220",height="25",width="90")
r2=Radiobutton(top,text="Female",font=("arial",12),value="Female")
r2.place(x="250",y="220",height="25",width="90")

l5 = Label(top,text="Language Known : ",font=("arial",12))
l5.place(x="0",y="270",height="25",width="150")
c1=Checkbutton(top,text="Python",font=("arial",12))
c1.place(x="150",y="255",height="25",width="90")
c2=Checkbutton(top,text="Java",font=("arial",12))
c2.place(x="250",y="255",height="25",width="90")
c3=Checkbutton(top,text="Ruby",font=("arial",12))
c3.place(x="350",y="255",height="25",width="90")
c4=Checkbutton(top,text="C++",font=("arial",12))
c4.place(x="140",y="290",height="25",width="90")
c5=Checkbutton(top,text="Kotlin",font=("arial",12))
c5.place(x="250",y="290",height="25",width="90")
c6=Checkbutton(top,text="Pearl",font=("arial",12))
c6.place(x="350",y="290",height="25",width="90")


l5 = Label(top,text="Phone No:",font=("arial",12))
l5.place(x="20",y="325",height="25",width="90")
e4 = Entry(top,font=("cambria",12))
e4.place(x="125",y="325",height="25",width="270")


l6 = Label(top,text="Email :",font=("arial",12))
l6.place(x="20",y="360",height="25",width="90")
e5 = Entry(top,font=("cambria",12))
e5.place(x="125",y="360",height="25",width="270")

b1=Button(top,text="Submit",font=("arial",16))
b1.place(x="140",y="420",height="30",width="100")
b2=Button(top,text="Reset",font=("arial",16))
b2.place(x="260",y="420",height="30",width="100")

top.mainloop()
