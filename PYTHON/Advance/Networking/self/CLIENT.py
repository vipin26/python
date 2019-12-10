from Tkinter import *
import socket

class Client:
    def __init__(self):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = 12345
		
		Top=Tk()
        Top.geometry("350x350")

        self.L1=Label(Top,text="CLIENT")
        self.L1.place(x=150,height=50,width=80)
        self.T1=Text(Top,height=30,width=80)
        self.T1.place(x=10,y=50,height=200,width=300)
        self.E1=Entry(Top,bd=5)
        self.E1.place(x=10,y=270,height=30,width=250)

        self.B1=Button(Top,text="Send",command=lambda:self.connect)
        self.B1.place(x=270,y=270,height=30,width=50)
        Top.mainloop()

    def connect():     #SOCKET PROGRAM
        self.s.connect((host, port))
        self.T1.insert("1.0",s.recv(1024))
        self.s.close()
        
ob = Client()
    