age = int(input("Enter the applicant's age: "))
if age < 21:
    print("Not eligible due to age")
else:
    salary = float(input("Enter the monthly salary in ₹: "))
    if salary < 25000:
        print("Not eligible due to insufficient salary")
    else:
        credit_score = int(input("Enter the credit score: "))
        if credit_score < 700:
            print("Not eligible due to low credit score")
        else:
            print("Loan approved") 