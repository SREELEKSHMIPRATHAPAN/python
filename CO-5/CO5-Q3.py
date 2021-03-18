import csv
with open('movie1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SL.NO", "Movie", "Ratings"])
    writer.writerow([1, "Lord of the Rings", 5])
    writer.writerow([2, "Harry Potter", 6])
    writer.writerow([2, "Avengers", 5])


with open('movie1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
