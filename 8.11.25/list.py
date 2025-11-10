print("1 Reverse a given list in Python")
l=[100,200,300,400,500]
print(l)
rev=[]
for i in l:
    rev.insert(0,i)
print(rev)

print("\n2 Concatenate two lists")
l1=["Hello","Madam"]
l2=["Dear","Sir"]
l3=[]
for i in l1:
    l3.append(i)
for i in l2:
    l3.append(i)
print(l1,l2)
print(l3)

print("\n3 Remove empty strings from the list of strings")
l=["pen","","Pencil","eraser","","scale"]
print(l)
for i in l:
    if i=="":
        l.remove("")
print(l)

print("\n4 Write a Python program to convert a string to a list.")
a=input("Enter a string:")
print(a)
l=list(a)
print(l)

print("\n5 Check if a list contains an element")
l=[1,2,3,"a","b","c"]
print(l)
print("a in list:",'a' in l)

print("\n6 Remove all elements from a list")
l=[1,2,3,4]
print(l)
l.clear()
print(l)

print("\n7 Count the occurrence of a specific object in a list")
pets=['dog','cat','fish','fish','cat']
print(pets)
print(pets.count('fish'))

print("\n8 Return the length of a list")
l=[1,2,3,4]
print(l)
count=0
for i in l:
    count+=1
print(count)

print("\n9 Insert a value at a specific index in an existing list")
l=[1,2,3,4]
print(l)
l.insert(0,0)
print(l)

print("\n10 Write a Python program to clone or copy a list.")
l=[1,2,3,4]
print(l)
k=l.copy()
print(k)

print("\n11 Write a Python program to extend a list without append.")
l=[1,2,3,4]
k=[4,3,2,1]
print(l)
print(k)
k.extend(l)
print(k)

print("\n12 Remove duplicates from a list")
l=[3,2,2,1,1,1]
print(l)
l=list(set(l))
print(l)

print("\n13 Find the index of the 1st matching element")
l=[1,2,3,4]
print(l)
print(l.index(2))

print("\n14 check if an element is not in a list")
l=[1,2,3,"a","b","c"]
print(l)
print("z not in list:",'z' not in l)

print("\n15 Write a Python program to create a list of 5 numbers and print it.")
l=[]
n=int(input("Enter number of elements"))
for i in range(n):
    e=input("Enter a value:")
    l.append(e)
print(l)    
    
print("\n16 Write a program to find the length of a list using len().")
l=[1,2,3,"a","b","c"]
print(l)
print("Length:",len(l))

print("\n17 Write a program to access elements from a list using positive and negative indexes.")
l=[1,2,3,"a","b","c"]
print(l[1:-1])

print("\n18 Write a program to update the 3rd element of a list.")
l=[1,2,3,"a","b","c"]
print(l)
l[2]=56
print(l)

print("\n19 Write a program to delete an element from a list")
l=['a','b','c','d','e']
print(l)
l.remove('b')
print(l)

print("\n20 Write a program to append a new element to the list using append().")
l=['a','b','c','d','e']
print(l)
l.append('f')
print(l)

print("\n21 Write a program to insert an element at a specific position using insert().")
l=['a','b','c','d','e']
print(l)
l.insert(0,'r')
print(l)

print("\n22 Write a program to remove an element using remove().")
l=['a','b','c','d','e']
print(l)
l.remove('b')
print(l)

print("\n23 Write a program to remove the last element using pop().")
l=['a','b','c','d','e']
print(l)
l.pop()
print(l)

print("\n24 Write a program to clear all elements using clear().")
l=['a','b','c','d','e']
print(l)
l.clear()
print(l)

print("\n25 Write a program to print all elements of a list using a for loop.")
l=['a','b','c','d','e']
for i in l:
    print(i)

print("\n26 Write a program to find the sum of all elements using sum().")
l= [10, 20, 30, 40]
print(l)
total = sum(l)
print(total)

print("\n27 Write a program to find the maximum and minimum values using max() and min().")
l=[1,2,3,4,5]
print(l)
b=max(l)
c=min(l)
print("Max:",c)
print("Min:",b)

print("\n28 Write a program to count how many times an element appears using count().")
l=['a','a','b','b','b','c']
print(l)
print(l.count('a'))

print("\n29 Write a program to find the index of a specific element using index().")
l=['a','b','c']
print(l)
print(l.index('b'))

print("\n30 Write a program to reverse a list using reverse().")
l=[1,2,3,4,5]
l.reverse()
print(l)

print("\n31 Write a program to sort a list in ascending and descending order using sort().")
l=["Ramya","krishna","apple","Banana"]
l.sort()
print(l)
l=["Ramya","krishna","apple","Banana"]
l.sort(reverse=True)
print(l)

print("\n32 Write a program to copy one list to another using copy().")
a=[1,2,3]
print(a)
b=a.copy()
print(b)

print("\n33 Write a program to print only even numbers from a list.")
l=[1,2,3,4,5,6]
print(l)
for i in l:
    if i%2==0:
        print(i)

print("\n34 Write a program to print only odd numbers from a list.")
l=[1,2,3,4,5,6]
print(l)
for i in l:
    if i%2!=0:
        print(i)

print("\n35 Write a program to add two lists using + operator.")
l1=[1,2,3]
l2=[4,5,6]
print(l1)
print(l2)
print(l1+l2)

print("\n36 Write a program to repeat list elements using * operator.")
a=[1,2,3]
print(a)
b=a*2
print(b)

print("\n37 Write a program to check if an element exists in a list using in.")
l=[1,2,3,"a","b","c"]
print(l)
print("a in list:",'a' in l)

print("\n38 Write a program to slice a list (print first 3 and last 3 elements).")
l=[1,2,3,4,5,6]
print(l)
print(l[:3])
print(l[-3:])

print("\n39 Write a program to find the largest 2 numbers in a list.")
l=[16,43,92,76,30]
l.sort(reverse=True)
print(l)
print("largest numbers:",l[0:2])

print("\n40 Write a program to find duplicate elements in a list.")
l=[1,1,2,4,4,5,7]
dup=[]
for i in l:
    if l.count(i)>1:
        dup.append(i)
print(dup)

print("\n41 Write a program to remove duplicate elements from a list.")
l=[1,1,2,3,4,4]
print(l)
print(list(set(l)))

print("\n42 Write a program to merge two sorted lists into one sorted list.")
l1=[1,4,32,67,34]
print(l1)
l2=["a","B","g","F","y"]
print(l2)
l1.sort()
l2.sort(key=str.lower)
l3=l1+l2
print(l3)

print("\n43 Write a program to create a list of squares of numbers from 1 to 10 using a loop.")
sq=[]
for i in range(1,11):
    i*=i
    sq.append(i)
print(sq)
    
print("\n44 Write a program to separate even and odd numbers into two lists.")
l1=[]
l2=[]
for i in range(1,11):
    if i%2==0:
        l1.insert(i,i)
    else:
        l2.insert(i,i)
print(l1)
print(l2)

print("\n45 Write a program to create a nested list (list inside a list).")

print("\n46 Write a program to access elements from a nested list.")

print("\n47 Write a program to flatten a nested list (convert to one single list).")

print("\n48 Write a program to find common elements between two lists.")
l1=[1,2,3,4,5]
l2=[2,4,6,9,0]
print(l1)
print(l2)
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

print("\n49 Write a program to find elements present in one list but not in another.")
l1=[1,2,3,4,5]
l2=[2,4,6,9,0]
print(l1)
print(l2)
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)

print("\n50 Write a program to remove all occurrences of a specific element from a list.")
l=[1,1,2,2,2,3,4,4]
print(l)
l1=[]
for i in l:
    if i!=2:
        l1.append(i)
print(l1)

print("\n51 Write a program to convert a list into a tuple.")
l=[1,2,3]
print(tuple(l))

print("\n52 Write a program to find the average of list elements.")
l=[]
add=0
n=int(input("Enter number of elements"))
for i in range(n):
    e=int(input("Enter a value:"))
    l.append(e)
    add+=e
print(l)
print("Sum:",add)
print("average:",add/n)

print("\n53 Write a program to count positive, negative, and zero numbers in a list.")
l=[-2,-1,0,1,2,3,4]
print(l)
zerocount=0
poscount=0
negcount=0
for i in l:
    if i==0:
        zerocount+=1
    elif i>0:
        poscount+=1
    else:
        negcount+=1
print(zerocount)
print(poscount)
print(negcount)

print("\n54 Write a program to find product of all elements in a list (without using math.prod()).")
l=[1,2,3,4,5]
pro=1
for i in l:
    pro*=i
print(pro)
