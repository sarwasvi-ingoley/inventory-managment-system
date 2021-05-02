import MySQLdb

conn = MySQLdb.connect(host = "localhost", user = "sarwasvi", passwd = "sarwasvi")
print(conn)
mycursor = conn.cursor()
if conn:
    print('Connection successful')

else:
    print('Connection unsuccessful')

mycursor.execute("Create database if not exists inventory_management_system")
mycursor.execute("Show databases")
print(mycursor)
for db in mycursor:
    print(db)
