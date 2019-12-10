# Frequency of each character

s7=raw_input("Enter a String: ")
s8=""
for i in range(ord('a'),ord('z')+1,+1):
    count=0
    for j in s7:
        if(ord(j)==i):
            count=count+1
            s8=j
    if(count>0):
        print "Frequency of ",s8,"is",count
