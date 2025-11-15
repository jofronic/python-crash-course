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


first_choice = Restaurant('Mcdonalds', 'American')
second_choice = Restaurant('Good Taste', 'Haitian')
third_choice = Restaurant('Olive Garden', 'Italian')

first_choice.describe_restaurant()
second_choice.describe_restaurant()
third_choice.describe_restaurant()