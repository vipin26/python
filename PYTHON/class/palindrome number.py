class palind:
    def reverse(self):
        n=input("enter a number :")
        t=n
        rn=0
        while(n>0):
            r=n%10
            rn = rn*10+r
            n=n/10
        if(t==rn):
            print"number is palindrome",rn
        else:
            print"number is not palindrome"
    
ob = palind()
ob.reverse()
    
    
