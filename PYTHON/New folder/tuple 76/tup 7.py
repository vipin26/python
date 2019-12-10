tup=(2,3,4,6,8,10,15)
n=int(input("enter the value :"))
for i in range(0,7):
    if(tup[i]==n):
        print"n is in tuple"
        break
else:
    print"n is not in tuple"
        
