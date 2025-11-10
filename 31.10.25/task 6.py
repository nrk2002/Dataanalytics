print("To print grade")
mark=int(input("Enter your mark"))
if mark>=80 and mark<=100:
    print("Grade A")
elif mark>=65 and mark<80:
    print("Grade B")
elif mark>=50 and mark<65:
    print("Grade C")
elif mark>=35 and mark<50:
    print("Grade D")
elif mark>=0 and mark<35:
    print("Fail")
else:
    print("Enter a valid mark")
