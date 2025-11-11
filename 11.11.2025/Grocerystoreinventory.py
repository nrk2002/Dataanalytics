l=[["Fruits",["Apple","Banana","Mango"]],["Veg",["Carrot","Tomato","Potato"]],["Dairy",["Milk","Curd","Cheese"]]]
#1
print("Print each category with item")
for i in l:
    category,item=i
    print(f"Category : {category}:")
    for j in item:
        print(f"\t-{j}")
#2
print("\nAdd new item")
l[0][1].append("Orange")
print(l)
 #3       
print("\nRemove existing item")
l[1][1].remove("Potato")
print(l)
#4
print("\nCount items")
for i in l:
    category,item=i
    print(f"Category {category} has {len(item)} items")
#5   
print("\nUpdated list after modification")
for i in l:
    category,item=i
    print(f"Category : {category}:")
    for j in item:
        print(f"\t-{j}")
