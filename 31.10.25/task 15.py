print("Scholorship program")
mark=int(input("Enter your mark:"))
if mark>=85 and mark<=100:
    att=int(input("Enter your attendance percentage:"))
    if att>=90:
        print("You are eligible for the scholorship")
    else:
        print("Sorry, you are not eligible")
else:
    print("Sorry, you are not eligible")
