st1="Good Morning""\n""Have a Nice Day""\n""Are you okay ?""\n"
fw=open("Afile.txt","w")
fw.write(st1)
fw.close()

fr=open("Afile.txt","r")
st2=fr.readlines()
for i in st2:
    print(i)
