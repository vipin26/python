# insert by user

s1=input("enter a file name : ")
f=open(s1,'w')
f.close()

s2=input("enter a string : ")
f=open(s1,'w')
f.write(s2)
f.close()


