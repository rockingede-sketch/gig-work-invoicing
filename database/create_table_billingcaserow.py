import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS BillingCaseRow") 
query = """CREATE TABLE BillingCaseRow( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billing_case_id int not null,
        customer_id int not null,
        frontman bit not null,
        work_hours decimal(5,2) not null,
        share_of_pay decimal(5,2) not null,
        other_claims varchar(500),
        other_claims_amount decimal(10,2) NULL,
        travel_exp_claim_id int NULL,
        payroll_id int NULL,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()