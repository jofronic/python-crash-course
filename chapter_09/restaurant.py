class Restaurant:
    """This class has resturant name and cuisine type"""
    def __init__(self, restaurant_name, cuisine_type):
        self.r_name = restaurant_name
        self.c_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to {self.r_name}")
        print(f"We serve {self.c_type} Mon through Friday")

    def open_restaurant(self):
        print(f"{self.r_name} is open!")

# restaurant = Restaurant('Mcdonalds', 'Fast Food')
# print(f"Is this {restaurant.r_name}?")
# print(f"I dont generally eat {restaurant.c_type} so I hope this isnt {restaurant.r_name}")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()