#Left side triangle
n=int(input("Enter a number of Raws: "))
for i in range(1,n+1,1):
    for j in range(1,n+1-i,1):
        print("  "),
    for k in range(1,i+1,1):
        print k,
    print
