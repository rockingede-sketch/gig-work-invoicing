import pymysql
import params as params

conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS TravelExpenceClaims") 
query = """CREATE TABLE TravelExpenceClaims( 
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        billing_case_id int not null,
        billing_case_row_id int not null,
        customer_id int not null,
        travel_begin datetime not null,
        travel_ended datetime not null,
        country varchar(50) default 'Finland' not null,
        daily_allowance_type varchar(10) null,
        daily_allowance_count decimal(5,2) null,
        daily_allowance_amount decimal(10,2) null,
        itinerary varchar(300) null,
        number_of_km decimal(10,2) null,
        price_of_km decimal(5,2) null,
        price_of_km_sum decimal(10,2) null,
        other_expences_desc varchar(300) null,
        other_expences_sum decimal(10,2) null,
        claims_sum decimal(10,2) null,
        payment_date date null,
        payment_state varchar(20) not null,
        created timestamp not null,
        updated timestamp not null)"""

# To execute the SQL query
cur.execute(query)   

# To commit the changes
conn.commit()         
conn.close()
       