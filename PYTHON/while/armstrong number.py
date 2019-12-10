n=input("enter the number:")
x=0
y=0
z=0
t=n
while(n>0):
    x=n%10
    y=x*x*x
    z=z+y
    n=n/10

if(t==z):
    print "number is armstrong :"
else:
    print"number is not armstrong:"
