class A:
    def a1(self):
        self.a=2
        print"ME FROM CLASS A:",self.a

class B(A):
    def b1(self):
        self.b=3
        print"ME FROM CLASS B:",self.b
        self.b=self.b+self.a
        print"SUM OF CLASS A AND B:",self.b

class C(A,B):
    def c1(self):
        self.c=5
        print"ME FROM CLASS C:",self.c
        self.c=self.c+self.b
        print"SUM OF ALL CLASSES ARE:",self.c

ob=C()
ob.a1()
ob.b1()
ob.c1()
