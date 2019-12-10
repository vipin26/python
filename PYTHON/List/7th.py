# Find a number with index
L1=[]
n=int(input("Enter a number: "))
for i in range(0,n,1):
    x=int(input("Enter a elemnt in list: "))
    L1.insert(i,x)
print("List is",L1)
a=int(input("Enter a number to searched: "))
flag=0
for j in L1:
    if(a==L1[j]):
        flag==1
        print(a,"Number is found at Index",j)
else:
    print("Number is not found")
