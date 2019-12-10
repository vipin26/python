class cal:
    def sum(self):
        a = input("enter a first number :")
        b = input("enter a second number:")
        c = a+b
        print("sum of 2 number is :"),c
class ini(cal):
    
    def num(self):
        a = input("enter a number :")
        if(a>0):
            print"number is positive"
        elif(a==0):
            print"number is zero :"
        else:
            print"number is negative :"

ob=ini()
ob.sum()
ob.num()

exit()
