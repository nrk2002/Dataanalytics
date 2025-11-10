print("Length/upper/lower")
a=input("Enter a string:")
print("Length:",len(a))
print("Upper:",a.upper())
print("Lower:",a.lower())

print("count")
b=input("Enter a string to count how many a there:")
print("how many a are there:",b.count("a"))

print("Startswith")
c=input("Enter a string to check starts with hello:")
print("Check startswith:",c.startswith("Hello"))

print("endswith")
d=input("Enter a string to check ends with .com:")
print("Check endswith:",d.endswith(".com"))

print("Find")
e="This is python"
f="python"
pos=e.find(f)
print(pos)

print("Replace")
g="This is java"
print(g.replace("java","python"))

print("Strip")
h="     Ramya     "
print(h)
print(h.strip())

print("Capitalize")
i="ramya"
print(i)
print(i.capitalize())

print("split")
j="Hey this is ramya"
print(j.split())

print("join")
k="Ramya", "krishna"
print(" ".join(k))

print("Check alpahabelt")
i="Ramya"
print(i.isalpha())

print("check digit")
m="1234"
print(m.isdigit())

print("check alphabet and number")
n="ad12"
print(n.isalnum())

print("check islower")
o="ramya"
print(o.islower())

print("check is upper")
p="RAMYA"
print(p.isupper())

print("swapcase")
q="Ramya"
print(q.swapcase())

print("title")
r="i am ramya"
print(r.title())

print("check is space")
s="    "
print(s.isspace())

print("count vowel")
a=input("Enter string:")
a=a.lower()
count=0
for vow in a:
    if vow=="a" or vow=="e" or vow=="i" or vow=="o" or vow=="u":
        count+=1
print(count)

print("palindrome")
a="ramar"
s=a[::-1]
print(s)
if a==s:
    print("palindrome")
else:
    print("Not a palindrome")

print("remove number print alphabets")
a="Ram23ya"
res=""
for i in a:
    if i.isalpha():
        res+=i
print(res)

print("Replace")
a="I am ramya"
print(a.replace(" ","_"))

print("remove alphabet and print numbers")
a="Ram2387ya"
res=""
for i in a:
    if i.isdigit():
        res+=i
print(res)

print("print only word with capital letter starting in the sentence")
a="I am Ramya krishna"
b=a.split()
print(b)
for i in b:
    if i[0].isupper():
        print(i)

print("count how many times a letter occors")
a=input("Enter word with repeated letters:")
b=input("Enter letter to count:")
print(a.count(b))

print("Remove special charcter")
a="Hey! how are you?"
res=" "
for i in a:
    if i.isalnum() or i.isspace():
        res+=i
print(res)

print("check ends with mail")
a=input("Enter a email:")
print("Check endswith:",a.endswith("@gmail.com"))

print("Reverse")
a="Ramyakrishna"
rev=""
for i in a:
    rev=i+rev
print(rev)
