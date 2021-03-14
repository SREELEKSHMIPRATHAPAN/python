n=int(input("enter number of terms required"))
n1=0
n2=1
c=0
if n<0:
    print("enter positive integers")
elif n==1:
    print("0")
else :
    print("the series is:")
    while c<n:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        c+=1
