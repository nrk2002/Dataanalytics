num=int(input("Enter:"))
add=0
while num>0:
    d=num%10
    add+=d*d
    num//=10
print(add)
    
