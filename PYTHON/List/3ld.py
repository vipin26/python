#UPDATING LIST VALUES
L=[2,3,4,5,6,7,8]
print("List is :",L)
print("Length of List is:",len(L))
L[3]=10
print("New List is:",L)
L[1:5]=[88,99]
print("After change List is:",L)

#Swapping of 2 number of List
L1=[1,2,3,4,5,6]
L2=[0]
L2[0]=L1[2]
L1[2]=L1[3]
L1[3]=L2[0]
print(L1)

#Delete Element From List
L=[77,88,99,66,55,44]
print("List is:     ",L)
del L[0]
print("After delete:",L)
del L[3]
print("After delete:",L)

# List operations
L1=[1,2,3,4,5]
L2=[5,6,7,8]
# Repetion
L3=L1*2
print("Repetion",L3)
#Concatenation
L4=L1+L2
print("Concatenation",L4)
#Iteration
print("Iteration")
for i in L1:
    print(i)
#Length
print("Length of L1 is:",len(L1))
print("Length of L2 is:",len(L2))    
#Iterating a List
L=["sandeep","vipin","nitin"]
for i in L:
    print(i);


