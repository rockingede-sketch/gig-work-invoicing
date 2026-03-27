import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Invoices") 
query = """CREATE TABLE Invoices( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billingCaseId int not null,
        billingCustId int not null,
        invoiceNum varchar(20) not null,
        invoiceDate date not null,
        dueDate date not null,
        invoiceStatus varchar(20) not null,
        description varchar(200) null,
        salarySum decimal(10,2) null,
        travelExpSum decimal(10,2) null,
        otherClaimsSum decimal(10,2) null,
        amountVat0 decimal(10,2) not null,
        vatPercent decimal(5,2) NOT NULL,
        vatSum decimal(10,2) not null,
        totalAmount decimal(10,2) not null,
        reference varchar(30) not null,
        bankaccount varchar(18) not null,
        paidAmount decimal(10,2) null,
        penaltyInterest decimal(10,2) null,
        paymentDate date null,
        paymentState varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()