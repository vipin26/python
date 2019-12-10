# length of string and count spaces

s2=raw_input("Enter a string : ")
print s2
print "length of string is : ",len(s2)

count=0
for i in range(0,len(s2),1):
    if(s2[i]==" "):
        count=count+1
print "spaces in your text :",count
