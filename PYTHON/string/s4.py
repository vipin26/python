# longest word in string

s4 = raw_input("Enter a string : ")
s4 = s4+" "
s5 = ""
s6 = ""

for i in range(0,len(s4),1):
    k=s4[i]
    if(k==" "):
        print s5,":",len(s5)
        if(len(s5)>len(s6)):
            s6=s5
        s5=" "
    if(k!=" "):
        s5=s5+k
print "longest string is :",s6
