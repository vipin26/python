lis1=[]
n = input("enter a number :")
for i in range(0,n):
    x=input("enter a element in list")
    lis1.insert(i,x)
for j in range(len(lis1)-1,-1,-1):
    print lis1[j]
