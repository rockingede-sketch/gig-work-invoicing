import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS BillingCustomers") 
query = """CREATE TABLE BillingCustomers( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        companyId varchar(11) not null,
        companyName varchar(50) NOT NULL,
        location varchar(50) NULL,
        contactPerson varchar(50) NOT NULL,
        email varchar(100) NOT NULL,
        phone varchar(15) NOT NULL,
        address varchar(50) NOT NULL,
        postcode char(5) NOT NULL,
        postoffice varchar(50) NOT NULL,
        eInvoideAddress varchar(18) NULL,
        operatorCode varchar(18) NULL,
        customerStatus varchar(20) NULL,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()