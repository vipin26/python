s1=raw_input("Enter a File Name:")+".txt"
s2=raw_input("Enter a String: ")
f=open(s1,"w")
f.write(s2)
f.close()

f=open(s1,"r")
s=f.read()
print s
