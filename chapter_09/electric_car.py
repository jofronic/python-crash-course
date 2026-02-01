class Car:
    """A simple attempt to represent a car. """
    def __init__(self, make, model, year):
        """Initialize attributes to descibe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
            """Print a statement showing the car's mileage"""
            print(f"This car has {self.odometer_reading} miles on it")

    def increment_odometer(self, miles):
        """Add the given amaount to the odometer reading"""
        if miles > 0:
             self.odometer_reading += miles
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
       """Initialize the battery's attributes."""
       self.battery_size = battery_size
        
    def describe_battery(self):
     """Print a statement describing the battery size."""
     print(f"This car has a {self.battery_size}-kWh battery.")
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """ Initilize attributes of parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
        self.battery_size = 40
    def describe_battery(self):
        """Print a statement describing the battery size"""
        return f"This car has a {self.battery_size}-KWh battery."
       

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print(my_leaf.describe_battery())
my_leaf.battery.describe_battery()