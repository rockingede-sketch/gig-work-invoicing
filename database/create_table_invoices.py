import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Invoices") 
query = """CREATE TABLE Invoices( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billing_case_id int not null,
        billing_cust_id int not null,
        invoice_num varchar(20) not null,
        invoice_date date not null,
        due_date date not null,
        invoice_status varchar(20) not null,
        description varchar(200) null,
        salary_sum decimal(10,2) null,
        travel_exp_sum decimal(10,2) null,
        other_claims_sum decimal(10,2) null,
        amount_vat_0 decimal(10,2) not null,
        vat_percent decimal(5,2) NOT NULL,
        vat_sum decimal(10,2) not null,
        total_amount decimal(10,2) not null,
        reference varchar(30) not null,
        bankaccount varchar(18) not null,
        paid_amount decimal(10,2) null,
        penalty_interest decimal(10,2) null,
        payment_date date null,
        payment_state varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()