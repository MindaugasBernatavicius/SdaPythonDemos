import csv

with open("C:\\Users\\Mindaugas\\Desktop\\delete.csv", 'r') as csvf:
  csvr = csv.reader(csvf)
  next(csvr)
  for line in csvr:
    print(line)


lst = [1, 2]
print(next(lst))


