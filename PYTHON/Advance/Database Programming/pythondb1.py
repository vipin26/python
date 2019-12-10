import MySQLdb 

dbcon= MySQLdb.connect("localhost","root","12345","db1")
print "Database Connected Successfully "
dbcon.close()
