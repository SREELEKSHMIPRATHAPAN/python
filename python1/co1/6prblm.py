names=[]
n=input("enter number of names")
a_count=0 

for i in range(int(n)):
    name=input("input a name:")
    names.append(name)
for name in names:
    count=name.count("a")
    a_count+=count
print(a_count)