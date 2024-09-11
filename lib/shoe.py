class Shoe:
    def __init__(self, brand, size, color):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        self.brand = brand
        self.size = size
        self.color = color
        self.condition = "New"  # Initialize condition to "New"

    def cobble(self):
        self.condition = "New"  # Set condition to "New" after repair
        print("Your shoe is as good as new!")
