import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Users") 
query = """CREATE TABLE Users( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        username varchar(100) not null,
        password varchar(250) NOT NULL,
        confirmed bit NOT NULL,
        validFrom date not null,
        validTo date null,
        disabled bit NOT NULL,
        created timestamp,
        updated timestamp)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()