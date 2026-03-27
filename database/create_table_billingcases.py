import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS BillingCase") 
query = """CREATE TABLE BillingCase( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        frontmanCustId int not null,
        billingCustId int not null,
        stage varchar(100) not null,
        jobLocation varchar(100) not null,
        jobDate date not null,
        jobBegin datetime null,
        jobEnded datetime null,
        jobHours decimal(5,2) not null,
        workDescription varchar(500) null,
        workTask varchar(50) not null,
        contactPerson varchar(50) not null,
        phone varchar(15) not null,
        email varchar(100) not null,
        address varchar(50) not null,
        postcode char(5) null,
        postoffice varchar(50) null,
        billingMethod varchar(15) null,  
        eInvoiceAddress varchar(18) null,
        payerReference varchar(50) null,  
        payment decimal(10,2) not null,
        vatPercent decimal(5,2) NOT NULL,
        groupBilling bit not null,
        numberOfMembers int not null,
        ownerProfit decimal(10,2) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()