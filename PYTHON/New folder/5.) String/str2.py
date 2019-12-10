# Learnign Strings

nm=raw_input("Insert any string :")
# print "The String you inserted :",nm

l=len(nm)
c=0
for i in range(l-1,0,-1):
    if(nm[i]==' '):
        c=c+1

print "Spaces in your text :",c        
