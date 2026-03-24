import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS CompanyCustomers") 
query = """CREATE TABLE CompanyCustomers( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        userid int not null,
        companyId char(9) not null,
        email varchar(100) NOT NULL,
        name varchar(50) NOT NULL,
        contactPerson varchar(50) NOT NULL,
        phone varchar(15) NOT NULL,
        address varchar(50) NOT NULL,
        postcode char(5) NOT NULL,
        postoffice varchar(50) NOT NULL,
        bankaccount char(18) not null,
        validFrom date not null,
        validTo date null,
        created timestamp,
        updated timestamp)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()