k=1
N=int(input("Enter a number of rows: "))
for i in range(1,N+1):
    if(i%2!=0):
        for j in range(1,N+1):
            print k,
            k=k+1
        print 
    if(i%2==0):
        c=k+5
        k=k+6
        for j in range(1,N+1):
            print c,
            c=c-1
        print
            

