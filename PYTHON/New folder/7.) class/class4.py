# Multiple objects 
class Student:
    def insert(self,m):
        age=input("Enter your Age :")
        print "Marks you inserted :",m
        print "Age is :",age



s1=[Student() for i in range(10)]
for j in range(1,3+1):
    print "________________________"
    marks=input("Enter your marks :")
    s1[j].insert(marks)
print "________________________"
print "Loop Ended"    
 
