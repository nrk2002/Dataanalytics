num=12345
add=0
while num>0:
    d=num%10
    if d%2==0:
        add+=d
    num//=10
print(add)
