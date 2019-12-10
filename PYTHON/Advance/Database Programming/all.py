import MySQLdb

dbcon=MySQLdb.connect("localhost","root","12345","db2")
print "Database connected sussfully "

cur=dbcon.cursor()

cur.execute("SELECT * FROM tb2")
print("fetchall :")
result=cur.fetchall()
for r in result :
    print (r)

cur.execute("SELECT * FROM tb2")
print("\nfetch one :")
res=cur.fetchone()
print(res)
dbcon.close()

