import db
import random
class admin:
    database = db.db()
    conn = database.create_db()
    def set_admin(self, username, password):
        cur = self.conn.cursor()
        cur.execute("SELECT username from ADMIN WHERE username=:username", {'username':str(username)})
        user_name = cur.fetchone()
        if user_name is None:
            self.conn.execute("INSERT INTO ADMIN VALUES(?,?)",(username, password))
            self.conn.commit()
            return'admin registered successfully'
        else:
            return'username already exists'
    
    def add_categories(self, username, adminpassword, category_name):
        cur = self.conn.cursor()
        cur.execute("SELECT password from ADMIN WHERE username=:username AND password=:password", {'username':str(username),'password':str(adminpassword)})
        password = cur.fetchone()
        if password is not None  and adminpassword == password[0]:  
            id = random.randint(1, 100000)
            self.conn.execute("INSERT INTO CATEGORIES (category_id, name) VALUES (?,?)", (id, category_name))
            self.conn.commit()
            return'Categories added successfully'
        else:
            return'Incorrect Password'
    
    def add_products(self,username, adminpassword, product_name, product_desc, product_amount, product_category):
        cur = self.conn.cursor()
        cur.execute("SELECT password from ADMIN WHERE username=:username AND password=:password", {'username':str(username),'password':str(adminpassword)})
        password = cur.fetchone()
        if password and adminpassword == password[0]:
            id = random.randint(1, 100000)
            cur.execute("SELECT * from CATEGORIES WHERE name=:name", {'name':str(product_category)})
            category = cur.fetchone()
            if category is not None:
                self.conn.execute("INSERT INTO CATEGORIES (category_id, name) VALUES (?,?)", (id, product_name))
                self.conn.commit()
                category_id = category[0]
                id = random.randint(1, 100000)
                self.conn.execute("INSERT INTO PRODUCTS VALUES (?,?,?,?,?)", (id,product_name,product_desc,product_amount,product_category))
                self.conn.commit()
                return('Product added successfully')
            else:

                return('Please enter correct category name')
        else:
            return('Incorrect password')
