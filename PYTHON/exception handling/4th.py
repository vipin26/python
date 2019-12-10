class MyError(Exception):
    def __str__(self):
        return "not a valid age"
    
age =input("enter your age:")
    
try:
    if(age<=18):
        raise MyError
    elif(age>=100):
        print"your age is too much"
    else:
        print "valid age"
except MyError as e:
        print e
