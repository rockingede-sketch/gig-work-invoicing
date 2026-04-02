import pymysql
import params as params
conn = pymysql.connect(host=params.Host, user=params.Username, password=params.Password, database=params.Dbname)

def add_foreign_key(connection, table, column, ref_table, ref_column):
    """
    Lisää ulkoavaimen (Foreign Key) olemassa olevaan tauluun.
    """
    try:
        with connection.cursor() as cursor:
            sql = f"""
                ALTER TABLE {table}
                ADD CONSTRAINT fk_{table}_{column}
                FOREIGN KEY ({column}) REFERENCES {ref_table}({ref_column})
                ON DELETE SET NULL;
            """
            print(sql)
            cursor.execute(sql)
        connection.commit()
        print(f"Ulkoavain lisätty: {table}.{column} -> {ref_table}.{ref_column}")
    except Exception as e:
        print(f"Virhe luotaessa ulkoavainta: {e}")

# Käyttö:
add_foreign_key(conn, "customers", "user_id", "users", "id")
#add_foreign_key(conn, "CompanyCustomers", "userId", "Users", "id")
#add_foreign_key(conn, "BillingCases", "frontman_cust_id", "Customers", "id")
#add_foreign_key(conn, "BillingCases", "frontman_cust_id", "CompanyCustomers", "id")