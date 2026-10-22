product_name =str(input("enter the product_name"))
unit_price =int(input("enter unit_price"))
quantity =int(input("enter the quantity"))
discount =int(input("enter the discount"))
subtotal = unit_price * quantity
final_bill = subtotal - discount
print("Product name:", product_name)
print("Unit price:", unit_price)
print("Quantity:", quantity)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final bill:", final_bill)