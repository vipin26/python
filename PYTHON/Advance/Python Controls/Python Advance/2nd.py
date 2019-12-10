from Tkinter import *

Top=Tk()
Top.geometry("250x220")

class g_Game:
    flag=0
    counter=0
    msg=""
    l1=[1,1,1,1,1,1,1,1,1]
    def game(self,k):
        self.counter+=1
        if(self.counter%2==0):
            m
            sg="X"
        else:
            msg="0"
        
        if(k==1):
            B1.config(text=msg)
            self.l1[0]=msg
        if(k==2):
            B2.config(text=msg)
            self.l1[1]=msg
        if(k==3):
            B3.config(text=msg)
            self.l1[2]=msg
        if(k==4):
            B4.config(text=msg)
            self.l1[3]=msg
        if(k==5):
            B5.config(text=msg)
            self.l1[4]=msg
        if(k==6):
            B6.config(text=msg)
            self.l1[5]=msg
        if(k==7):
            B7.config(text=msg)
            self.l1[6]=msg
        if(k==8):
            B8.config(text=msg)
            self.l1[7]=msg
        if(k==9):
            B9.config(text=msg)
            self.l1[8]=msg

        print self.counter
        print self.l1

        if(self.l1[0]==self.l1[1] and self.l1[1]==self.l1[2] and self.l1[0]!=1):
            self.flag=1
        if(self.l1[3]==self.l1[4] and self.l1[4]==self.l1[5] and self.l1[3]!=1):
            self.flag=1
        if(self.l1[6]==self.l1[7] and self.l1[7]==self.l1[8] and self.l1[6]!=1):
            self.flag=1
        if(self.l1[0]==self.l1[3] and self.l1[3]==self.l1[6] and self.l1[3]!=1):
            self.flag=1
        if(self.l1[1]==self.l1[4] and self.l1[4]==self.l1[7] and self.l1[4]!=1):
            self.flag=1
        if(self.l1[2]==self.l1[5] and self.l1[5]==self.l1[8] and self.l1[5]!=1):
            self.flag=1
        if(self.l1[0]==self.l1[4] and self.l1[4]==self.l1[8] and self.l1[7]!=1):
            self.flag=1
        if(self.l1[2]==self.l1[4] and self.l1[4]==self.l1[6] and self.l1[8]!=1):
            self.flag=1

        if(self.flag==1 and msg=="X"):
            L.config(text="Player 1 Wins ")
        if(self.flag==1 and msg=="0"):
            L.config(text="Player 2 Wins ")
        if(self.flag==1):
            self.flag=0
            B1.config(text="")
            B2.config(text="")
            B3.config(text="")
            B4.config(text="")
            B5.config(text="")
            B6.config(text="")
            B7.config(text="")
            B8.config(text="")
            B9.config(text="")
            for x in range(0,len(self.l1),1):
                self.l1[x]=1
                
ob = g_Game()

B1=Button(text="",command=lambda:ob.game(1))
B1.place(x=10,y=20,height=30,width=50)
B2=Button(text="",command=lambda:ob.game(2))
B2.place(x=90,y=20,height=30,width=50)
B3=Button(text="",command=lambda:ob.game(3))
B3.place(x=170,y=20,height=30,width=50)
B4=Button(text="",command=lambda:ob.game(4))
B4.place(x=10,y=70,height=30,width=50)
B5=Button(text="",command=lambda:ob.game(5))
B5.place(x=90,y=70,height=30,width=50)
B6=Button(text="",command=lambda:ob.game(6))
B6.place(x=170,y=70,height=30,width=50)
B7=Button(text="",command=lambda:ob.game(7))
B7.place(x=10,y=130,height=30,width=50)
B8=Button(text="",command=lambda:ob.game(8))
B8.place(x=90,y=130,height=30,width=50)
B9=Button(text="",command=lambda:ob.game(9))
B9.place(x=170,y=130,height=30,width=50)

L=Label(Top,text="")
L.place(x=80,y=180,height=30,width=80)
Top.mainloop()
