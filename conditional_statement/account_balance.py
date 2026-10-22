balance = 10000
amount = int(input("Enter the withdrawal amount: ₹"))
if amount > 0:
    if amount <= balance:
        if amount % 100 == 0:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance: ₹", balance)
        else:
            print("Error: Amount must be a multiple of ₹100")
    else:
        print("Error: Insufficient balance")
else:
    print("Error: Withdrawal amount must be greater than zero")