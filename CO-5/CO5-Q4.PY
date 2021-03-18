import csv
with open("movie2.csv",'w',newline='') as file:
  write=csv.writer(file)
  write.writerow(["Sl.No","Movie","Rating"])
  write.writerow(["1","Conjuring 2","3"])
  write.writerow(["2","Titanic","5"])
  write.writerow(["3","Avengers","6"])
  write.writerow(["4","Jumanji","5"])
  
with open("movie2.csv" ,'r') as file:
    data=csv.reader(file)
    print("Contents in Column 'Movie': ")
    for r in data:
        print(r[1])
