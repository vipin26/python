n = int(input("enter the number :"))
a = 0
b = 1
i = 1
c=0
while(i<n):
    c = a+b
    print c,
    a = b
    b = c
    i = i+1
