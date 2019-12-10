
class A:
    def sum(self,x,y):
        self.a=x
        self.b=y
        c=self.a+self.b
        print "value of c is",c

class B(A):
    def sum1(self):
        c=self.a*self.b
        print "value of c is",c
        
class C(B):
    def sum2(self):
        c=(self.a/self.b)*%
        print "value of c is",c


ob = C()

ob.sum(100.00,200.00)
ob.sum1()
ob.sum2()
