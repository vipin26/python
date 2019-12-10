class student:
    roll = 0
    nm = ' '
    def insert(self):
        self.roll = input("enter a roll number :")
        self.nm =raw_input("enter a name :")
    def display(self):
        print"roll number",self.roll
        print"name",self.nm
ob = student()
ob.insert()
ob.display()
