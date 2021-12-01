import csv

def writing_csv():
  with open ("d.csv", "w") as data:
    csv_writer = csv.writer(data, delimiter = ",")

    for i in range(3):
      name = input("Enter the name")
      age = input("Enter the age")
      album = input("Enter the album")

      csv_writer.writerow(list((name, age, album)))


def reading_csv():
  with open("d.csv") as bob:
    csv_reader = csv.reader(bob)
    for line in csv_reader:
      print()
      for item in line:
        print(item, end = ",")


reading_csv()