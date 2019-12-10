L1=[]
L2=[]
n=input("Enter a Number:")
for i in range(0,n,1):
    x = input("enter a element in list :")
    L1.insert(i,x)

n=int(input("Enter Number to be Searched "))
flag=0
print "Indexes for the Numbers are : "
i=0
for j in range(0,len(L1),1):
    if(n==L1[j]):
        print j
        L2.insert(i,j)
        i=i+1
        flag=1
if(flag==1):
    print "Number is Found "
else:
    print "Number is not Found "

print "Number is found at ",L2," Indexes "
