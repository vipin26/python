lis1=[]
n=input("enter a no.")
for i in range(0,n):
    x=int(input("enter a element in list : "))
    lis1.insert(i,x)

sign=0
s=int(input("enter a no. you find : "))
for x in lis1:
    if(s==x):
        sign=1
if(sign==1):
    print"number is found"
else:
    print"number is not found"
    
    
