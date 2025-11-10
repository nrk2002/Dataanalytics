print("To print grade")
mark=int(input("Enter your mark"))
if mark>=90 and mark<=100:
    print("Grade A")
elif mark>=75 and mark<90:
    print("Grade B")
elif mark>=50 and mark<75:
    print("Grade C")
elif mark>=0 and mark<50:
    print("Fail")
else:
    print("Enter a valid mark")
