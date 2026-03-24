import pymysql
import params as params

Host = params.Host
User = params.Username
Password = params.Password
dbname = params.Dbname

conn  = pymysql.connect(host=Host, user=User, password=Password)
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
databaseList = cursor.fetchall()

if tuple([dbname]) not in databaseList:
    cursor.execute("CREATE DATABASE " + dbname)
    print(f"New database {dbname} created")

else:
    print(f"Database {dbname} already exists")

cursor.execute("SHOW DATABASES")
databaseList = cursor.fetchall()

for database in databaseList:
  print(database)
  
conn.close()