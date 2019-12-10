# Learning string
# indexing

nm = raw_input("insert any string :")
print"the string you insterted :",nm

l= len(nm)
c= 0
for i in range(l-1,0,-1):
    if(nm[i]==' '):
        c=c+1
print "spaces in your text :",c
