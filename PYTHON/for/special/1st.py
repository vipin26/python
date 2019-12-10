n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print j,
    print
for i in range(1,n+1,1):
    for j in range(i,0,-1):
        print j,
    print
