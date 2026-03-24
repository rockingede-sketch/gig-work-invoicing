import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Customers") 
query = """CREATE TABLE Customers( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        userid int not null,
        customerRole varchar(20) NULL,
        taxnumber char(12) NULL,
        lastName varchar(100) NOT NULL,
        firstname varchar(250) NOT NULL,
        email varchar(100) NOT NULL,
        phone varchar(15) NOT NULL,
        address varchar(50) NOT NULL,
        postcode char(5) NOT NULL,
        postoffice varchar(50) NOT NULL,
        taxrRate decimal(5,2) not null,
        bankaccount char(18) not null,
        validFrom date not null,
        validTo date null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()