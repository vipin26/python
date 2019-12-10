print"2 for 2D:"
print"3 for 3D:"
ch = int(input("enter your choice:"))
M = int(input("enter the member:"))
if(ch==2):
    print"WELCOME TO 2D ZONE:"
    if(M<=5):
        print "you got a discount of 5%:"
        bill = M*200
        print "Your bill is:",bill
        D = (bill*5)/100
        print "You saved:",D
        FB = bill-D
        print "your final bill is:",FB
    elif(M>5 and M<=10):
        print "you got a discount of 7%:"
        bill = M*200
        print "your bill is:",bill
        D = (bill*7)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB
    elif(M>10 and M<=20):
        print "you got a discount of 10%:"
        bill = M*200
        print "your bill is:",bill
        D = (bill*10)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB
    elif(M>20):
        print "you got a discount of 20%:"
        bill = M*200
        print "your bill is:",bill
        D = (bill*20)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB
elif(ch==3):
    print"WELCOME TO 3D ZONE:"
    if(M<=5):
        bill = M*300
        print "you got a discount of 5%:"
        print "your bill is:",bill
        D = (bill*5)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB
    elif(M>5 and M<=10):
        print "you got a discount of 7%:"
        bill = M*300
        print "your bill is:",bill
        D = (bill*7)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB
    elif(M>10 and M<=20):
        print "you got a discount of 10%:"
        bill = M*300
        print "your bill is:",bill
        D = (bill*10)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB
    elif(M>20):
        print "you got a discount of 20%:"
        bill = M*300
        print "your bill is:",bill
        D = (bill*20)/100
        print "you saved:",D
        FB = bill-D
        print "your final bill is:",FB

