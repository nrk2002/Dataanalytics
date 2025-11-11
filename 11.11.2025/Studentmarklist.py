s=[ ("Alice",(85,90,78)),("Bob",(75,80,82)),("Charlie",(95,88,92))]
#1
print("Name with each mark:")
for i in s:
    name,mark=i
    print(f"{name}:",end=" ")
    sub=1
    for m in mark:
        print(f"Subject {sub} : {m},",end=" ")
        sub+=1
    print()
#2    
print("\nAverage marks of each student:")
for i in s:
    name, mark = i
    avg = sum(mark) / len(mark)
    print(f"{name} : Average: {avg}")
#3  
print("\nHighest mark of each student:")
for i in s:
    name, mark = i
    high = max(mark)
    print(f"{name} : Highest Mark: {high}")
#4    
print("\nAfter adding new person")
new=("David",(88,76,90))
s.append(new)
print(s)

print("\nName with each mark:")
for i in s:
    name,mark=i
    print(f"{name}:",end=" ")
    sub=1
    for m in mark:
        print(f"Subject {sub} : {m},",end=" ")
        sub+=1
    print()
    
print("\nAverage marks of each student:")
for i in s:
    name, mark = i
    avg = sum(mark) / len(mark)
    print(f"{name} : Average: {avg:.2f}")
    
print("\nHighest mark of each student:")
for i in s:
    name, mark = i
    high = max(mark)
    print(f"{name} : Highest Mark: {high}")
