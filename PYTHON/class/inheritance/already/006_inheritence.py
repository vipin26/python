'''Calling same function name from different classes'''
class Bank:  
        def getroi(self):  
            print " I am Bank"  
class SBI:  
        def getroi(self):  
            print " I am SBI"  
      
class ICICI:  
        def getroi(self):
            print "  I am ICICI"
b1 = Bank()  
b2 = SBI()  
b3 = ICICI()

for i in (b1,b2,b3):
        i.getroi()
