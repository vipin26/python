class A:
    a=0
    
    def __init__(self,x):
        self.a=x
        
    def __floordiv__(self,k):
        ob=A
        ob.a=self.a*k.a
        return ob

ob1=A(10)
ob2=A(3)
ob3=ob1//ob2
print ob3.a
