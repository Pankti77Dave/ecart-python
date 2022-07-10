import pytest
import admin
import user

def testcase_1():
    object = admin.admin()
    userobject = user.user()
    assert object.set_admin("pank", "pank") == "username already exists"
    assert object.add_categories("pank", "pank", "axys") == "Categories added successfully"
    assert object.add_products("pank", "pank", "hey", "value", "500", "axys") == "Product added successfully"
    assert userobject.user_register("panku", "pank") == "user registered successfully"
    assert not userobject.view_categories() == str
    assert not userobject.view_products() == str
    assert not userobject.view_cart() == str
    assert not userobject.add_to_cart("pank", "pank", "axys") == "product is added to your cart"
    assert not userobject.remove_cart("pank", "pank", "axys") == "Product is removed from your cart"

def testcase_2():
    object = admin.admin()
    userobject = user.user()
    assert object.set_admin("panktitest2", "pank") == "admin registered successfully"
    assert object.add_categories("pank", "panko", "axys") == "Incorrect Password"
    assert object.add_products("pank", "pank", "hey", "value", "500", "pink") == "Please enter correct category name"
    assert userobject.user_register("pank", "abcd") == "username already exists"
    assert not userobject.add_to_cart("pank", "pank", "axys") == "product is added to your cart"
    assert not userobject.remove_cart("pank", "pank", "axys") == "Product is removed from your cart"
