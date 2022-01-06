from person import Person

class Database:

  def __init__(self):
    self.name = "Stefan's Database"
    self.people = []
    self.num_of_people = len(self.people)
  
  def add_person(self, p):
    self.people.append(p)
    self.num_of_people += 1

  def remove_person(self, p):
    self.people.remove(p)
    self.num_of_people -= 1

  def display_all(self):
    for person in self.people:
      person.hello()


if __name__ == "__main__":
  p1 = Person("Orsi", 27)
  p2 = Person("Wesley")
  p3 = Person("Stefan", job = "Programmer", energy = 87)
  db = Database()
  print(f"{db.name} contains {db.num_of_people} objects")
  db.add_person(p2)
  db.add_person(p3)
  db.add_person(p1)
  db.display_all()
  print(f"{db.name} contains {db.num_of_people} objects")