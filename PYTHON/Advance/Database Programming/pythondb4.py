import MySQLdb

connection= MySQLdb.connect("localhost","root","12345","schooldb")
print "Database Connected Successfully "
cur = connection.cursor()

#cid = int(input("Enter Country ID "))
cname = raw_input("Enter Country Name ")

query = "INSERT INTO countrytb(countryname)VALUES(%s)"
args = (cname)

cur.execute(query,args)
connection.commit()

print "Values inserted succesfully "
