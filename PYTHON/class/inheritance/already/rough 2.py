class Reverse:
    def rev(self):
        n = input("Enter a Number :")
        rem = 0
        RN = 0
        t=n
        while(n>0):
            rem = n%10
            RN = RN*10+rem
            n=n/10
        print RN
        self.pali(RN,t)

class palind(Reverse):
    def pali(self,a,b):
        if(a == b):
            print"number is palindrome :"
        else:
            print"number is not palindrome :"

ob = palind()
#ob.pali()
ob.rev()
exit()

