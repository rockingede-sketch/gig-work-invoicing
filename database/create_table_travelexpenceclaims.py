import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS TravelExpenceClaims") 
query = """CREATE TABLE TravelExpenceClaims( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billingCaseId int not null,
        billingCaseRowId int not null,
        customerId int not null,
        travelBegin datetime not null,
        travelEnded datetime not null,
        country varchar(50) default 'Finland' not null,
        dailyAllowanceType varchar(10) null,
        dailyAllowanceCount decimal(5,2) null,
        dailyAllowanceAmount decimal(10,2) null,
        itinerary varchar(300) null,
        numberOfKm decimal(10,2) null,
        priceOfkm decimal(5,2) null,
        priceOfKmSum decimal(10,2) null,
        otherExpencesDesc varchar(300) null,
        otherExpencesSum decimal(10,2) null,
        claimsSum decimal(10,2) null,
        paymentDate date null,
        paymentState varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()
       