t=(11,23,23,45,77,77)
print("Tuple:",t)
l=list(t)
s=[]
for i in l:
    if l.count(i)>1 and i not in s:
        s.append(i)
print("Repeated element:",tuple(s))
