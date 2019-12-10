#Reverse string

s1=raw_input("Enter a String : ")
s1=s1+" "
s2=" "
print "reverse string is =",
for i in range(len(s1)-1,-1,-1):
    k=s1[i]
    print k,
