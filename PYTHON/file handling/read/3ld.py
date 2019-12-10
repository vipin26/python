s1=[]
i=0
x=" "
f=open("white.txt","w")
while(x!="halt"):
    s1.insert(i,x+chr(10))
    x=input("enter a string :")
f.writelines(s1)
f.close()
