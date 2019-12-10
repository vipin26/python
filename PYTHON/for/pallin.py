n=input(" Enter any number :")
r=0
s=0
t=n
while(n>0):
    r=n%10
    s=s*10+r
    n=n/10

if(t==s):
    print "Pallinrom Number"
else:
    print "Not Pallindrom"
