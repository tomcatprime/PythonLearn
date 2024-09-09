def purchase_product(product_type, price):
    discount = 10
    total_price = price - price * discount / 100
    print("Total price of " +product_type+ " is "+str(total_price))
purchase_product("Mobile", 20000)
purchase_product("Shoe", 200)

print("##############################################################")
print("##############################################################")
print("##############################################################")
print("##############################################################")


def purchase_product1(product_type, price, mobile_brand = None):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        total_price = price + price * 2 / 100
    print("Total price of " +product_type+ " is "+str(total_price))
purchase_product1("Mobile", 20000, "Samsung")
purchase_product1("Shoe", 300)

print("##############################################################")
print("##############################################################")
print("##############################################################")
print("##############################################################")



def purchase_product2(product_type,price,mobile_brand,material):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        if material == "leather":
            tax = 5
        else:
            tax = 2
        total_price = price + price * tax / 100
    print("Total price of "+product_type+" is "+str(total_price))
purchase_product2("Mobile",20000,"Apple",None)
purchase_product2("Shoe",200,None,"leather")
purchase_product2("Shoe", 300, None, "cotton")