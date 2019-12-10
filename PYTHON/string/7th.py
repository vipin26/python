# reverse reverse string
# eg-> computer is fun
# fun is computer

s1 = raw_input("Enter a String :")
s1 = " "+s1
s2 = ""
s3 = ""

for i in range(len(s1)-1,-1,-1):
    k=s1[i]
    if(k!=' '):
        s2=s2+s1[i]
    if(k==' '):
        for j in range(len(s2)-1,-1,-1):
            s3=s3+s2[j]
        s2=""
        print s3,
        s3=""
