# writing a file by user
s1=""
f=open("user.txt",'w')
s1=raw_input("enter a string : ")
f.write(s1)
f.close()

f=open("user.txt",'r')
s=f.read()
print s


