l1=[]
for i in range(0,5,1):
    x=input('Enter 5 elements in list:')
    l1.insert(i,x)
print l1

s=1
for i in l1:
    s=1
    c=0
    f=0
    for k in range(s,-1,-1):
        if(l1[k]==l1[i]):
            f=f+1
        if(f==1):
            c=0
            for j in range(0,len(l1),1):
                if(i==l1[j]):
                    c=c+1
        print c
    s=s+1
    
            
