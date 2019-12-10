#program to calculate the length of string
s1 = raw_input("insert any string :")
print"the string you instered ",s1

l = len(s1)
print"length of string",l
c= 0
for i in range(l-1,0,-1):
    if(s1[i]==' '):
        c=c+1
print "spaces in your text :",c
