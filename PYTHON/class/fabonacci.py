class fabonacci:
    def insert(self):
        n=input("enter a number :")
        a=0
        b=1
        next = 0
        i=0
        while(i<n):
            next=a+b
            print next,
            b=next
            a=b
            i=i+1
            
ob=fabonacci()
ob.insert()
