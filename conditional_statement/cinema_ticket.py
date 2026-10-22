age = int(input("Enter your age: "))
if age < 5:
    print("Ticket price: Free")
elif age <= 12:
    print("Ticket price: ₹100")
elif age <= 59:
    print("Ticket price: ₹200")
else:
    print("Ticket price: ₹150")