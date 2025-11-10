num=int(input("Enter a value:"))
count=0
while num>0:
    count+=1
    num//=10
print(count)
