m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print m1,
print
for i in range(0,3):
    for j in range(0,3):
        if(i*j==0 and j<2 and i<2):
            print m1[i][j],
    print
   
