class Rectangle:
    def __init__(self, width, height):
        print("I'm initializing a new Rectangle instance.")
        self.width = width
        self.height = height
    

    def calculate_area(self):
        return self.width * self.height

    def __del__(self):
        print("This reactangle of delete")

ob = Rectangle(3, 40)
print(ob.calculate_area())