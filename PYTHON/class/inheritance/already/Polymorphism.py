'''Calling same function name from different classes'''
class Bank:  
    def getroi(self):
        a=929
        print " I am Bank"
        print "Values is :",a 

class SBI(Bank):  
    def getroi(self):  
        a=980
        print " I am SBI"  
        print "Values are :",a

class ICICI(SBI):  
    def getroi(self):
        b=90
        print "  I am ICICI"
        print "Values is :",b



ob1=Bank()
ob2=SBI()
ob3=ICICI()
  
for i in(ob1,ob2,ob3):
    i.getroi()
    
