st1= "Good Morning Have A Nice Day To All"
fw=open("Dictfile.txt","w")
fw.write(st1)
fw.close()
fr=open("Dictfile.txt","r")
st2=fr.read()

print("Dictfile.txt have the string:\n",st2)
st1=st2.split()
ls=[]

for i in st1:
    word_count = st1.count(i) 
    ls.append((i,word_count))     
     
dict1 = dict(ls)
print("\nFrequency of Words is:\n",dict1)
