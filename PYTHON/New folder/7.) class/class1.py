class Student:
    roll=0
    nm=' '
    def insert(self):
        self.roll=input("Enter Roll Number :")
        self.nm=raw_input("Enter your name :")
        a=10
        b=20
        self.c=a+b

    def disp(self):
         print "The Roll Number you inserted :",self.roll
         print "The Name you inserted :",self.nm
         print "Sum of a and b is :",self.c

ob=Student()
ob.insert()
ob.disp()    
