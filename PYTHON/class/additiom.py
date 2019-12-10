x=input("enter the number")
m=0
n=0
b=x
while(x>0):
    m=x%10
    n=n*10+m
    x=x/10
if(b==n):
    print"the number is palendrom",n
else:
    print"the number is not palendrom"

