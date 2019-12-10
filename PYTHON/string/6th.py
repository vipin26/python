# convert a string in short form

s1= raw_input("enter a string :")
s1=" "+s1
c=0
k=0
for i in range(0,len(s1),1):
    if(s1[i]==' ' and c<=2):
        if(c<=1):
            print s1[i+1],".",
        c=c+1
        k=i+1

print s1[k:len(s1)]
