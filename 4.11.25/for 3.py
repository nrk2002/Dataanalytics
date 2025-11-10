count=0
for i in range(1,201):
    if i%4==0:
        count+=1
print("Numbers divisible by 6:",count)
for i in range(1,201):
    if i%6==0:
        count+=1
print("Numbers divisible by 9:",count)
