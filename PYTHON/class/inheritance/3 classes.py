class A:
    def f1(self):
        print"me from class A"
        self.a =int(input("enter a first number"))
        

class B:
    def f2(sell):
        print"me from class B"
        sell.c=int(input("enter a second number"))
        
        
class C(A,B):
    def f3(ask):
        ask.x=ask.a+ask.c
        print"sum from class c"
        print"sum of a and b is:",ask.x
       
ob=C()
ob.f1()
ob.f2()
ob.f3()
        
