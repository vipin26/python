'update query
import MySQLdb

connection= MySQLdb.connect("localhost","root","12345","schooldb")
print "Database Connected Successfully "
cur = connection.cursor()

cid = int(input("Enter Country ID "))
cname = raw_input("Enter Country Name ")

query = "UPDATE countrytb SET countryname=%s where countryid=%s"
args = (cname,cid)

cur.execute(query,args)
connection.commit()

print "Values Updated Succesfully "
