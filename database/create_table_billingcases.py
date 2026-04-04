import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS BillingCase") 
query = """CREATE TABLE BillingCase( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        frontman_cust_id int not null,
        billing_cust_id int not null,
        stage varchar(100) not null,
        jobLocation varchar(100) not null,
        job_date date not null,
        job_begin datetime null,
        job_ended datetime null,
        job_hours decimal(5,2) not null,
        work_description varchar(500) null,
        work_task varchar(50) not null,
        contact_person varchar(50) not null,
        phone varchar(15) not null,
        email varchar(100) not null,
        address varchar(50) not null,
        postcode char(5) null,
        postoffice varchar(50) null,
        billing_method varchar(15) null,  
        e_invoice_address varchar(18) null,
        payer_reference varchar(50) null,  
        payment decimal(10,2) not null,
        vat_percent decimal(5,2) NOT NULL,
        group_billing bit not null,
        number_of_members int not null,
        owner_profit decimal(10,2) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()