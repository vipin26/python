# Count a words in string

s3=raw_input("Enter a string : ")
print"you inserted string : ",s3
print "length of string is : ",len(s3)
s3=s3+" "
s4=""
for i in range(0,len(s3),1):
    if(s3[i]==' '):
        print s4," : ",len(s4)
        s4=""
    if(s3[i]!=' '):
        s4=s4+s3[i]
