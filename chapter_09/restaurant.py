class Restaurant:
    """This class has resturant name and cuisine type"""
    def __init__(self, r_name, c_type):
        self.restaurant_name = r_name
        self.cusine_type = c_type
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"We serve {self.cusine_type} Mon through Friday")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

my_spot = Restaurant('Mcdonalds', 'Fast Food')
print(f"Is this {my_spot.restaurant_name}?")
print(f"I dont generally eat {my_spot.cusine_type} so I hope this isnt {my_spot.restaurant_name}")
my_spot.describe_restaurant()
my_spot.open_restaurant()