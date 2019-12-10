# Reverse reverse string

s6=raw_input("Enter a String: ")
s6=" "+s6
s7=""
s8=""
for i in range(len(s6)-1,-1,-1):
    k=s6[i]
    if(k!=" "):
        s7=s7+k
    if(k==" "):
        for j in range(len(s7)-1,-1,-1):
            s8=s8+s7[j]
        s7=""
        print s8,
        s8=""
