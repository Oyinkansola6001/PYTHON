password = "python123"                 # correct password.

user_password = input("Enter your password: ")             # user's input.

while user_password != "python123":
    print("Wrong, try again.")
    user_password = input("Enter your password again: ")
print("Access granted")

