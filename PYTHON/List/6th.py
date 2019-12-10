# Find Number in List
L1=[]
sign=0
n=int(input("Enter a Number:"))
for i in range(0,n,1):
    x=int(input("Enter a Element in List:"))
    L1.insert(i,x)
print("List is:",L1)
a=int(input("Enter a Number you find:"))
for j in L14:
    if(a==j):
        sign=1
if(sign==1):
    print("Number is found")
else:
    print("Number is not found")
