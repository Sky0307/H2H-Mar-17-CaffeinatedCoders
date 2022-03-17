import psycopg2

class db:
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
                    password VARCHAR(100) NOT NULL,
                    email VARCHAR(255),
                    role VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS products (
                prod_id SERIAL PRIMARY KEY,
                prod_name VARCHAR(255) NOT NULL,
                quantity INTEGER NOT NULL,
                company VARCHAR(255),
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

    #product table CRUD
    def insert_proddata(prodname,quantity,company):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        command="""SELECT bp_id FROM business_partner WHERE company = %s"""
        cur=conn.cursor()
        cur.execute(command,(company,))
        bpid=cur.fetchone()
        commands="""INSERT INTO products (prod_name, quantity,bp_id) VALUES (%s, %s, %s)"""
        insert_value=(prodname,quantity,bpid)
        
        try:
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
        records=None
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

    def delete_proddata(prodname):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""DELETE from products WHERE prod_name = %s"""
        value = (prodname)
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands,value)
            cur.close()
            conn.commit()
            print("Product deleted")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    #user table CRUD
    def insert_user(name,password,email,role):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""INSERT INTO users (user_name, password, email, role) VALUES (%s, %s, %s, %s)"""
        insert_value=(name,password,email,role)
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands,insert_value)
            cur.close()
            conn.commit()
            print("User Added")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def update_user(name,password=None,email=None):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        
        try:
            cur = conn.cursor()
            if(password!=None):
                commands="""UPDATE users SET password = %s WHERE user_name = %s"""
                value = (password,name)
                cur.execute(commands,value)
            #for command in commands:
            if(email!=None):
                commands="""UPDATE users SET email = %s WHERE user_name = %s"""
                value = (email,name)
                cur.execute(commands,value)
            cur.close()
            conn.commit()
            print("User Updated")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def read_user():
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""SELECT * FROM users"""
        records=None
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

    def delete_user(name):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""DELETE from users WHERE user_name = %s"""
        value = (name)
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands,value)
            cur.close()
            conn.commit()
            print("Product deleted")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    #business partner table CRUD
    def insert_bpdata(name,email,company):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""INSERT INTO business_partner (bp_name, bp_email, company) VALUES (%s, %s, %s)"""
        insert_value=(name,email,company)
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

    def update_bp(name,email=None,company=None):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        
        try:
            cur = conn.cursor()
            if(email!=None):
                commands="""UPDATE business_partner SET bp_email = %s WHERE bp_name = %s"""
                value = (email,name)
                cur.execute(commands,value)
            #for command in commands:
            if(company!=None):
                commands="""UPDATE business_partner SET company = %s WHERE bp_name = %s"""
                value = (company,name)
                cur.execute(commands,value)
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

    def read_bpdata():
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""SELECT * FROM business_partner"""
        records=None
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

    def delete_bpdata(bp_name):
        conn = None
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        commands="""DELETE from business_partner WHERE bp_name = %s"""
        value = (bp_name)
        try:
            cur = conn.cursor()
            #for command in commands:
            cur.execute(commands,value)
            cur.close()
            conn.commit()
            print("Row deleted")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()



#db.create_tables()
#db.insert_proddata('item4','123','companyA')
#update_prodquantity('item1','50')

#for records in db.read_proddata():
#    print(records)
#db.insert_bpdata('ali','1@b.com','companyA')
## to import class db use: query.db.function()
