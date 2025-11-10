print("To check temperature")
temper=float(input("Enter degree "))
if temper>=40:
    print("Hot")
elif temper>=30 and temper<40:
    print("warm")
elif temper>=15 and temper<30:
    print("Cool")
else:
    print("Cold")
