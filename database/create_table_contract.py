import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Contract") 
query = """CREATE TABLE Contract( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billingCaseId int not null,
        frontmanCustId int not null,
        billingCustId int not null,
        contranctNr varchar(20) not null,
        contranctDate date not null,
        lastAnswerDate date not null,
        contractStatus varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()