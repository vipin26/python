#OPERATOR OVERLOADING

class A:
    a=0
    def __init__(self):
        self.a=input("enter a number :")
        
    def __add__(self,k):
        print "difference is :",self.a-k.a

ob1=A()
ob2=A()
ob1+ob2
