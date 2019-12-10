# Find number and index
L1=[]
n=input("enter a number ")
for i in range(0,n):
    x=input("enter a element in list :")
    L1.insert(i,x)

s=input("enter a number you find :")
index=-1
for x in range (0,len(L1),1):
    if(s==L1[x]):
        index=x
if(index!=-1):
    print"number is found at ",index," Index"
else:
    print"number is not found"
