# multiple inheritance
class A:
    def f1(self,a,b):
        c=a+b
        print"sum is :",c
class B:
    def f2(ask,x,y):
        z=x-y
        print"subtraction is :",z
class C:
    def f3(sell,m,n):
        o = m*n
        print"multiply is :",o
class D(A,B,C):
    def f4(sim,s,d):
        h=s/d
        print"divide is :",h
ob = D()
ob.f1(100,200)
ob.f2(200,100)
ob.f3(20,5)
ob.f4(400,5)
