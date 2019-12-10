# write exit file exit

s1=""
f=open("Exit.txt",'w')
while(s1!="Exit"):
    f.write(s1)
    s1=input("enter a sting : ")
f.close()

