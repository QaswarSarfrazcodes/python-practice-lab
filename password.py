password = input("Enter your password: ")
# checking the length of the password
if len(password) >= 8:
    # checking if the password consists of any numeral value
    special_characters = "!@#$%^&*()_+><:\""
    if any(char.isdigit() for char in password) and any(char in special_characters for char in password):  # special keys like !@#$%^&*()_+><:""
         print("password is strong.")
    else:
        print("Password must contain at least one number and one special character.")   
else:
    print("Password is too short. It must be at least 8 characters long.")