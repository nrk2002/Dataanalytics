count=0
for i in range(1,101):
    if  i==2 or i==3 or i==5 or i==7:
        print(i)
        count+=1
    elif i!=1 and i%2!=0 and  i%3!=0 and  i%5!=0 and  i%7!=0:
        print(i)
        count+=1
print("Total numbers:",count)
