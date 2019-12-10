'''Loop Through a Dictionary : Print all key names in the dictionary, one by one:'''


dic={'Name':'Harry', 'Age':20, 'Marks':988}
print "Printing Keys"
for x in dic:
    print x



''' Print all values in the dictionary, one by one:'''    
print
print
print "Printing Values"
for x in dic.values():
    print x



''' Loop through both keys and values, by using the items() function:'''
print
print
print
for x, y in dic.items():
  print(x, y)
