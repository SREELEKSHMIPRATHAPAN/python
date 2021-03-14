l1=[5,6,9,3]
l2=[2,4,6,8,10]
#a whether list are of same length
if(len(l1)==len(l2)):
    print("Both list are of same length")
else:
      print("Both are of different length")

#b whether list sums to same value
if(sum(l1)==sum(l2)):
    print("Both having same sum")
else:
    print("Both having different sum")

#c whether any value occur in both
l3=[x for x in l1 if x in l2]
print("common in both list",l3)