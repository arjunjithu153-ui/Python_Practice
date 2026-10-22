units = int(input("Enter monthly electricity consumption in units: "))
if units <= 100:
    print("Low consumption")
elif units <= 200:
    print("Moderate consumption")
elif units <= 300:
    print("High consumption")
else:
    print("Very high consumption")