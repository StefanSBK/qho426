from tech import Tech

class Laser(Tech):

    MAX_RANGE = 100

    def __str__(self):
        return "It's a Laser!"
    
    def __repr__(self):
        return "laser()"


    def activate(self):
        print("Vzzzzzzzing! (Laser Activated)")
    
    def deactivate(self):
        print("Vzzzzzzuff (Laser off)")
    
    def fire(self, d_range = 10):
        if d_range <= Laser.MAX_RANGE:
            print(f"Laser shot at a distance {d_range}")
        else:
            print(f"Oh no! Cannot fire laser for a distance larger than {Laser.MAX_RANGE}")

if __name__ == "__main__":
    las = Laser()
    las.activate()
    las.fire(28)
    las.fire(10000)
    las.deactivate()
    