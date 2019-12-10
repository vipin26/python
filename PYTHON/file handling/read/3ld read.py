f=open("white.txt","r")
s=f.readlines()
for x in range(len(s)-1,-1,-1):
    print(s[x])

