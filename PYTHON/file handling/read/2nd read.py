f=open("whitespace.txt",'r')
s=f.read()
print(s)
c=d=e=0
for i in s:
    if(i==' '):
        c=c+1
    if(i== '.'):
        d=d+1
    if(ord(i)==10):
        e=e+1
        
print("spaces in your text :",c)
print("lines in your text : ",d)
print("paragraph in your text : ",e)
