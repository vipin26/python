s1= raw_input("enter a string :")
print"you inserted string :",s1
print"Length of string is :",len(s1)

s1=s1+" "
s2 = ""

for i in range(0,len(s1),1):
    k=s1[i]
    if(k==" "):
        print s2,len(s2)
        s2=""
    if(k!=" "):
        s2=s2+k
        
        
