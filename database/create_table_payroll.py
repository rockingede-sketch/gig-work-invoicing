import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Payroll") 
query = """CREATE TABLE Payroll( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billing_case_id int not null,
        billing_case_row_id int not null,
        customer_id int not null,
        payroll_time varchar(50) not null,
        working_hours decimal(5,2) not null,
        gross_salary decimal(10,2) not null,
        tax_rate decimal(5,2) not null,
        tax decimal(10,2) not null,
        tt_tyel_proc decimal(5,2) null,
        tt_tyel decimal(10,2) null,
        tt_tyottvak_proc decimal(5,2) null,
        net_salary decimal(10,2) not null,
        ta_tyel_proc decimal(5,2) null,
        ta_tyel decimal(10,2) null,
        ta_tyottvak_proc decimal(5,2) null,
        ta_tyottvak decimal(10,2) null,
        acc_insur_proc decimal(5,2) null,
        acc_insur decimal(10,2) null,
        payment_date date null,
        payment_state varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()
       