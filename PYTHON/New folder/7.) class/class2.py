class Student:
    roll=0
    nm=' '
    def insert(self):
        self.roll=input("Enter Roll Number :")
        self.nm=raw_input("Enter your name :")

    def disp(self):
         print "The Roll Number you inserted :",self.roll
         print "The Name you inserted :",self.nm

ob1=[Student() for i in range(3)]
for ob2 in ob1:
    ob2.insert()
    ob2.disp()    
