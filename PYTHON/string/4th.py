# Count a words in string
s1 = raw_input("enter a string :")
s1 = s1+" "
s2 = ""

for i in range(0,len(s1),1):
    k=s1[i]
    if(k==' '):
        print s2," : ",len(s2)
        s2=""
    if(k!=' '):
        s2=s2+k
