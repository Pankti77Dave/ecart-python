from unicodedata import category
import args
import random
import admin

arg = args.parser.parse_args()

if arg.setadmin is not None:
    # object.set_admin()
    username = arg.setadmin[0]
    password = arg.setadmin[1]
    adminobject = admin.admin()
    print(adminobject.set_admin(username, password))

elif arg.addcategory is not None:
    username = arg.addcategory[0]
    password = arg.addcategory[1]
    category_name = arg.categoryname[2]
    object.add_categories(username, password, category_name)

elif arg.addproduct is not None:
    username = arg.addproduct[0]
    password = arg.addproduct[1]
    product_name = arg.addproduct[2]
    product_desc = arg.addproduct[3]
    product_amount = arg.addproduct[4]
    product_category = arg.addproduct[5]
    object.add_products(username, password, product_name,  product_desc, product_amount, product_category)

elif arg.viewcategory is not None:
    object.view_categories()

elif arg.viewproducts is not None:
    object.view_products()

elif arg.userregister is not None:
    username = arg.userregister[0]
    password = arg.userregister[1]
    object.user_register(username, password)

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