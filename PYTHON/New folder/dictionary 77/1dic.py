dic={"Name ":" Bijay", "Age":20, "Gender":"Male"}
print dic
print 
print "Printing Keys Only"
for x in dic:
    print x

print 
print "Printing Key and Values in Loop"
for x in dic:
    print x,dic[x]


print 
print "Printing Values in Loop"
for x in dic:
    print dic[x]


print 
print "Printing Values in Loop"
for x in dic:
    print dic.values()
