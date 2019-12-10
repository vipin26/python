from Tkinter import *
Top=Tk()
Top.geometry("250x220")

class g_Game:
    counter=0
    msg=""
    def game(self,k):
        self.counter+=1
        if(self.counter%2==0):
            msg="X"
        else:
            msg="0"
        
        if(k==1):
            B1.config(text=msg)
        if(k==2):
            B2.config(text=msg)
        print self.counter
        
ob = g_Game()   
        
    
B1=Button(text="X",lambda:ob.game(1))
B1.place(x=10,y=20,height=30,width=50)
B2=Button(text="")
B2.place(x=90,y=20,height=30,width=50)
B3=Button(text="")
B3.place(x=170,y=20,height=30,width=50)
B4=Button(text="")
B4.place(x=10,y=70,height=30,width=50)
B5=Button(text="")
B5.place(x=90,y=70,height=30,width=50)
B6=Button(text="")
B6.place(x=170,y=70,height=30,width=50)
B7=Button(text="")
B7.place(x=10,y=130,height=30,width=50)
B8=Button(text="")
B8.place(x=90,y=130,height=30,width=50)
B9=Button(text="")
B9.place(x=170,y=130,height=30,width=50)

L=Label(Top,text="shyamlaal")
L.place(x=80,y=180,height=30,width=80)
Top.mainloop()
