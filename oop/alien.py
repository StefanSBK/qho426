from inhabitant import Inhabitant

class Alien(Inhabitant):

    def __init__(self, name = "E.T.", age = 0, tech = []):
        super().__init__(name, age)
        self.technology = tech
    
    def __str__(self):
        return f"Alien named {self.name} of age {self.age} who has the following technology: {self.technology}"

    def __repr__(self):
        return f"alien(name={self.name}, age={self.age}, energy={self.energy}, technology={self.technology}"

    def pickup(self, tech):
        self.technology.append(tech)
    
    def drop(self, tech):
        if tech in self.technology:
            self.technology.remove(tech)
    
if __name__ == "__main__":
    a = Alien("Leelo")
    a2 = Alien("Thanos")
    print(a)
    print(a2)
    a2.pickup("Time Stone")
    a2.pickup("Space Stone")
    print(a2)
    a2.drop("Time Stone")
    print(a2)
    