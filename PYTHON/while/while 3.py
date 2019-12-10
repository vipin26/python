n = int(input("Enter a number :"))
rem = 0
rn = 0
while(n>0):
    rem = n%10
    rn = rn*10+rem
    n = n/10
print "reverse number is:",rn
