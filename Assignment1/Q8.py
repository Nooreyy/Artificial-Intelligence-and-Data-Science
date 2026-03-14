'''Login System (Using Logical Operators)

Ask user for:
Username
Password'''

username = input("Enter your username: ")
password = input("Enter your password: ")

pas = "1234"
user_name = "admin"

if username == user_name and password == pas:
    print("Login successful. Welcome!")
else:
    print("Login failed. Invalid username or password.")
