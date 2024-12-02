import mysql.connector  

con = mysql.connector.connect(host="host", user="username", password="password", database="database_name")

con.close()

cur = con.cursor()
cur.execute("INSERT INTO Computer VALUES (1005,'Toshiba','Tecra',2013)")
print(cur.rowcount)
cur.close()


#Committing the changes
con.commit() 

con.close()