num = input("Enter: ")
rev = ""
i = len(num) - 1
while i >= 0:
    rev = rev + num[i]
    i = i - 1
print(rev)
