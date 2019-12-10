class A:
    def a1(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
        print "Hello",self.x
                
class B(A):
    def b1(self):
        print self.x
        print self.y
        print self.z
        
        

        

ob=B()
ob.a1(10,20,30)
ob.b1()


        
    
        
        
