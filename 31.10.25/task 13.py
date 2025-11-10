print("Job eligiblity program")
age=int(input("Enter your age:"))
if age>=18:
    expe=int(input("Number of years(experience):"))
    if expe>0:
        print("You are eligible for the job")
    else:
        print("Sorry, Experience required")
else:
    print("Sorry, age must be above 18")
