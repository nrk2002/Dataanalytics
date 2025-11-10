a=str(input("enter a letter:"))
if len(a)>1 or a.isdigit():
    print("provide single alphabet")
elif a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("It is vowel")
else:
    print("It is consonant")
