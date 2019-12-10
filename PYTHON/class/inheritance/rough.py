class A:
    a=0
    b=0
    c=0
    def insert(self):
        self.a = int(input("enter a first number = "))
        self.b = int(input("enter a second number = "))

    def sum(self):
        self.c = self.a+self.b
        print "addition is =",self.c

class B(A):
    def sum(self):
        self.c = self.a*self.b
        print "multiplication is =",self.c

ob=B()
ob.insert()
ob.sum()
ob.mul()
