import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Payroll") 
query = """CREATE TABLE Payroll( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billingCaseId int not null,
        billingCaseRowId int not null,
        customerId int not null,
        payrollTime varchar(50) not null,
        workingHours decimal(5,2) not null,
        grossSalary decimal(10,2) not null,
        taxRate decimal(5,2) not null,
        tax decimal(10,2) not null,
        ttTyELProc decimal(5,2) null,
        ttTyEL decimal(10,2) null,
        ttTyottvakProc decimal(5,2) null,
        netSalary decimal(10,2) not null,
        taTyELProc decimal(5,2) null,
        taTyEL decimal(10,2) null,
        taTyottvakProc decimal(5,2) null,
        taTyottvak decimal(10,2) null,
        accInsurProc decimal(5,2) null,
        accInsur decimal(10,2) null,
        paymentDate date null,
        paymentState varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()
       