age=int(input("Enter age:"))
if age<13 and age>0:
    print("child")
elif age<19 and age>=13:
    print("teen")
elif age<59 and age>=20:
    print("adult")
elif age>=60:
    print("senior citizen")
else:
    print("Provide valid age")
