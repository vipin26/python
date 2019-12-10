# frequency of each character in string

s1 = raw_input("Enter a string :")
x1=""
for i in range(ord('a'), ord('z')+1,1):
    count=0
    for x in s1:
        if(ord(x)==i):
            count+=1
            x1=x
    if(count>0):
        print "Frequency of ",x1," is ",count
