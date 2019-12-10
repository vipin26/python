L1=[1,2,3,4,5]
print(L1)
L1=["sandeep","vipin","nitin"]
print(L1)
L1=[1,"sandeep",2,"vipin",3,"nitin"]
print(L1)
L1=[]
n=int(input("Enter a Number:"))
for i in range(0,n,1):
    n=input("Enter a Number in List:")
    L1.insert(i,n)
print("List is:",L1)
for j in range(0,len(L1),1):
    print("Index:",j)
print("ReVeRsE")
L1=[]
n=int(input("Enter a Number:"))
for i in range(0,n,1):
    n=input("Enter a Number in List:")
    L1.insert(i,n)
    L1.reverse()
print("List is:",L1)

print L1
"""for j in range(len(L1)-1,-1,-1):
    x=(L1[j])
    print(x)
