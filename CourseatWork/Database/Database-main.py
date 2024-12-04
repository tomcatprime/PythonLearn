import mysql.connector
import os
from dotenv import *
import sys

path = sys.path[1]+'/config/.env'  #try .path[0] if 1 doesn't work
load_dotenv(path)
HOST = os.getenv("HOSTNAME")
USER_NAME = os.getenv("USER_NAME")
print(USER_NAME)
PASSWORD_FILE = os.getenv("PASSWORD_FILE")

con = mysql.connector.connect(host=HOST, user=USER_NAME, password=PASSWORD_FILE, database="lexlabs", )

cur = con.cursor()
cur.execute("INSERT INTO Computer VALUES (1005,'Toshiba','Tecra',2013)")
print(cur.rowcount)

#Committing the changes
con.commit() 

con.close()