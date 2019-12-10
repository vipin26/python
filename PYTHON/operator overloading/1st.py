#OPERATOR OVERLOADING

class A:
    a=0
    def __init__(self,x):
        self.a=x
    def __add__(self,k):
        print "difference is :",self.a-k.a

ob1=A(600)
ob2=A(400)
ob1+ob2
