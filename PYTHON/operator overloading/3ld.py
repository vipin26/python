#OPERATOR OVERLOADING

class A:
    a=0 
    b=0
    def __init__(self,s,t):
        self.a=s
        self.b=t
    def __add__(self,k):
        print "difference is :",self.a-k.b
        print "multiplication is :",self.a*k.b

x=input("enter a 1st number :")
y=input("enter a 2nd number :")
        
ob1=A(x,y)
ob2=A(x,y)
ob1+ob2
