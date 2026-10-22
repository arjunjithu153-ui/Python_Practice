age = int(input("Enter the candidate's age: "))
if age >= 21:
    experience = int(input("Enter years of experience: "))
    if experience >= 2:
        degree = input("Does the candidate have the required degree? (yes/no): ")
        if degree == "yes":
            print("Candidate is eligible for the job")
        else:
            print("Candidate is not eligible: Required degree is missing")
    else:
        print("Candidate is not eligible: At least 2 years of experience required")
else:
    print("Candidate is not eligible: Age must be at least 21")