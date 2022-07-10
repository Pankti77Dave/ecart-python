import db
import random
class user:
    database = db.db()
    conn = database.create_db()
    def user_register(self, username, password):
        cur = self.conn.cursor()
        cur.execute("SELECT username from USERS WHERE username=:username", {'username':str(username)})
        user_name = cur.fetchone()
        if user_name is None:
            self.conn.execute("INSERT INTO USERS VALUES (?,?)", (user_name, password))
            self.conn.commit()
            return('user registered successfully')
        else:
            return('username already exists')

    def view_categories(self):

        cur = self.conn.cursor()
        cur.execute("SELECT name from CATEGORIES")
        categories = cur.fetchall()
        for category in categories:
            return(category[0])

    def view_products(self):

        cur = self.conn.cursor()
        cur.execute("SELECT product_name from PRODUCTS")
        products = cur.fetchall()
        for product in products:
            print(product[0])

    def add_to_cart(self,username,password, product_name):
        cur = self.conn.cursor()
        cur.execute("SELECT username,password FROM USERS WHERE username=:username AND password=:password",
                            {"username": username, 'password': password})
        user_name = cur.fetchone()
        if user_name is not None and username==user_name[0] and password == user_name[1]:
            user_name = user_name[0]
            cur.execute("SELECT amount FROM PRODUCTS WHERE product_name=:product_name",{'product_name':product_name})
            amount=cur.fetchone()
            if amount is not None:
                amount=amount[0]
                id = random.randint(1, 10000000)
                self.conn.execute("INSERT INTO MYCART VALUES(?,?,?,?)", (id,product_name,amount,user_name))
                self.conn.commit()
                return('product is added to your cart')

            else:
                return('Product not found enter valid product name please')
        else:
            return('Incorrect Username Or Password')

    def view_cart(self):
        cur = self.conn.cursor()
        print('Your cart: \n')
        cur.execute("SELECT product_name, amount FROM MYCART")
        cart_products=cur.fetchall()
        for cart_product in cart_products:
            print(cart_product[0], cart_product[1])

    def remove_cart(self, username, password, product_name):
        cur = self.conn.cursor()
        cur.execute("SELECT username,password FROM USERS WHERE username=:username AND password=:password",
                            {"username": username, 'password': password})
        user_name = cur.fetchone()
        if user_name is not None and username==user_name[0] and password == user_name[1]:
            user_name = user_name[0]
            cur.execute("SELECT product_name FROM MYCART WHERE product_name=:product_name",{'product_name':product_name})
            p_name=cur.fetchone()
            if p_name is not None:
                self.conn.execute("DELETE FROM MYCART WHERE product_name=:product_name",{'product_name':p_name[0]})
                self.conn.commit()
                return('Product is removed from your cart')

            else:
                return('Product not found enter valid product name please')
        else:
            return('Incorrect Username Or Password')

