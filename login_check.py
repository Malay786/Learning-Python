correct_username = "admin"
correct_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

print("Username: " + username)
print("Password: " + password)

isCorrectUsername = correct_username == username
isCorrectPassword = correct_password == password

print(isCorrectUsername and isCorrectPassword)