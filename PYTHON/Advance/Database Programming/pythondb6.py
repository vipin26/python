#delete query

import MySQLdb

connection= MySQLdb.connect("localhost","root","12345","schooldb")
print "Database Connected Successfully "
cur = connection.cursor()

cid = input("Enter Country ID ")

query = "delete from countrytb where countryid=%s"
args = (cid)

cur.execute(query,args)
connection.commit()

print "Values Deleted Succesfully "
