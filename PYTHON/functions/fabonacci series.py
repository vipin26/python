def fab():
    a = int(input("enter a number :"))
    tab(a)
def tab(h):
    x = 0
    y = 1
    n = 0
    i = 1
    while(h>=i):
        n = x+y
        print n,
        x = y
        y = n
        i = i+1
fab()
        
