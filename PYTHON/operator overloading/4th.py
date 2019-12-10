
#OPERATOR OVERLOADING

class A:
    a=0 
    b=0
    c=0
    d=0
    def __init__(self,s,t,u,v):
        self.a=s
        self.b=t
        self.c=u
        self.d=v
    def __add__(self,k):
        print "difference is :",self.a-k.b
        print "multiplication is :",self.c*k.d

x=input("enter a 1st number :")
y=input("enter a 2nd number :")
g=input("enter a 3ld number :")
h=input("enter a 4th number :")
ob1=A(x,y,g,h)
ob2=A(x,y,g,h)
ob1+ob2
