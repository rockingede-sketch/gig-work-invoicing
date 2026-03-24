import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS BillingCaseRow") 
query = """CREATE TABLE BillingCaseRow( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billingCaseId int not null,
        customerId int not null,
        frontman bit not null,
        workHours decimal(5,2) not null,
        shareOfPay decimal(5,2) not null,
        otherClaims varchar(500),
        otherClaimsAmount decimal(10,2) NULL,
        travelExpClaimId int NULL,
        payrollId int NULL,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()