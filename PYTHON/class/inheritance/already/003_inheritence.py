# Multiple Inheritence

class Calculation1:  
    def Summation(self,a,b):
        summation.a=input("enter a number :")
        summation.a=input("enter a number :")
        return a+b;  

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  

class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  
print(d.Summation)  
print(d.Multiplication(10,20))  
print(d.Divide(105,20))  
