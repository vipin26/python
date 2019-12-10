# reverse string

s1 = raw_input("enter a string :")
s1=s1+""
s2 = ""
print"the string is :",s1
print"length of string ",len(s1)

print"reverse string : "

for i in range(len(s1)-1,-1,-1):
  print s1[i],
  s2=s1
  s2=""
for j in range(0,len(s2),1):
   print (s2)
