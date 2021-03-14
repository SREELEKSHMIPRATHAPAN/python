string=input("enter a word")
last=string[-3:]
if(last=="ing"):
    string+="ly"
else:
    string+="ing "
print(string)