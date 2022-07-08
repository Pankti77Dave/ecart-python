import db
import args
import random

class main:
    database = db.db()
    conn = database.create_db()
    def set_admin(self):
        cur = self.conn.cursor()
        username = input('Please set a username:')
        password= input('Please set a password:')
        cur.execute("SELECT username from ADMIN WHERE username=:username", {'username':str(username)})
        user_name = cur.fetchone()
        if user_name is None:
            self.conn.execute("INSERT INTO ADMIN VALUES(?,?)",(username, password))
            self.conn.commit()
            print('admin registered successfully')
        else:
            print('username already exists')
    
    def add_categories(self, username, adminpassword):
        cur = self.conn.cursor()
        cur.execute("SELECT password from ADMIN WHERE username=:username AND password=:password", {'username':str(username),'password':str(adminpassword)})
        password = cur.fetchone()
        if password is not None  and adminpassword == password[0]:  
            name = input('Please enter type of categories you want:') 
            name=name.lower()
            id = random.randint(1, 100000)
            self.conn.execute("INSERT INTO CATEGORIES (category_id, name) VALUES (?,?)", (id, name))
            self.conn.commit()
            print('Categories added successfully \n')
        else:
            print('Incorrect Password')
    
    def add_products(self,username, adminpassword):
        cur = self.conn.cursor()
        cur.execute("SELECT password from ADMIN WHERE username=:username AND password=:password", {'username':str(username),'password':str(adminpassword)})
        password = cur.fetchone()
        if password and adminpassword == password[0]:
            name = input('Please enter product name:')
            description=input('Please enter product description:')
            amount = input('Please enter product amount:')
            product_category=input('Please enter product category name:')
            #product_category=product_category.lower()
            id = random.randint(1, 100000)
            cur.execute("SELECT * from CATEGORIES WHERE name=:name", {'name':str(product_category)})
            category = cur.fetchone()
            if category is not None:
                self.conn.execute("INSERT INTO CATEGORIES (category_id, name) VALUES (?,?)", (id, name))
                self.conn.commit()
                category_id = category[0]
                id = random.randint(1, 100000)
                self.conn.execute("INSERT INTO PRODUCTS VALUES (?,?,?,?,?)", (id,name,description,amount,(category_id)))
                self.conn.commit()
                print('Product added successfully \n')
            else:

                print('Please enter correct category name')
        else:
            print('Incorrect password')

    def view_categories(self):

        cur = self.conn.cursor()
        cur.execute("SELECT name from CATEGORIES")
        categories = cur.fetchall()
        for category in categories:
            print(category[0])

    def view_products(self):

        cur = self.conn.cursor()
        cur.execute("SELECT product_name from PRODUCTS")
        products = cur.fetchall()
        for product in products:
            print(product[0])

    def user_register(self):
        cur = self.conn.cursor()
        username = input('Please set a username:')
        password= input('Please set a password:')
        cur.execute("SELECT username from USERS WHERE username=:username", {'username':str(username)})
        user_name = cur.fetchone()
        if user_name is None:
            self.conn.execute("INSERT INTO USERS VALUES (?,?)", (user_name, password))
            self.conn.commit()
            print('user registered successfully')
        else:
            print('username already exists')

    def add_to_cart(self,username,password):
        cur = self.conn.cursor()
        cur.execute("SELECT username,password FROM USERS WHERE username=:username AND password=:password",
                            {"username": username, 'password': password})
        user_name = cur.fetchone()
        if user_name is not None and username==user_name[0] and password == user_name[1]:
            user_name = user_name[0]
            product_name = input('enter product name to add')
            cur.execute("SELECT amount FROM PRODUCTS WHERE product_name=:product_name",{'product_name':product_name})
            amount=cur.fetchone()
            if amount is not None:
                amount=amount[0]
                id = random.randint(1, 10000000)
                self.conn.execute("INSERT INTO MYCART VALUES(?,?,?,?)", (id,product_name,amount,user_name))
                self.conn.commit()
                print('product is added to your cart')

            else:
                print('Product not found enter valid product name please')
        else:
            print('Incorrect Username Or Password')

    def view_cart(self):
        cur = self.conn.cursor()
        print('Your cart: \n')
        cur.execute("SELECT product_name, amount FROM MYCART")
        cart_products=cur.fetchall()
        for cart_product in cart_products:
            print(cart_product[0], cart_product[1])

    def remove_cart(self, username, password):
        cur = self.conn.cursor()
        cur.execute("SELECT username,password FROM USERS WHERE username=:username AND password=:password",
                            {"username": username, 'password': password})
        user_name = cur.fetchone()
        if user_name is not None and username==user_name[0] and password == user_name[1]:
            user_name = user_name[0]
            product_name = input('enter product name to remove:')
            cur.execute("SELECT product_name FROM MYCART WHERE product_name=:product_name",{'product_name':product_name})
            p_name=cur.fetchone()
            if p_name is not None:
                self.conn.execute("DELETE FROM MYCART WHERE product_name=:product_name",{'product_name':p_name[0]})
                self.conn.commit()
                print('Product is removed to your cart')

            else:
                print('Product not found enter valid product name please')
        else:
            print('Incorrect Username Or Password')


object = main()
arg = args.parser.parse_args()

if arg.setadmin is not None:
    object.set_admin()

elif arg.addcategory is not None:
    username = arg.addcategory[0]
    password = arg.addcategory[1]
    object.add_categories(username, password)

elif arg.addproduct is not None:
    username = arg.addproduct[0]
    password = arg.addproduct[1]
    object.add_products(username, password)

elif arg.viewcategory is not None:
    object.view_categories()

elif arg.viewproducts is not None:
    object.view_products()

elif arg.userregister is not None:
    object.user_register()

elif arg.addtocart is not None:
    username = arg.addtocart[0]
    password = arg.addtocart[1]
    object.add_to_cart(username, password)

elif arg.viewcart is not None:
    object.view_cart()

elif arg.removefromcart is not None:
    username = arg.removefromcart[0]
    password = arg.removefromcart[1]
    object.remove_cart(username, password)