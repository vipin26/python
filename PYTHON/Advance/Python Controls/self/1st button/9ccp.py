from Tkinter import*

class abc:
    def ccp(self,k):
        if(k==1):
            self.a=T1.get("1.0",END)
            T1.delete("1.0",END)
        if(k==2):
            self.a=T1.get("1.0",END)
        if(k==3):
            T2.insert(END,self.a)
        if(k==4):
            T1.delete("1.0",END)
            
ob = abc()
T1=Text(height=3,width=30)
T1.pack()
b1=Button(text="CUT",command=lambda:ob.ccp(1))
b1.pack()
b2=Button(text="COPY",command=lambda:ob.ccp(2))
b2.pack()
b3=Button(text="PASTE",command=lambda:ob.ccp(3))
b3.pack()
b4=Button(text="delete",command=lambda:ob.ccp(4))
b4.pack()
T2=Text(height=3,width=30)
T2.pack()

mainloop()
