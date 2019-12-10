s1=[]
i=0
x=" "
f=open("whitespace.txt",'w')
while(x!="halt"):
    x=input("enter a string :")
    s1.insert(i,x+chr(10))

f.writelines(s1)
f.close()
