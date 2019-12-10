from Tkinter import *

Top=Tk()
Top.geometry("500x300")

class Movie():
    flag1=0
    flag2=0
    flag3=0
    def silver(self,k):
        if(k>=1 and k<=5):
            self.flag1=self.flag1+1
        if(k>=6 and k<=10):
            self.flag2=self.flag2+1
        if(k>=10 and k<=15):
            self.flag3=self.flag3+1
        
        if(k==1):
            B1.config(bg="black")
        if(k==2):
            B2.config(bg="black")
        if(k==3):
            B3.config(bg="black")
        if(k==4):
            B4.config(bg="black")
        if(k==5):
            B5.config(bg="black")
        if(k==6):
            B6.config(bg="black")
        if(k==7):
            B7.config(bg="black")
        if(k==8):
            B8.config(bg="black")
        if(k==9):
            B9.config(bg="black")
        if(k==10):
            B10.config(bg="black")
        if(k==11):
            B11.config(bg="black")
        if(k==12):
            B12.config(bg="black")
        if(k==13):
            B13.config(bg="black")
        if(k==14):
            B14.config(bg="black")
        if(k==15):
            B15.config(bg="black")
        
        n=(self.flag1*200)+(self.flag2*250)+(self.flag3*300)
        L.config(text="your bill is = "+str(n))
        

ob = Movie()

Lframe=LabelFrame(Top,text="SCREEN",font=("Times New Roman",20,"bold"))
Lframe.place(x=100,y=20,height=500,width=700)

B1=Button(Top,text="",bg="blue",activebackground="red",command=lambda:ob.silver(1))
B1.place(x=120,y=70,height=30,width=50)
B2=Button(Top,text="",bg="red",activebackground="green",command=lambda:ob.silver(2))
B2.place(x=180,y=70,height=30,width=50)
B3=Button(Top,text="",bg="green",activebackground="blue",command=lambda:ob.silver(3))
B3.place(x=240,y=70,height=30,width=50)
B4=Button(Top,text="",bg="blue",activebackground="red",command=lambda:ob.silver(4))
B4.place(x=300,y=70,height=30,width=50)
B5=Button(Top,text="",bg="red",activebackground="green",command=lambda:ob.silver(5))
B5.place(x=360,y=70,height=30,width=50)
B6=Button(Top,text="",bg="blue",activebackground="red",command=lambda:ob.silver(6))
B6.place(x=120,y=130,height=30,width=50)
B7=Button(Top,text="",bg="red",activebackground="green",command=lambda:ob.silver(7))
B7.place(x=180,y=130,height=30,width=50)
B8=Button(Top,text="",bg="green",activebackground="blue",command=lambda:ob.silver(8))
B8.place(x=240,y=130,height=30,width=50)
B9=Button(Top,text="",bg="blue",activebackground="red",command=lambda:ob.silver(9))
B9.place(x=300,y=130,height=30,width=50)
B10=Button(Top,text="",bg="red",activebackground="green",command=lambda:ob.silver(10))
B10.place(x=360,y=130,height=30,width=50)
B11=Button(Top,text="",bg="blue",activebackground="red",command=lambda:ob.silver(11))
B11.place(x=120,y=190,height=30,width=50)
B12=Button(Top,text="",bg="red",activebackground="green",command=lambda:ob.silver(12))
B12.place(x=180,y=190,height=30,width=50)
B13=Button(Top,text="",bg="green",activebackground="blue",command=lambda:ob.silver(13))
B13.place(x=240,y=190,height=30,width=50)
B14=Button(Top,text="",bg="blue",activebackground="red",command=lambda:ob.silver(14))
B14.place(x=300,y=190,height=30,width=50)
B15=Button(Top,text="",bg="red",activebackground="green",command=lambda:ob.silver(15))
B15.place(x=360,y=190,height=30,width=50)
L=Label(Top,text="",font=("times new roman",16,"bold"))
L.place(x=150,y=250,height=30,width=150)
Top.mainloop()
