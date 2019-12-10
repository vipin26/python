s1=raw_input("Enter a string: ")
print "original string is: ",s1
s2=""
for i in s1:
    if(i=="a"or i=="e"or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        pass
    else:
        s2=s2+i
s1=s2
print"after removing vowels string is:",s1

    
