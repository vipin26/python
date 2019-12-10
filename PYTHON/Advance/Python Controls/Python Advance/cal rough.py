from Tkinter import*
Top=Tk()
Top.geometry("200x300")


def cal(k):
    E.insert("1.0",str(k))

    

E=Text(Top)
E.place(x=10,y=50,height=50,width=100)
B1=Button(Top,text="1",command=lambda:cal(1))
B1.place(x=20,y=150,height=30,width=50)
B1=Button(Top,text="2",command=lambda:cal(2))
B1.place(x=20,y=200,height=30,width=50)
B1=Button(Top,text="3",command=lambda:cal(3))
B1.place(x=20,y=250,height=30,width=50)
Top.mainloop()
