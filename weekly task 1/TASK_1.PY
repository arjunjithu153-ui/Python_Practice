name = input("Enter student name: ")
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
total = mark1 + mark2 + mark3
average = total / 3
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)