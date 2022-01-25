from clothing_size import ClothingSize

class Clothing:

    def __init__(self, colour, material, size):
        self.colour = colour
        self.material = material
        self.size = size

    def __str__(self):
        return f"This is clothing of {self.size} size, made of {self.colour} {self.material}"

    def __repr__(self):
        return f"clothing(colour={self.colour}, material={self.material}, size={self.size})"


if __name__ == "__main__":
    t_shirt = Clothing("Black", "Cotton", ClothingSize.SMALL.name )
    print(t_shirt)
    