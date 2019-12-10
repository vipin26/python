class A:
    def sum1(self):
        a = input("ENTER A FIRST NUMBER :")
        b = input("ENTER A SECOND NUMBER :")
            
        c = a+b
        print"sum of two number is = ",c
        self.s1(a,b)
        
class B(A):
    def s1(self,x,y):
        m = x*y
        print"multiplication of two number is = ",m

ob1 = B()
ob1.sum1()

