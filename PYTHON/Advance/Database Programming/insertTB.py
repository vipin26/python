import MySQLdb

connection= MySQLdb.connect("localhost","root","12345","db1")
print "Database Connected Successfully "

iid=int(input("Enter Number "))
name=raw_input("Enter Name")

cur = connection.cursor()

query = "INSERT INTO tb1(rollno,name)VALUES(%s,%s)"
args = (iid,name)

cur.execute(query,args)
connection.commit()

print "Values inserted succesfully "
