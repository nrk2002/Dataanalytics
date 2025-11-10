a=input("Enter a string:")
a="".join([i for i in a if not i.isdigit()])
print(a[0].upper()+a[1:-1]+a[-1].upper())

