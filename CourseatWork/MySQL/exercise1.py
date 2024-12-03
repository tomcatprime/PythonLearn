import mysql.connector
from dotenv import load_dotenv
import os 
load_dotenv()
#Replace the connection string of your MySQL server
HOST = os.getenv("HOSTNAME")
PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")

DATABASE_NAME="LexLabs"

con = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE_NAME, port=3306)
print(con)
try:
    print("Database connection established successfully.")
    # cur = con.cursor()
    # print("created")
    # cur.execute("INSERT INTO LexLabs  VALUES (1005,'Toshiba','Tecra',2013)")
    # print(cur.rowcount)
    # con.commit()
    # param = "1005"
    # cur.execute("DELETE FROM LexLabs WHERE CompId="+param)
    # print(cur.rowcount)
    # con.commit()

except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    
    con.close()