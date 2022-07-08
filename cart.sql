--
-- File generated with SQLiteStudio v3.3.3 on Fri Jul 8 14:55:18 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: ADMIN
CREATE TABLE ADMIN(username varchar  default 'admin',password varchar default 12345);
INSERT INTO ADMIN (username, password) VALUES ('pankti', 'abcd');
INSERT INTO ADMIN (username, password) VALUES ('pank', 'abcd');
INSERT INTO ADMIN (username, password) VALUES ('username', 'password');

-- Table: CATEGORIES
CREATE TABLE CATEGORIES(category_id integer  primary key,name varchar COLLATE NOCASE);
INSERT INTO CATEGORIES (category_id, name) VALUES (29153, 'toys');
INSERT INTO CATEGORIES (category_id, name) VALUES (43790, 'pink');
INSERT INTO CATEGORIES (category_id, name) VALUES (60616, 'red');
INSERT INTO CATEGORIES (category_id, name) VALUES (70745, 'toys');
INSERT INTO CATEGORIES (category_id, name) VALUES (77293, 'blue');
INSERT INTO CATEGORIES (category_id, name) VALUES (79393, 'toys');
INSERT INTO CATEGORIES (category_id, name) VALUES (79537, 'toys');
INSERT INTO CATEGORIES (category_id, name) VALUES (83689, 'clothes');
INSERT INTO CATEGORIES (category_id, name) VALUES (84333, 'shoes');
INSERT INTO CATEGORIES (category_id, name) VALUES (90724, 'socks');

-- Table: MYCART
CREATE TABLE MYCART(cart_id integer primary key ,product_name varchar COLLATE NOCASE,amount integer,username integer,FOREIGN KEY(username)REFERENCES USERS(username) ON DELETE CASCADE);

-- Table: PRODUCTS
CREATE TABLE PRODUCTS (product_id integer primary key,product_name varchar COLLATE NOCASE,description varchar,amount integer ,category_id integer ,FOREIGN KEY(category_id)REFERENCES CATEGORIES(category_id) ON DELETE CASCADE );
INSERT INTO PRODUCTS (product_id, product_name, description, amount, category_id) VALUES (1172, 'black', 'blackred', 900, 84333);
INSERT INTO PRODUCTS (product_id, product_name, description, amount, category_id) VALUES (32316, 'pink', 'pinkred', 800, 83689);
INSERT INTO PRODUCTS (product_id, product_name, description, amount, category_id) VALUES (61922, 'shhs', 'ahhaa', 400, 29153);
INSERT INTO PRODUCTS (product_id, product_name, description, amount, category_id) VALUES (73367, 'yellow', 'yellowred', 700, 83689);

-- Table: USER_STATUS
CREATE TABLE USER_STATUS(id integer primary key , username integer,coupon_id integer,coupon_time  );

-- Table: USERS
CREATE TABLE USERS(username varchar primary key,password varchar);
INSERT INTO USERS (username, password) VALUES ('pankti', 'abcd');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
