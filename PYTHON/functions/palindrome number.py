def tab():
    a = int(input("enter a number :"))
    pal(a)
    
def pal(n):
    c=n
    r=0
    s=0
    while(n>0):
        r = n%10
        s = s*10+r
        n = n/10
    if(c==s):
        print"number is palindrome :"
    else:
        print"number is not palindrome :"
tab()
    
