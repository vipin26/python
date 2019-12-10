
s1=""
s1=raw_input("enter a string : ")
f=open("ele.txt",'w')
f.write(s1)
f.close()

f=open("ele.txt",'r')
s=f.read()
print s

c=0
for i in s:
    if(i==" "):
        c=c+1
print c
