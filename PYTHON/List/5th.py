# Count a number in list
L1=[]
c=0
n=int(input("Enter a number:"))
for i in range(0,n,1):
    x=int(input("ENter a Number in list:"))
    L1.insert(i,x)
    c=c+1
print("List is:",L1)
print("Number of element in List is:",c)
    
