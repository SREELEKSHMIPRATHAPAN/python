l= []
for x in range(10):
    num = int(input("Enter an Integer : "))
    if(num>100):
        l.append("over")
    else:
        l.append(num)
print(l)