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
     
    def get_range(self):
        """Print a Statment about the range this battery provides"""
        if self.battery_size == 40: 
            range_miles = 150 
        elif self.battery_size ==65:
         range_miles = 225
        
        print(f"This car can go about {range_miles} miles on a full charge. ")
    
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """ Initilize attributes of parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()   
  

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()