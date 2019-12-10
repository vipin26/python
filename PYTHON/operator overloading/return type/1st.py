class A:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def __add__(self,k):
        ob=A
        ob.a=self.a+k.a
        ob.b=self.b+k.b
        return ob
ob1=A(9,10)
ob2=A(10,9)
ob3 =ob1+ob2
print(ob3.a)
print(ob3.b)
