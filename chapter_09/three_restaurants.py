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



first_choice = Restaurant('Mcdonalds', 'American')
second_choice = Restaurant('Good Taste', 'Haitian')
third_choice = Restaurant('Olive Garden', 'Italian')

first_choice.describe_restaurant()
second_choice.describe_restaurant()
third_choice.describe_restaurant()