import _sqlite3
class db:
    def create_db(self):
            conn=_sqlite3.connect('cart.db')
            c=conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS CATEGORIES(category_id integer  primary key autoincrement,name varchar COLLATE NOCASE)""")
            c.execute("""CREATE TABLE IF NOT EXISTS PRODUCTS (product_id integer primary key autoincrement,product_name varchar COLLATE NOCASE,description varchar,amount integer ,category_id integer ,FOREIGN KEY(category_id)REFERENCES CATEGORIES(category_id) ON DELETE CASCADE )""")
            c.execute("""CREATE TABLE IF NOT EXISTS USERS(username varchar primary key autoincrement,password varchar)""")
            c.execute("""CREATE TABLE IF NOT EXISTS MYCART(cart_id integer primary key autoincrement,product_name varchar COLLATE NOCASE,amount integer,username integer,FOREIGN KEY(username)REFERENCES USERS(username) ON DELETE CASCADE)""")
            c.execute("""CREATE TABLE IF NOT EXISTS USER_STATUS(id integer primary key autoincrement, username integer,coupon_id integer,coupon_time  )""" )
            c.execute("""CREATE TABLE IF NOT EXISTS ADMIN(id integer primary key autoincrement, username varchar  default 'admin',password varchar default 12345)""")
            return conn