unit=int(input("Enter units consumed:"))
total=0
if 0<=unit<=100:
    total=1.5*unit
elif 101<=unit<=200:
    total=2.5*unit
elif 201<=unit<=300:
    total=4.5*unit
elif unit>300:
    total=5.0*unit
else:
    print("Enter valid data")

if total>1000:
    sur=total*0.10
    total=total+sur

print("Total charge:",total)
