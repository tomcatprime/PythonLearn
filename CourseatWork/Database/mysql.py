import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

con = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database="lexlabs")

cur = con.cursor()
cur.execute("INSERT INTO Computer VALUES (1005,'Toshiba','Tecra',2013)")
print(cur.rowcount)

#Committing the changes
con.commit() 

con.close()