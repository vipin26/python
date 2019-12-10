class A:
    def f1(self):
        self.roll = 1
        self.nm = 'Vipin'
        
class B(A):
    def f2(sell):
        print "roll number",sell.roll
        print "name",sell.nm
ob=B()
ob.f1()
ob.f2()
