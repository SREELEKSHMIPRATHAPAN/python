string="every day is a good day.today is a good day"
a=string.split(" ")
count=0
for i in range(0,len(a)):
      if (a[i])==" day" ) :
            count+=1
print("the occurence times of day is :",count)