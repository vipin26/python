"""#List Enter by user
L1=[]
n=int(input("Enter a Number:"))
for i in range(0,n,1):
    x=input("Enter a element in list:")
    L1.insert(i,x)
print("\nList is:",L1)
#index
L2=[]
M=int(input("Enter a Number:"))
for i in range(0,M,1):
    x=int((input("Enter a list number:")))
    L2.insert(i,x)
    print("index:","of",x,"is:",i)'
#Reverse List
L1=[]
L2=[]
n=int(input("Enter a Number:"))
for i in range(0,n,1):
    x=int(input("Enter a Number in List:"))
    L1.insert(i,x)
print("List is:",L1)
for j in range(len(L1)-1,-1,-1):
    print(L1[j])
"""
L1=[]
n=int(input("enter a number: "))
for i in range(0,n,1):
    x=int(input("enter a element in list: "))
    L1.insert(i,x)

L2=[]
m=int(input("enter a number: "))
for i in range (0,m,1):
    x=int(input("enter a number in list: "))
    L2.insert(i,x)
L3=L1+L2 
print L3
