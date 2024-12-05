import mysql.connector
import os
from dotenv import *
import sys


load_dotenv()

HOST = os.getenv("HOSTNAME")
USER_NAME = os.getenv("USER_NAME")
PASSWORD_FILE = os.getenv("PASSWORD_FILE")

con = mysql.connector.connect(host=HOST, user=USER_NAME, password=PASSWORD_FILE, database="lexlabs", )
try:
    
    cur = con.cursor()
    cur.execute("INSERT INTO Computer VALUES (1005,'Toshiba','Tecra',2013)")
    print(cur.rowcount)


    param = "1005"
    cur.execute("DELETE FROM Computer WHERE CompId="+param)
    print(cur.rowcount)
except Exception as e:
    print(e)
finally:

#Committing the changes
    con.commit() 

    con.close()