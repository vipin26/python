a=0
b=0
c=0
try:
    a=input("enter value for a")
    b=input("enter value for b")
    c=a/b
except NameError:
    print"please input number"
except ZeroDivisionError:
    print"can not divide by zero"
else:
    print c

exit()
