from Tkinter import*


class abc:
    a=""
    b=""
    def ccp(self,k):
        if(k==1):
            self.a=T1.get("1.0",END)
            self.b=T2.get("1.0",END)
            if(len(self.a)>1):
                T1.delete("1.0",END)
            if(len(self.b)>1):
                T2.delete("1.0",END)
                
        if(k==2):
            self.a=T1.get("1.0",END)
            self.b=T2.get("1.0",END)

            if(len(self.a)>1):
                self.a=T1.get("1.0",END)
            if(len(self.b)>1):
                self.b=T2.get("1.0",END)
        if(k==3):
            if(len(self.a)>1):
                T2.insert(END,self.a)
            if(len(self.b)>1):
                T1.insert(END,self.b)
ob = abc()
T1=Text(height=3,width=30)
T1.pack()
b1=Button(text="CUT",command=lambda:ob.ccp(1))
b1.pack()
b2=Button(text="COPY",command=lambda:ob.ccp(2))
b2.pack()
b3=Button(text="PASTE",command=lambda:ob.ccp(3))
b3.pack()
T2=Text(height=3,width=30)
T2.pack()

mainloop()
