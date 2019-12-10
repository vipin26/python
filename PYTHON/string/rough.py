s1=raw_input("Enter a String: ")
s1=s1+" "
s2=""
s3=""
print "instered string: ",s1
print "length of string: ",len(s1)
count = 0
for i in range(0,len(s1),1):
    k=s1[i]
    if(k==" "):
        count=count+1
print "spaces in string: ",count
#count a word
for i in range(0,len(s1),1):
    s=s1[i]
    if(s==" "):
        print s2,":",len(s2)
        s2=""
    if(s!=" "):
        s2=s2+s
    
        
        

