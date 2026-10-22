marks = int(input("Enter the student's marks: "))
if marks >= 85:
    income = float(input("Enter family income in ₹: "))
    if income < 300000:
        print("Scholarship awarded")
    else:
        print("Scholarship not awarded: Family income must be below ₹3,00,000")
else:
    print("Scholarship not awarded: Marks must be at least 85")