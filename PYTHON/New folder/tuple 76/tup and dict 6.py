l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[1,1,1],[1,1,1],[1,1,1]]
l3=[[0,0,0],[0,0,0],[0,0,0]]
print
for i in range(0,3):
    for j in range(0,3):
        l3[i][j]=l1[i][j]+l2[i][j]
        if(l3[i][j]%2==0):
            print l3[i][j],
    print


