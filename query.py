
from asyncio.windows_events import NULL
import psycopg2

class db:
    def test():
        print("hello")

    def create_tables():
        """ create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS business_partner (
                    bp_id SERIAL PRIMARY KEY,
                    bp_name VARCHAR(100) NOT NULL,
                    bp_email BYTEA NOT NULL,
                    company VARCHAR(255)
            )
            
            """,
            """ 
            CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    email VARCHAR(255),
                    role VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS products (
                prod_id SERIAL PRIMARY KEY,
                prod_name VARCHAR(255) NOT NULL,
                quantity INTEGER NOT NULL,
                bp_id INTEGER,
                FOREIGN KEY (bp_id)
                    REFERENCES business_partner (bp_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
            )
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        try:
            # connect to the PostgreSQL server
            cur = conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
            print("tables created")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def insert_proddata(prodname,quantity):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""INSERT INTO products (prod_name, quantity) VALUES (%s, %s)"""
        insert_value=(prodname,quantity)
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands,insert_value)
            cur.close()
            conn.commit()
            print("Row Added")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def update_prodquantity(prodname,quantity):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""UPDATE products SET quantity = %s WHERE prod_name = %s"""
        value = (quantity,prodname)
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands,value)
            cur.close()
            conn.commit()
            print("Row Updated")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def read_proddata():
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""SELECT * FROM products"""
        records=NULL
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands)
            
            records = cur.fetchall()
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return records



#db.create_tables()
#db.insert_proddata('item4','222')
#update_prodquantity('item1','50')

#for records in db.read_proddata():
#    print(records)

## to import class db use: query.db.function()