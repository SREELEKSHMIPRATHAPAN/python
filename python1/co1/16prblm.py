w1=input("enter a word")
w2=input("enter a word")
w1=w1.replace(w1[0:2],w2[0:2])
w2=w2.replace(w2[0:2],w1[0:2])
print(w1,w2)