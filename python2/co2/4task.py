F=int(input("Enter range from:"))
L=int(input("Enter range to:"))
a=[]
for x in range(F,L+1):
    if x%2==0 and x**2:
        a.append(x)
print(a)