class Vehicle:
    """Base class for all vehicle"""
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

class Car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheel = 4
if __name__ == "__main__":
    c = Car("Audi", 'Ford', 'red', 2018)
    print(c.name, c.year, c.wheel)