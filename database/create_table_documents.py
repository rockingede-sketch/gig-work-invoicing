import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Documents") 
query = """CREATE TABLE Documents( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        docType varchar(20) not null,
        docDate date not null,
        userId int null,
        contractId int null,
        invoiceId int null,
        payrollId int null,
        docname varchar(250) not null,
        filepath varchar(250) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()