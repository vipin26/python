# Multiple Inheritence

class Calculation1:  
    def Summation(self,x,y):
        self.a = x
        self.b = y
        c=self.a+self.b
        print "Addition is :",c  

class Calculation2:  
    def Multiplication(self):  
        c=self.a*self.b
        print "Product is :",c

class Derived(Calculation1,Calculation2):  
    def Divide(self):
        c=self.a/self.b
        print "Division :",c

d = Derived()  
d.Summation(100.00,200.00)
d.Multiplication()
d.Divide()
