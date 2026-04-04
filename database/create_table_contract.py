import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Contract") 
query = """CREATE TABLE Contract( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billing_case_id int not null,
        frontman_cust_id int not null,
        billing_cust_id int not null,
        contract_nr varchar(20) not null,
        contract_date date not null,
        last_answer_date date not null,
        contract_status varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()