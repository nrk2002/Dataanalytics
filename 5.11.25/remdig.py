a=input("Enter string and number:")
b=""
for alp in a:
    if not alp.isdigit():
        b+=alp
print(b)
