print("To check a person is pass/fail")
mark=int(input("Enter your mark"))
if mark>=50 and mark<=100:
    print("You passed the exam")
elif mark<=50 and mark>=0:
    print("You are fail")
else:
    print("Enter a valid mark")
