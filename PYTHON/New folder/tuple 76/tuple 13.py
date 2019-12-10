m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print m1,
print
for i in range(0,3):
    for j in range(0,3):
        if(m1[i][j]%2==1 and m1[i][j]<9 and m1[i][j]>1):
            print m1[i][j],
    print
   
