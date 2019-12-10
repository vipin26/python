# MERGE 2 LIST
L1=[]
L2=[]
n=int(input("Enter a number in list1: "))
for i in range(0,n,1):
    x=int(input("Enter a element in list1: "))
    L1.insert(i,x)
print "List1 is: ",L1
n=int(input("Enter a number in list2: "))
for i in range(0,n,1):
    x=int(input("Enter a element in list2: "))
    L2.insert(i,x)
print "List2 is: ",L2
L3=sorted(L1+L2)
# Remove Duplicate in Final List
L3=list(dict.fromkeys(L3))
print "Final List is: ",L3
