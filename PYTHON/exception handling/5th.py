class ins(Exception):
    def __str__(self):
        return "not valid for insurance"
    
print "                      ANSWERS ONLY CAPITAL LATTERS    "
G = raw_input("Enter your Gender : ")
A= input("Enter your Age : ")
if((A<25 and G=="FEMALE")or A<30 and G=="MALE"):
    s=raw_input("ARE YOU MARRIED : ")

try:
    if((G=="MALE") and A>=30):
        print "you are eligable for insurence"
    elif(((G=="MALE")and A<30)and s=="YES"):
        print "you are eligable for insurence"
    elif((G=="FEMALE") and A>25):
        print "you are eligable for insurence"
    elif(((G=="FEMALE") and A<25) and s=="YES"):
        print "you are eligable for insurence"
    else:
        raise ins
except ins as e:
    print e
