print("\nRight angled triangle")
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
print("\nInverted right angled triangle")
for i in range(1,5):
    for j in range(5-i):
        print(end="*")
    print()
print("\nLeft angled triangle")
for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
print("\nInverted left angled triangle")
for i in range(4,0,-1):
    for j in range(4-i):
        print(end=" ")
    for k in range(i):
        print(end="*")
    print()
print("\nSquare")
for i in range(1,4):
    for j in range(1,4):
        print(end=" * ")
    print()
print("\nHollow Square")
for i in range(1, 4):
    for j in range(1, 4):
        if i == 1 or i == 3 or j == 1 or j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\nHollow right angled triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end="")
        else:
            print(" ", end=" ")
    print()
print("\nPrint 8")
for i in range(7):
    for j in range(5):
        print("*" if (i in [0,3,6] and 0<j<4) or (j in [0,4] and i not in [0,3,6]) else " ", end="")
    print()
print("\nPattern 1")
for i in range(1, 6):
    for j in range(i):
        print(j+1, end="")
    print()
print("\nPattern 2")
for i in range(1,6):
    for j in range(6-i):
        print(j+1,end="")
    print()
print("\nPattern 3")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print(j, end="")
        else:
            print(" ", end=" ")
    print()
print("\nPattern 4")
a = ["A", "B", "C", "D", "E"]
for i in range(len(a)):
    for j in range(i + 1):
        print(a[i], end=" ")
    print()
print("\nPattern 5")
a = 'A'
for i in range(1, 6):   
    for j in range(i):
        print(a, end=" ")
        a = chr(ord(a) + 1)
        if a > 'O':
            break
    print()
    if a > 'O':
        break
print("\nPattern 6")
a = ["A", "B", "C", "D", "E"]
for i in range(len(a)):
    for j in range(i + 1):
        print(a[j], end=" ")
    print()








