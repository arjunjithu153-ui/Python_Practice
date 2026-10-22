username = "admin"
password = "12345"
entered_username = input("Enter username: ")
if entered_username == username:
    entered_password = input("Enter password: ")
    if entered_password == password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")