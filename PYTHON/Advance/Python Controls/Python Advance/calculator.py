from Tkinter import *

Top=Tk()
Top.geometry("300x400")

def cal(k):
    s=""
    s=T.get("1.0",END)
    s=s.strip()
    s=s+str(k)
    T.delete("1.0",END)
    T.insert("1.0",str(s))
    
    
class Add:
    def sum(self):
        self.a=float(T.get("1.0",END))
        T.delete("1.0",END)
        self.flag=1
    def subtraction(self):
        self.a=float(T.get("1.0",END))
        T.delete("1.0",END)
        self.flag=2
    def multiply(self):
        self.a=float(T.get("1.0",END))
        T.delete("1.0",END)
        self.flag=3
    def divide(self):
        self.a=float(T.get("1.0",END))
        T.delete("1.0",END)
        self.flag=4
    def percent(self):
        self.a=float(T.get("1.0",END))
        T.delete("1.0",END)
        self.flag=5     
         
    def eqlTo(self):
        self.b=float(T.get("1.0",END))
        if(self.flag==1):
            self.c=float(self.a+self.b)
        if(self.flag==2):
            self.c=float(self.a-self.b)
        if(self.flag==3):
            self.c=float(self.a*self.b)
        if(self.flag==4):
            self.c=float(self.a/self.b)
        if(self.flag==5):
            self.c=float((self.a*100)/self.b)
        T.delete("1.0",END)
        T.insert("1.0",str(self.c))
ob=Add()

def clear():
    T.delete("1.0",END)

def cut():
    s1=""
    s2=""
    s1=T.get("1.0",END)
    for i in range(0,len(s1)-2,1):
        s2=s2+s1[i]
    T.delete("1.0",END)
    T.insert("1.0",str(s2))    

L=Label(Top,text="CALCULATOR")
L.place(x=100,y=00,height=50,width=80)
T=Text(Top)
T.place(x=50,y=70,height=50,width=200)
B1=Button(text="1",command=lambda:cal(1))
B1.place(x=20,y=150,height=30,width=50)
B2=Button(text="2",command=lambda:cal(2))
B2.place(x=80,y=150,height=30,width=50)
B3=Button(text="3",command=lambda:cal(3))
B3.place(x=140,y=150,height=30,width=50)
M=Button(text="*",command=ob.multiply)
M.place(x=200,y=150,height=30,width=50)
B4=Button(text="4",command=lambda:cal(4))
B4.place(x=20,y=200,height=30,width=50)
B5=Button(text="5",command=lambda:cal(5))
B5.place(x=80,y=200,height=30,width=50)
B6=Button(text="6",command=lambda:cal(6))
B6.place(x=140,y=200,height=30,width=50)
D=Button(text="/",command=ob.divide)
D.place(x=200,y=200,height=30,width=50)
B7=Button(text="7",command=lambda:cal(7))
B7.place(x=20,y=250,height=30,width=50)
B8=Button(text="8",command=lambda:cal(8))
B8.place(x=80,y=250,height=30,width=50)
B9=Button(text="9",command=lambda:cal(9))
B9.place(x=140,y=250,height=30,width=50)
E=Button(text="=",command=ob.eqlTo)
E.place(x=200,y=250,height=80,width=50)
d=Button(text="+",command=ob.sum)
d.place(x=20,y=300,height=30,width=50)
B0=Button(text="0",command=lambda:cal(0))
B0.place(x=80,y=300,height=30,width=50)
S=Button(text="-",command=ob.subtraction)
S.place(x=140,y=300,height=30,width=50)
C=Button(text="AC",command=clear)
C.place(x=20,y=350,height=30,width=50)
X=Button(text="C",command=cut)
X.place(x=80,y=350,height=30,width=50)
P=Button(text="%",command=ob.percent)
P.place(x=140,y=350,height=30,width=50)
D=Button(text=".",command=lambda:cal("."))
D.place(x=200,y=350,height=30,width=50)
Top.mainloop()
