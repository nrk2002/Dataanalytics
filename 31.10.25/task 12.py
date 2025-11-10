print("Login system")
user="Ramya"
passkey="Ramya123"
name=str(input("Enter a user name:"))
if name==user:
    print("User name is correct")
    password=input("Enter a password:")
    if password==passkey:
        print("Successfully logged in")
    else:
        print("Wrong password, Try again")
else:
    print("wrong username")
