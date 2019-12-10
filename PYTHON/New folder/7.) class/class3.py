# Calling funtion of another class into another class
class Student:
    def insert(self):
        self.age=input("Enter your Age :")
        print "Age is :",self.age      

class Access:
        s1=Student()
        s1.insert()
        
            

#a1=Access()
#a1.ass()
