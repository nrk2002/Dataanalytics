print("To check a value is alphabet or digit or special character")
a=input("Enter a value:")
if a.isalpha():
    print("Given value is an alphabet")
elif a.isdigit():
    print("Given value is a digit")
else:
    print("Given value is a special character")
