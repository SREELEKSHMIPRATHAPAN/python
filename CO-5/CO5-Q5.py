import csv
f=open("leaves.csv","w")
writer=csv.DictWriter(f,fieldnames=["leaf","count"])
writer.writeheader()
writer.writerow({"leaf":"Mint","count":"1"})
writer.writerow({"leaf":"Neem","count":"2"})
writer.writerow({"leaf":"Tulsi","count":"3"})
writer.writerow({"leaf":"Banana","count":"4"})

f.close()
c=0
f=open("leaves.csv")
reader=csv.DictReader(f)
for row in reader:
    if c==0:
        print(f'{" ".join(row)}')
    print(f'{row["leaf"]},{row["count"]}')
f.close()
