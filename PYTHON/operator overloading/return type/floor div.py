class A:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y

    def __mul__(self,k):

        ob=A
        ob.a=self.a//k.b
        return ob
a=input("enter a first number :")
b=input("enter a second number :")
ob1=A(a,b)
ob2=A(a,b)
ob3=ob1*ob2
print "division is" ,ob3.a
