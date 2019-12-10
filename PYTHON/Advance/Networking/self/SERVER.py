from Tkinter import *
import socket

class Server:
    def __init__(self):
        Top=Tk()
        Top.geometry("350x350")
    
        self.L1=Label(Top,text="Server")
        self.L1.place(x=150,height=50,width=80)
        self.T1=Text(Top,height=30,width=80)
        self.T1.place(x=10,y=50,height=200,width=300)
        self.E1=Entry(Top,bd=5)
        self.E1.place(x=10,y=270,height=30,width=250)

        self.B1=Button(Top,text="Send")
        self.B1.place(x=270,y=270,height=30,width=50)
        Top.mainloop()

        s = socket.socket()    
        host = socket.gethostname()
	port = 12345        
        s.bind((host, port))
        s.listen(5)                 
        while True:
           c, addr = s.accept()     
           self.T1.insert("1.0",'Got connection from', addr)
           c.send('Thank you for connecting')
        c.close()                

ob = Server()
    
