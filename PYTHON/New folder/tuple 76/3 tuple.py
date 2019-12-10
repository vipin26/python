tup=(10,"bj","cj","dj",20,30,40)
lst=[1,2,3,4,5]

print"printing list only"
for a in lst:
    print a,

print"printing list and tuple together"
lst.extend(tup)
for a in lst:
    print a,

print"printing tuple and list together"
tup=tuple(lst)
print tup,
