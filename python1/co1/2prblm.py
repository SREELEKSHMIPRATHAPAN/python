y=int(input("enter target year"))
print("The leap years are:")
for i in range(2021,y+1):
    if i%4==0 or i%400==0 and i%100!=0 :
        print(i)
              