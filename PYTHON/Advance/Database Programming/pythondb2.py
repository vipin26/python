import MySQLdb

connection= MySQLdb.connect("localhost","root","12345","db1")
print "Database Connected Successfully "

cur = connection.cursor()

cur.execute("SELECT * FROM tb1") 
print("fetchall:")
result = cur.fetchall() 
for r in result:
    print(r)

cur.execute("SELECT * FROM tb1")
print("\nfetch one:")
res = cur.fetchone() 
print(res)
