m1=int(input("Enter mark1:"))
m2=int(input("Enter mark2:"))
m3=int(input("Enter mark3:"))
if m1>=40 and m2>=40 and m3>=40:
    print("passed")
elif m1>=40 or m2>=40 or m3>=40:
    print("Fail")
else:
    print("Error")
avg=(m1+m2+m3)/3
if avg>=90:
    print("outstanding")
