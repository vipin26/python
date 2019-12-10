l1=['nitin',"abc",10,10.599]
print(l1)
print(len(l1))

# append and insert method in list

l1.append("nitin")
print(l1)
l1.insert(1,10)
print(l1)

# remove  and pop method in list

l1.remove("nitin")
print(l1)
l1.pop(1) #pop keyword remove specific index or last item
print(l1)
del l1[2] # del specific index
print(l1)
l1=[]
n=int(input("Enter a number: "))
for i in range(0,n,1):
    x=int(input("enter a elemnent in list:"))
    l1.insert(i,x)
print l1
