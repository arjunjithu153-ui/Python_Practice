entrance_mark = int(input("Enter the entrance examination mark: "))
if entrance_mark >= 60:
    maths_mark = int(input("Enter the Mathematics mark: "))
    if maths_mark >= 50:
        english_mark = int(input("Enter the English mark: "))
        if english_mark >= 50:
            print("Admission approved")
        else:
            print("Admission rejected: English mark must be at least 50")
    else:
        print("Admission rejected: Mathematics mark must be at least 50")
else:
    print("Admission rejected: Entrance examination mark must be at least 60")