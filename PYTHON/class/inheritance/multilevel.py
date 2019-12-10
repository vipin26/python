# multilevel inheritance
class A:
    def f1(self):
        self.roll = 1
        self.nm = 'vipn'
class B(A):
    def f2(sell):
        print"hello world"
class C(B):
    def f3(ask):
        print"roll no.",ask.roll
        print"name",ask.nm
ob=C()
ob.f1()
ob.f2()
ob.f3()
