class A:
    def f1(self):
        print"A class"
class B(A):
    def f2(self):
        print"B class"
ob=B()
ob.f1()
ob.f2()
