print "ch 1 for comercial:"
print "ch 2 for domestic:"
ch = int(input("enter a choice:"))
unit = int(input("enter a unit:"))
if(ch==1):
  if(unit<=100):
    Bill = unit*10
    print "your bill is:",Bill
elif(unit>100 and unit<=200):
    Bill = unit*15
    print "your bill is:",Bill
elif(unit>200 and unit<= 300):
    Bill = unit*20
    print "your bill is:",Bill
elif(unit>300):
    Bill = unit*25
    print "your bill is:",Bill
elif(ch==2):
    if(unit<=100):
            Bill = unit*7
    print "your bill is:",Bill
elif(unit>100 and unit<=200):
    Bill = unit*9
    print "your bill is:",Bill
elif(unit>200 and unit<= 300):
    Bill = unit*10
    print "your bill is:",Bill
elif(unit>300):
    Bill = unit*15
    print "your bill is:",Bill
        
