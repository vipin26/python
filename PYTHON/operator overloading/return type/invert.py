class A:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y

    def __sub__(self,k):
        print"multiply is :"
        ob=A
        ob.a=self.a*k.b
        return ob
       
a= int(input("enter a 1st number :"))
b= int(input("enter a 2nd number :"))
ob1=A(a,b)
ob2=A(a,b)
ob3=ob1-ob2
print(ob3.a)

