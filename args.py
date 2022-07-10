import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--setadmin',
                    type=str,
                    nargs=2,
                    help='set admin'
                    )

parser.add_argument('--addcategory',
                    type=str,
                    nargs=3,
                    help='add categories'
                    )

parser.add_argument('--addproduct',
                    type=str,
                    nargs=6,
                    help='add product'
                    )
            
parser.add_argument('--viewcategory',
                    type=str,
                    nargs=1,
                    help='view category'
                    )
    
parser.add_argument('--viewproducts',
                    type=str,
                    nargs=1,
                    help='view products'
                    )

parser.add_argument('--userregister',
                    type=str,
                    nargs=2,
                    help='user register'
                    )

parser.add_argument('--addtocart',
                    type=str,
                    nargs=3,
                    help='add to cart'
                    )

parser.add_argument('--viewcart',
                    type=str,
                    nargs=1,
                    help='view cart'
                    )
                
parser.add_argument('--removefromcart',
                    type=str,
                    nargs=3,
                    help='remove from cart'
                    )