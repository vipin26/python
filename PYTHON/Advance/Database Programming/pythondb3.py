import MySQLdb

connection= MySQLdb.connect("localhost","root","12345","db1")
print "Database Connected Successfully "

cur = connection.cursor()
sql_command = "INSERT INTO tb1 values(117,'BHUshan')"
cur.execute(sql_command)
print "Inserted record  "
connection.commit()
