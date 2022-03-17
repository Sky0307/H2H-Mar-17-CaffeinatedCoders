import query;
import psycopg2

class DataValidation():
    def __init__(self, *args):
        pass

    def write_to_database(self,prodlist):
        conn = psycopg2.connect(database="H2H", user = "postgres", password="admin123", host="localhost")
        cur=conn.cursor()
        command="""SELECT prod_name,company,quantity,products.bp_id FROM products INNER JOIN business_partner ON business_partner.bp_id=products.bp_id"""
        cur.execute(command)
        dbprodlist=cur.fetchall()
        print(dbprodlist)

        for prod in prodlist:
            cout=0
            for dbprod in dbprodlist:
                if(dbprod[0]==prod[1] and dbprod[1]==prod[0]):
                    finalquantity=dbprod[2]-prod[2]
                    if(finalquantity<0):
                        print("negative quantity")
                        cout=0
                        break
                    else:
                        command1="UPDATE products SET quantity = %s WHERE prod_name = %s AND bp_id = %s"
                        value1=(finalquantity,dbprod[3])
                        cur.execute(command1,value1)
                        cout=0
                        break
                else:
                    cout=cout+1
            if(cout!=0):
                
                command2="""INSERT INTO products (company,prod_name,quantity) VALUES (%s,%s,%s)"""
                value2=(prod[0],prod[1],prod[2])
                cur.execute(command2,value2)
        
        conn.commit()
        cur.close()
        conn.close()


#function = DataValidation()
# function.test()
#listing=['test']
#function.write_to_database(listing)
# db = Database.test()
# db.test()
