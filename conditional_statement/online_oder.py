logged_in = input("Is the customer logged in? (yes/no): ")
if logged_in == "yes":
    cart = input("Does the cart contain items? (yes/no): ")
    if cart == "yes":
        payment = input("Is the payment successful? (yes/no): ")
        if payment == "yes":
            print("Order placed successfully")
        else:
            print("Payment failed")
    else:
        print("Cart is empty")
else:
    print("Please log in first")